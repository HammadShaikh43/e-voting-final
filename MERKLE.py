# import csv
# import hashlib

# class MerkleTree:
#     def _init_(self, cand_id): 
#       #it will take string value of candidate ID
#       self.c_id = cand_id
#       self.L = [] #the leaves of the tree as an empty list
#       self.T = [] #the tree itself as an empty list

#     def add_leaf(self, l):
#       self.L.append(l)
#       #appending a leaf l to the leaves list L

#     def build_tree(self):
#       self.T = self.L.copy()
#       #making a copy of the leaves list and storing in the tree list
#       num_of_levels = int.bit_length(len(self.T) - 1)
#       #here we are identifying the levels in the tree
#       #int.bit_length gives the number of bits to represent an int in binary
#       #so by using this on the tree list T, we find its levels (also because T is a copy of L and it's length is not the number of levels)
#       for i in range(num_of_levels):
#           level = [] #creating an empty list level so that we can append the data of the two children (or one child)
#           for j in range(0, len(self.T), 2): #here we are performing a step of 2 because we are taking two nodes for each parent
#             Left = self.T[j] #left node of the tree
#             Right = self.T[j + 1] if j + 1 < len(self.T) else Left #j+1 is to check if the next leaf is there or not for current parent
#             #here we are checking if the next leaf in the tree is present (if the index j+1 is not greater then the length of the tree)
#             #if the index j+1 is greater than the length of the tree then we just make the right node as left node (basically one child)
#             #having left and right because a merkle tree follows the binary tree structutre so we assume at max two child nodes for each parent
#             Data = Left + Right #we sum both the nodes to get a value to perform hashing on
#             level.append(hashlib.sha256(Data.encode()).hexdigest()) #we perform sha 256 hashing and hex digest is used to create a hex value hash
#             #we have encoded the above data to allow for hashing
#             self.T = level #we then append the level to the tree
#         #we repeat this whole process for all number of levels

#     def get_root(self): #to get root of the tree
#         return self.T[0] #we return the first element from the list T

# # Function to verify the Merkle tree data is correct or not
# def verify_merkle_tree(tree, vot_id, cand_id): #here we take the parameters vot_id and cand_id as strings
#     curr_node = vot_id #we set the current node to use for searching as the voter id we took input
#     for i in range(len(tree)): #we iterate through the merkle tree
#         curr_node = hashlib.sha256(curr_node.encode()).hexdigest() #again we perform a hash for comparison on the current node
#         if i == cand_id: #we check if the index is equal to the cand_id for eg. if i==1 and cand_id==1
#             if tree[i] != curr_node: #we then check if the hash value at this cand_id in the tree is equal to the voter id (current node)
#                 return False #return false (meaning tampering or wrong data entered)
#     return True #(otherwise return true if the hashes are equal)

# # Read the CSV file of voters data 
# # def read_csv(fp): #we take in input the file path
# #     Merkles = {} #we create an empty dictionary to store the merkle trees
# #     with open(fp, 'r') as file: #we open the file to read it
# #         csv_reader = csv.reader(file) #we use the csv.reader to store the file in an iterable object
# #         for row in csv_reader: #we check every row
# #             voter_id = row[0] #we take the first column of the csv as voter id
# #             candidate_id = int(row[1]) #taking second column as candidate id
# #             if candidate_id not in Merkles: #we check if the candidate id exists in the Merkles or not
# #                 Merkles[candidate_id] = MerkleTree(candidate_id) #if not we insert it as a key
# #                 #the value of the key (candidate id) is an object of type MerkleTree with candidate id as input
# #             Merkles[candidate_id].add_leaf(voter_id) #we then add a leaf that is the the voter id data at that candidate id

# #     # Build the Merkle trees
# #     for candidate_id in Merkles: #we iterate for every candidate id in the merkle tree dictionary 
# #         Merkles[candidate_id].build_tree() #we call the buld function to build the tree

# #     return Merkles #we then return the dictionary



# import csv
# import hashlib

# class MerkleTree:
#     def _init_(self, cand_id): 
#       #it will take string value of candidate ID
#       self.c_id = cand_id
#       self.L = [] #the leaves of the tree as an empty list
#       self.T = [] #the tree itself as an empty list

#     def add_leaf(self, l):
#       self.L.append(l)
#       #appending a leaf l to the leaves list L
    

    

