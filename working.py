import os

# Open the file for reading.

## Build the file filepath
filename = os.path.join('data', '03_Prod.mdout')

# Open the file
f = open(filename,'r')

# Read the data in the file.
data = f.readlines()

# Close the file.
f.close()

# Open a file for writing
f_write = open('Etot.txt', 'w+')

# Loop through the lines
for line in data:
    split_line = line.split()
    if 'Etot' in line:
        print(split_line[2])
        f_write.write(F'{split_line[2]}\n')

f_write.close()
