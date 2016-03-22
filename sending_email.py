from sys import argv
from os.path import exists

scriptName, from_file, To_file = argv

in_file = open(from_file)
in_data = in_file.read()

out_file = open(To_file,'w')
out_file.write(in_data)