#     def build_tree(self):
#       self.T = self.L.copy()
#       #making a copy of the leaves list and storing in the tree list
#       num_of_levels = int.bit_length(len(self.T) - 1)
#       #here we are identifying the levels in the tree
#       #int.bit_length gives the number of bits to represent an int in binary
#       #so by using this on the tree list T, we find its levels (also because T is a copy of L and it's length is not the number of levels)
#       for i in range(num_of_levels):
#           level = [] #creating an empty list level so that we can append the data of the two children (or one child)
#           for j in range(0, len(self.T), 2): #here we are performing a step of 2 because we are taking two nodes for each parent
#             Left = self.T[j] #left node of the tree
#             Right = self.T[j + 1] if j + 1 < len(self.T) else Left #j+1 is to check if the next leaf is there or not for current parent
#             #here we are checking if the next leaf in the tree is present (if the index j+1 is not greater then the length of the tree)
#             #if the index j+1 is greater than the length of the tree then we just make the right node as left node (basically one child)
#             #having left and right because a merkle tree follows the binary tree structutre so we assume at max two child nodes for each parent
#             Data = Left + Right #we sum both the nodes to get a value to perform hashing on
#             level.append(hashlib.sha256(Data.encode()).hexdigest()) #we perform sha 256 hashing and hex digest is used to create a hex value hash
#             #we have encoded the above data to allow for hashing
#             self.T = level #we then append the level to the tree
#         #we repeat this whole process for all number of levels

#     def get_root(self): #to get root of the tree
#         return self.T[0] #we return the first element from the list T

# # Function to verify the Merkle tree data is correct or not
# def verify_merkle_tree(tree, vot_id, cand_id): #here we take the parameters vot_id and cand_id as strings
#     curr_node = vot_id #we set the current node to use for searching as the voter id we took input
#     for i in range(len(tree)): #we iterate through the merkle tree
#         curr_node = hashlib.sha256(curr_node.encode()).hexdigest() #again we perform a hash for comparison on the current node
#         if i == cand_id: #we check if the index is equal to the cand_id for eg. if i==1 and cand_id==1
#             if tree[i] != curr_node: #we then check if the hash value at this cand_id in the tree is equal to the voter id (current node)
#                 return False #return false (meaning tampering or wrong data entered)
#     return True #(otherwise return true if the hashes are equal)

# # # Read the CSV file of voters data 
# # def read_csv(fp): #we take in input the file path
# #     Merkles = {} #we create an empty dictionary to store the merkle trees
# #     with open(fp, 'r') as file: #we open the file to read it
# #         csv_reader = csv.reader(file) #we use the csv.reader to store the file in an iterable object
# #         for row in csv_reader: #we check every row
# #             voter_id = row[0] #we take the first column of the csv as voter id
# #             candidate_id = int(row[1]) #taking second column as candidate id
# #             if candidate_id not in Merkles: #we check if the candidate id exists in the Merkles or not
# #                 Merkles[candidate_id] = MerkleTree(candidate_id) #if not we insert it as a key
# #                 #the value of the key (candidate id) is an object of type MerkleTree with candidate id as input
# #             Merkles[candidate_id].add_leaf(voter_id) #we then add a leaf that is the the voter id data at that candidate id

# #     # Build the Merkle trees
# #     for candidate_id in Merkles: #we iterate for every candidate id in the merkle tree dictionary 
# #         Merkles[candidate_id].build_tree() #we call the buld function to build the tree

# #     return Merkles #we then return the dictionary

# # file_path = 'data.csv' # Replace with the path to your CSV file

# # # merkle_trees = read_csv(file_path)
    
# # #verify the Merkle trees data before and after voting process
# # C_ID = 1 #candidate ID 
# # V_ID = 'Voter1' #voter ID 
# # print('verifying Merkle tree for candidate ID: ', C_ID)
# # print('voter ID is : ', V_ID)
# # print('Before voting data: ', verify_merkle_tree(merkle_trees[C_ID].T, V_ID, C_ID))
    
# # #here we add a new voter to check
# # merkle_trees[C_ID].add_leaf('Voter2')
# # merkle_trees[C_ID].build_tree()

# # print('after voting data: ', verify_merkle_tree(merkle_trees[C_ID].T, V_ID, C_ID))


import hashlib
import binascii


