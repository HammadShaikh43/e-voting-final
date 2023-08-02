from flask import Flask, render_template, request, redirect, url_for
import csv
import hashlib
from MERKLE import *


app = Flask(__name__)

# Path to the CSV file to save the registered users
CSV_FILE_PATH = 'registered-users.csv'
admin_password = 'admin'
candidates_csv = 'candidates.csv'
registered_users_csv = 'registered-users.csv'
votes_csv = 'votes.csv'

# Load the registered users from the CSV file
registered_users = {}
try:
    with open(CSV_FILE_PATH, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            voter_id = row[0]
            name = row[1]
            hu_id = row[2]
            batch_year = row[3]
            registered_users[voter_id] = {"name": name, "hu_id": hu_id, "batch_year": batch_year}
except FileNotFoundError:
    print(f"No CSV file found at '{CSV_FILE_PATH}'")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        # Get form data
        name = request.form['name']
        hu_id = request.form['huid']
        batch_year = request.form['batch']
        name = name.capitalize()

        # Generate unique voter ID using uuid library
        voter_id = hashlib.sha256((hu_id + batch_year + name).encode()).hexdigest()

        # Check if the voter ID already exists in the database
        if voter_id in registered_users:
            error_message = "Voter ID already exists."
            return render_template("registration.html", error_message=error_message)

        # Add registered user to database
        registered_users[voter_id] = {"name": name, "hu_id": hu_id, "batch_year": batch_year}

        # Save the registered user to the CSV file
        with open(CSV_FILE_PATH, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([voter_id, name, hu_id, batch_year])
            csvfile.flush()

        # Display the generated voter ID to the user
        return render_template("registration.html", voter_id=voter_id)

    return render_template("registration.html")

@app.route('/signin', methods=['GET', 'POST', 'POST2'])
def signin():

    if request.method == 'POST2':
        voter_id = request.form['voterid']
        candidate = request.form['candidate']
        with open('votes.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([voter_id, candidate])
            csvfile.flush()
        
        return redirect(url_for('voted', voter_id=voter_id, candidate=candidate))
    
    if request.method == 'POST':
        voter_id = request.form['voterid']

        # Check if the voter ID is valid
        if voter_id in registered_users:
            # return render_template('voting.html', voter_id=voter_id)
            
            user = registered_users.get(voter_id)
            if user is None:
                # If the voter ID is not found, show an error message
                error_message = 'Invalid Voter ID'
                return render_template('signin.html', error_message=error_message)

            name = user["name"]
            huid = user["hu_id"]
            batch = user["batch_year"]
            return redirect(url_for('voting', voter_id=voter_id, name=name, huid=huid, batch=batch))

        # If the voter ID is not found, show an error message
        error_message = 'Invalid Voter ID'
        return render_template('signin.html', error_message=error_message)

    else:
        return render_template('signin.html')

@app.route('/voting', methods=['GET', 'POST'])
def voting():
    # Get voter ID from request parameters
    voter_id = request.args.get('voter_id')

    # Load the user's information from the database
    user = registered_users.get(voter_id)
    if user is None:
        # If the voter ID is not found, show an error message
        error_message = 'Invalid Voter ID'
        return render_template('signin.html', error_message=error_message)

    if request.method == 'POST':
        voter_id = request.args.get('voter_id')
        candidate = request.form['selected_candidate']
        cands1=[]
        cands2=[]
        cands3=[]
        cands4=[]

        '''
        add merkle implementation here, voter_id and candidate are relevant
        parameters, do not change the name of the variables, pls verify that
        everything is working after your changes
        
        '''
        with open(votes_csv,'r') as Votes:
            vote = csv.reader(Votes)
            
            for i in vote:
                cand=i[1]
                voter=i[0]
                
                with open(candidates_csv,'r') as Cands:
                    c = csv.reader(Cands)
                    for i in c:
                        if i[0] == cand:
                            if i[1]=='1':
                                cands1.append(voter)
                                    #for first candidate
                            elif i[1]=='2':
                                 cands2.append(voter)
                                    #for first candidate
                            elif i[1]=='3':
                                cands3.append(voter)
                                        #for first candidate
                            elif i[1]=='4':
                                cands4.append(voter)
    mt1 = MerkleTree(hash_type="sha256")
    mt1.add_leaves(cands1, True)
    mt1.build_merkle_tree()

    mt2 = MerkleTree(hash_type="sha256")
    mt2.add_leaves(cands2, True)
    mt2.build_merkle_tree()

    mt3 = MerkleTree(hash_type="sha256")
    mt3.add_leaves(cands3, True)
    mt3.build_merkle_tree()

    mt4 = MerkleTree(hash_type="sha256")
    mt4.add_leaves(cands4, True)
    mt4.build_merkle_tree()

    with open('votes.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([voter_id, candidate])
            csvfile.flush()
    return redirect(url_for('voted', voter_id=voter_id, candidate=candidate))


    # Load the candidate list from the candidates.csv file
    candidates = []
    with open('candidates.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            candidates.append(row[0])

    # Render the voting page with the user's information and the candidate list
    name = user["name"]
    huid = user["hu_id"]
    batch = user["batch_year"]
    return render_template('voting.html', name=name, huid=huid, batch=batch, candidates=candidates)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = 'Invalid Password'
    if request.method == 'POST':
        password = request.form.get('password')
        if password == admin_password:
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error_message='Invalid Password')
    else:
        return render_template('login.html')


@app.route('/admin')
def admin():
    # Read the candidates from the CSV file
    candidates = []
    with open(candidates_csv, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            candidates.append([row[0], row[1]])

    # Read the registered users from the CSV file
    registered_users = []
    with open(registered_users_csv, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            registered_users.append(row[1])

    # Read the votes from the CSV file
    # Read the votes from the CSV file
    votes = []
    with open(votes_csv, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            voter_id = row[0]
            with open(registered_users_csv, 'r') as g:
                reader2 = csv.reader(g)
                for row2 in reader2:
                    if row2[0] == voter_id:
                        voter_name = row2[1]
            candidate_name = row[1]
            votes.append((voter_name, candidate_name))


    return render_template('admin.html', candidates=candidates, registered_users=registered_users, votes=votes)

@app.route('/add_candidate', methods=['POST'])
def add_candidate():
    # Get the candidate name and ID from the form
    name = request.form.get('name')
    id = request.form.get('id')

    # Add the candidate to the CSV file
    with open('candidates.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, id])

    return redirect('/admin')

@app.route('/remove_candidate', methods=['POST'])
def remove_candidate():
    # Get the candidate ID from the form
    id = request.form.get('id')

    # Remove the candidate from the CSV file
    candidates = []
    with open('candidates.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] != id:
                candidates.append(row)

    with open('candidates.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(candidates)

    return redirect('/admin')

@app.route("/voted", methods=["GET", "POST"])
def voted():
    selected_candidate = request.args.get('selected_candidate')
    
    # with open('votes.csv', 'a', newline='') as csvfile:
    #         writer = csv.writer(csvfile)
    #         writer.writerow([voter_id, selected_candidate])
    #         csvfile.flush()

    # return selected_candidate
    return render_template("voted.html", selected_candidate=selected_candidate)

@app.route("/viewresults")
def viewresults():
    candidates = []
    votes1, votes2, votes3, votes4 = 0, 0, 0, 0
    with open('candidates.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            candidate_name = row[0]
            with open('votes.csv') as csv_file2:
                csv_reader2 = csv.reader(csv_file2)
                for row2 in csv_reader2:
                    if row2[1] == 'Hammad':
                        votes1 = votes1 + 1
                    elif row2[1] == 'Qasim':
                        votes2 = votes2 + 1
                    elif row2[1] == 'Ahmed':
                        votes3 = votes3 + 1
                    elif row2[1] == 'Someone':
                        votes4 = votes4 + 1
        candidates = [['Hammad', votes1//4], ['Qasim', votes2//4], ['Ahmed', votes3//4], ['Someone', votes4//4]]

    # with open('votes.csv') as Votes:
    #     vote = csv.reader(Votes)
    #     for row in vote:
    #         voterID=row[0]
    #         candName=row[1]
    #         with open('candidates_csv') as 



    return render_template("viewresults.html", candidates=candidates)

if __name__ == "__main__":
    app.run(port=3000, debug=True)