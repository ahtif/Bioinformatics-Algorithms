"""
Comments on generated trees:
TP53: Seems pretty consistent for know evolutionary relationships. The most unusual
one seems to be that cows are more closely related to dolphins and not closer to all
the other land mammals in the tree.

IL6: The generated trees seems mainly consistant with known evolutionary relationships

APOE: Seems somewhat consistant with known evolutionary relationships but it seems
a bit odd that the ferret, a bird, has a closer ancestor to humans, gibbons and 
orangutans than the other mammals in the tree (sheep, microbat, etc.)
"""


import itertools
import nwa
import nja
import os
from tree import Node, Leaf
from Bio import SeqIO

"""
Given a list of sequences, return a distance matrix based on the alignment scores
of each possible pair of sequences.
"""
def computeMatrix(seqs, lookup):
    #Initialise the matrix with 0 where appropriate
    matrix = dict()
    #print (*itertools.combinations(seqs,2))
    for seq in seqs:
        name = lookup[seq]
        matrix[name,name] = 0
    #print (matrix)

    #For all possible pairs of sequences, compute their NW alignment scores,
    #calculate the distance from the score and add to the distance matrix
    #NOTE: The sequences in the distance matrix are replaced by their corresponding
    #animal names for easier readability 
    for x,y in itertools.combinations(seqs,2):
        table = nwa.NWTable(x,y)
        score = list(table.items())[-1][1]
     #   print("table for pair: ", (x,y), "score: ", score)
     #   nwa.printTable(x,y,table, [])
        align1, _, _ = nwa.alignment(x, y, table)
        distance = (len(align1)-score)/len(align1)
        name1 = lookup[x]
        name2 = lookup[y]
        matrix[name1,name2] = distance
        matrix[name2,name1] = distance
    
    return matrix
    
"""
Same as task3() in nja.py
"""
def genTree(m):
    root = nja.nja(m)
    newroot = root
    keys = set()
    for pair in m.keys():
        for elem in pair:
            keys.add(elem)
    n = len(keys)
    print ("n is ", n)
    print (m, "\n")
    while (n > 1):
        node = nja.nja(m)
        keys = set()
        for pair in m.keys():
            for elem in pair:
                keys.add(elem)
        n = len(keys)
        print ("n is ", n)
        print (m, "\n")
        newroot.other = node
        newroot = node

    return root


"""
Read a folder containing fasta files, return a list of all the raw sequence data and 
a lookup dictionary to get the id of the gene from its sequence
"""
def readFolder(name):
    seqs = []
    lookup = dict()
    for f in os.listdir("genes/"+name):
        if f.endswith(".fa"):
            print (f)
            seq = SeqIO.read(os.path.join("genes",name,f), "fasta")
            seqStr = str(seq.seq)
            seqs.append(seqStr)
            lookup[seqStr] = seq.id
    return seqs, lookup

"""
For each gene, compute the first two steps of the CLUSTALW algorithm and print out a
representation of the PT generated.
"""
def task5():
    for name in ["tp53", "il6", "apoe"]:
        bio_seqs, lookup = readFolder(name)
        print ("\n\nGENE : {}\n\n".format(name))
        m = computeMatrix(bio_seqs, lookup)
        print("Original Distance matrix:\n", m)
        
        root = genTree(m)

        print("Printing the Phylogenetic Tree for gene: ", name)
        nja.printTree(root)
        print()

if __name__ == "__main__":
    task5()