class MerkleTree(object):
    def __init__(self, hash_type="sha256"):
        self.hash_function = getattr(hashlib, hash_type)
        self.reset_tree()

    def reset_tree(self):
        """ initializes an empty tree """
        self.leaves = list()
        self.levels = None
        self.complete = False

    def convert_to_hex(self, x):
        return x.hex()

    def get_leaf(self, index):
        """
        returns hex of leaf
        """
        return self.convert_to_hex(self.leaves[index])

    def add_leaves(self, datachunks, hash_required=False):
        """
        values = candidate IDs:  hashed using SHA-256 hash algorithm and the binary hashes are stored in merkle tree 
        """
        self.complete = False
        for chunk in datachunks:
            if hash_required:
                # converts string into byte to be acceptable by hash function
                chunk = chunk.encode('utf-8')
                # returns hashed encoded data in hexa decimal format
                chunk = self.hash_function(chunk).hexdigest()
                # a new bytearray object initialized from a string of hex numbers, 2 hexa-decimal digits per byte
            chunk = bytearray.fromhex(chunk)

            self.leaves.append(chunk)
        for m in range(0, len(self.leaves)):
            self.get_leaf(m)
        return self.leaves

    def leaves_count(self):
        """ 
        gives length of leaves
        """
        return len(self.leaves)

    def next_level_nodes(self):
        """ 
        Going up the merkle tree, a new level is generated with nodes of previous level
        """
        odd_leaf = None  # extra leaf from Right most that will be duplicated up the merkle tree
        N = len(self.levels[0])  # number of leaves on the current level
        if N % 2 == 1:  # if odd number of leaves on the current level
            odd_leaf = self.levels[0][-1]
            N -= 1

        level_up = []
        for left, right in zip(self.levels[0][0:N:2], self.levels[0][1:N:2]):
            level_up.append(self.hash_function(left+right).digest())
        if odd_leaf is not None:  # if odd number of leaves on the current level
            level_up.append(odd_leaf)
        # prepend new level
        self.levels.insert(0, level_up)
        # print(self.levels)

    def build_tree(self):
        """ 
        creates bottom leaves level + calls _calculate_next_level() to create levels for merkle tree
        """
        self.complete = False
        self.levels = []
        if self.leaves_count() > 0:  # if there are leaves
            self.levels.insert(0, self.leaves)
            while len(self.levels[0]) > 1:  # until root node reached
                self.next_level_nodes()
        self.complete = True

    def get_merkle_root(self):
        """ 
        gets hashed root
        """
        if self.complete:
            if self.levels is not None:
                return self.convert_to_hex(self.levels[0][0])
            else:
                return None
        else:
            return None

    def get_proof(self, index):
        """
        Generates the proof trail in a bottom-up fashion
        """
        if self.levels is None:
            return None

        # if merkle tree not complete or incorrect index
        elif not self.complete or index > len(self.leaves)-1 or index < 0:
            return None
        else:
            proof_result = []
            no_of_levels = len(self.levels)
            for x in range(no_of_levels - 1, 0, -1):
                level_nodes = len(self.levels[x])

                # skip if this is an odd end node
                if (index == level_nodes - 1) and (level_nodes % 2 == 1):
                    index = int(index / 2.)

                # if mod 2 = 0 , an even index , hashed with right sibling else with left
                # checks if the merkle_node is the left sibling or the right sibling
                Right_node = index % 2
                if Right_node:
                    sibIndex = index - 1
                    sibPos = "left"
                else:
                    sibIndex = index + 1
                    sibPos = "right"

                sibVal = self.convert_to_hex(
                    self.levels[x][sibIndex])
                proof_result.append({sibPos: sibVal})
                # current node gets adjusted as we go up the merkle tree
                index = int(index / 2.)
            return proof_result

    def verify_proof(self, proof_trail, given_leaf, merkle_root):
        """
        Performs the audit-proof from the audit_trail received from the trusted server.
        """
        merkle_root = bytearray.fromhex(merkle_root)
        given_leaf = bytearray.fromhex(given_leaf)  # index leaf given
        if len(proof_trail) == 0:
            return given_leaf == merkle_root
        else:
            proof_hash = given_leaf

            for p in proof_trail:
                # the order of hash concatenation depends on whether the node is a left child or right child of its parent
                try:
                    # the child is a left node
                    proof_till_now = bytearray.fromhex(p['left'])
                    proof_hash = self.hash_function(
                        proof_till_now + proof_hash).digest()
                except:
                    # the child is a right node
                    proof_till_now = bytearray.fromhex(p['right'])
                    proof_hash = self.hash_function(
                        proof_hash + proof_till_now).digest()
             # verifying the computed root hash against the actual root hash
            return proof_hash == merkle_root
