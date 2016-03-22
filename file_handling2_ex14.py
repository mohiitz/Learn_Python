from sys import argv
scriptName = argv
filename = raw_input("enter file name: ")
file_data = open(filename,'w')
# print file_data.read()
# print file_data.read()
# print file_data.readline()
file_data.write("chaudhary")
print "file %r has been overwritten." %filename
