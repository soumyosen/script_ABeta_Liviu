import numpy as np

first = 0
last = 99
filenames = []

for i in range(0,(last+1)):
    for j in range(10):
        filenames.append("%s.%s.complex_LSP.pdb" % (i, j))


print(filenames)

with open('combine_all.pdb', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
