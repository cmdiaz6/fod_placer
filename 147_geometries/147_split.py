#!/usr/bin/env python

with open('147_molecules') as f1:
  #loop 147 atoms
  for i in range(147):

    #read # of atoms
    num=f1.readline()

    #read atom name. strip newline, replace spaces.
    name=f1.readline().strip().replace(" ","_")

    print('creating file',int(num),name,i)

    #open new file
    filename = name + '.xyz'

    with open(filename,'w') as f2:
        # write # of atoms
        f2.write(num)
        # write atom name
        f2.write(name)
        f2.write("\n")
        #loop: read atom x y z
        for i in range(int(num)):
            line=f1.readline()
            f2.write(line)

