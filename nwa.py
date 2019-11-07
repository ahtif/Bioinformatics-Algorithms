import sys
from collections import OrderedDict
from termcolor import colored

symbols = set(["A", "C", "G", "T"])
MATCH_SCORE = 1
MISMATCH_SCORE = -0.5

"""
The scoring matrix provided in the assignment sheet as a function.
"""
def score(x, y):
    if x == y:
        return MATCH_SCORE
    if x == "-" or y == "-":
        return MISMATCH_SCORE
    return 0

"""
Generate a NW table as an ordered dictionary given two sequences. The alignment score
of the two sequences is just the last item added to the dictionary
"""
def NWTable(s1, s2):
    table = OrderedDict() 

    for i in range(0,len(s1)+1):
        table[(i,0)] = i*MISMATCH_SCORE    

    for j in range(0,len(s2)+1):
        table[(0,j)] = j*MISMATCH_SCORE

    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            match = table[(i-1, j-1)] + score(s1[i-1], s2[j-1])
            delete = table[(i-1, j)] + MISMATCH_SCORE
            insert = table[(i, j-1)] + MISMATCH_SCORE
            table[(i,j)] = max(match, insert, delete)

    return table

"""
Given two sequences and their NW table, calculate an optimal aligment and the path
in the table corresponding to the alignment
"""
def alignment(s1, s2, table):
    align1 = ""
    align2 = ""
    i = len(s1)
    j = len(s2)
    path = []
    while (i > 0 or j > 0):
        if i > 0 and j > 0 and table[(i,j)] == table[(i-1,j-1)] + score(s1[i-1], s2[j-1]):
            align1 = s1[i-1] + align1
            align2 = s2[j-1] + align2
            
            path.append((i,j))
            i -= 1
            j -= 1
        elif i > 0 and table[(i,j)] == table[(i-1, j)] + score(s1[i-1], "-"):
            align1 = s1[i-1] + align1
            align2 = "-" + align2
            path.append((i,j))
            i -= 1
        else:
            align1 = "-" + align1
            align2 = s2[j-1] + align2
            path.append((i,j))
            j -= 1 
    
    return align1, align2, path

"""
Pretty print a representation of the NW table and highlight the path that corresponds
to the optimal alignment.
If a file handle is passed in as the fname parameter, it will instead print to the
given file in a csv type format.
"""
def printTable(s1, s2, table, path, fname=None):
    x, y = list(table.keys())[-1]

    s1 = "E"+s1
    s2 = "E"+s2
    if fname:
        row = [c for c in s1]
        print (" ", *row, sep=",", file=fname)
    else:
        row = [c.ljust(5) for c in s1]
        print (" ", *row, sep="|", end="|\n")
    j = 0
    while j <= y:
        row = [s2[j]]
        i = 0
        while i <= x:
            if fname:
                i
                v = str(table[(i,j)])
            else:
                v = str(table[(i,j)]).ljust(5)
            if (i,j) in path:
                if fname:
                    v = "("+v+")"
                else:
                    v = colored(v, "green")
                row.append(v)
            else:
                row.append(v)
            i+=1
        if fname:
            print (*row, sep=",", file=fname)
        else:
            print (*row, sep="|", end="|\n")
        j+=1

"""
Calculate the alignment score of the two defined sequences, and print their NW, with
the optimal alignment highlighted.
"""
def task1(fname=None):
    s1 = "CATGAG"
    s2 = "CAGAGG"
    #s1 = "CAAAGATCTGAAGAGCCAGTGGACTCCACCCCACTTTCTGGTCTGACCAATT"
    #s2 = "ACCACACTCTCTGGGCTGACCAATTACAGCGCTTCTACAGAACTGAACACTCC"

    table = NWTable(s1, s2)
    print ("Alignment score for {} and {}: {}".format(s1, s2, list(table.items())[-1][1]))
    align1, align2, path = alignment(s1, s2, table)
    print("Optimal alignment:\n{}\n{}".format(align1, align2))

    if fname:
        outfile = open(fname, "w")
        printTable(s1,s2,table,path, outfile)
        print ("\nOptimal Path:\n", path, file=outfile)
        outfile.close()
    else:
        print("NW table: ")
        printTable(s1,s2,table,path)
        
        print("Optimal path:\n",path)

#If a filename is passed to the program, pass it in as a parameter to task1()
if __name__ == "__main__":
    fname = None
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    task1(fname)
