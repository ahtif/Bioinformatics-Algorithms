import itertools
import dmatrix
from tree import Node, Leaf

"""
Compute one iteration of the NJA for a given matrix. Return a new node where the 
left and right children are the optimal i,j that minimise step 2 of the algorithm.
The input matrix is also recalculated according to step 3. 
"""
def nja(matrix):
    #Compute all unique keys in the matrix
    keys = set()
    for pair in matrix.keys():
        for elem in pair:
            keys.add(elem)

    #For all keys i, caluclate its r(i) according to step 1 of the NJA
    keysum = dict()
    for i in keys:
        total = sum([v for (a, b), v in matrix.items() if i == a])
        keysum[i] = total

    #For a given pair i,j calculate the value given by step 2 of the NJA
    def Q(i,j):
        m = matrix[(i,j)]
        sumi = keysum[i]
        sumj = keysum[j]

        return m - ((sumi + sumj)/len(keysum)-2)

    #Compute a dictionary which contains value of the formula given by step 2 for 
    #all possible i,j pairs
    Qmatrix = dict()
    for i,j in itertools.permutations(keys, 2):
        Qmatrix[(i,j)] = Q(i,j)

    #Find the minimum i,j pair by sorting the dictionary by its values
    minpair = sorted(Qmatrix.items(), key=lambda x:x[1])[0][0]
    i,j = minpair


    #Create a new node for the PT, with i and j as leaves
    inode = Leaf(str(i))
    jnode = Leaf(str(j))
    node = Node(inode, jnode)

    #Calculate the distance to i and j from the new node.
    def Q1(i,j, right=False):
        m = matrix[(i,j)]
        sumi = keysum[i]
        sumj = keysum[j]

        if right:
            return (m + ((sumj - sumi)/len(keysum)-2.0))/2
        else:
            return (m + ((sumi - sumj)/len(keysum)-2.0))/2

    #Add the distances to the node object,
    node.dleft = Q1(i,j)
    node.dright = Q1(i,j,True)

    #Calculate the distances from all other nodes to the new node and add them to the
    #matrix
    matrix[(minpair,minpair)] = 0
    for k in keys:
        if k != i or k != j:
            ij = matrix[(i,j)]
            ik = matrix[(i,k)]
            jk = matrix[(j,k)]
            matrix[(minpair, k)] = (ik + jk - ij)/2
            matrix[(k,minpair)] = (ik + jk - ij)/2
            
    #Delete all values from the old i and j keys from the matrix
    todel = [pair for pair in matrix.keys() if i in pair or j in pair]
    for key in todel:
        del matrix[key]

    return node

"""
Print a representation of a PT. For each node in the tree, print a representation of 
the left and right nodes and their distances. Since the left and right children of the
tree are always leaf nodes, this makes it possible to print out the tree in the order
it was created in and shows us which nodes are merged at each step in the NJA.
"""
def printTree(node):
    if node != None and not node.visited:
        print ("[{},{}]".format(node.left, node.right))
        print("Distance to {} is: {}\nDistance to {} is: {}".format(node.left, node.dleft, node.right, node.dright))
        node.visited = True
        printTree(node.other)

"""
Given the distance matrix defined in task 3, caluclate the the Phylogenetic Tree and
print the intermediate distance matrices
"""
def task3(m=dmatrix.matrix):
    print("Original Distance Matrix:\n", m, "\n\n")
    #Keep root as a reference to the first node created
    root = nja(m)
    newroot = root
    keys = set()
    for pair in m.keys():
        for elem in pair:
            keys.add(elem)
    n = len(keys)
    print ("n is ", n)
    print (m, "\n")
    while (n > 2):
        node = nja(m)
        keys = set()
        for pair in m.keys():
            for elem in pair:
                keys.add(elem)
        n = len(keys)
        print ("n is ", n)
        print (m, "\n")
        newroot.other = node
        newroot = node

    print("Printing the Phylogenetic Tree:\n")
    printTree(root)    

if __name__ == "__main__":
    task3()
