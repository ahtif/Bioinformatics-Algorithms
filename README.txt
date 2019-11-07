Language used: Python 3.6.3 
The python modules used for this assignment are sys, os, itertools, termcolor and Bio.
All of the libraries used are part of the standard python library apart from Bio
which needs to be installed before running task5. 
Additionally all of the work was done on the DCS lab machines with the "module load
cs909-python" command used to create a python 3.6 environment.

TASK1:
Revelant Files: nwa.py, task1.tbl
To run the program simply type "python nwa.py" into the terminal. By default, it will
run the program with two smaller sequences so that the table that is printed out 
to the terminal is easier to read. To run it with the sequences provided in the 
assignment sheet, comment out lines 119 and 120 and uncomment lines 121 and 122.
Running the program with the longer sequences will result in a terminal output that
is quite hard to read, so additionally the program can also additionally output
the NW table and the optimal path to a csv type filename, if a filename is passed
to the program.
This can be done by typing "python nwa.py <filename>" where filename is the name of 
the file you want it to output to. The file "task1.tbl", included in the zip provides
output generated when running the program with the sequences defined in the assignment
sheet.


TASK3:
Relevant Files: tree.py, dmatrix.py, nja.py, Task3-PT.pdf
To run the program just type "python nja.py" into the terminal. The output generated
is: the original distance matrix, all of the intermediate distance matrices and a 
representation of the phylogenetic tree, which is done by printing the 2 elements
of the matrix that were merged at each step, followed by the edge weights to those 
elements.
The final tree generated has also been hand drawn with all the edge weights labelled
and is viewable in the "Task3-PT.pdf" file

TASK4:
The solution to this task has been provided in the file "suffix_tree.pdf"

TASK5:
Revelant Files: All of the files for Task3 with the addition of clustalw.py, Task5.pdf
and the genes folder, with its subfolders apoe, il6, tp53, each of with contain 10 
fasta (.fa) files.
To run the program type "python clustalw.py" into the terminal. The output generated
is the same as for task3, however it is first prefixed by the gene name and all of
files names for the sequences used for that particular gene.
Additionally the generated tree have also been drawn out again and can be accessed in
"Task5.pdf"

