from sys import argv
scriptName,input_file = argv
def content_file(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def rewind2(f):
	f.seek(7)
	
def line_print(counter,f):
	print "%dst line is " %counter 
	print f.readline()
	counter+=1
	print "%dnd line is " %counter
	counter+=1
	print f.readline()
	print "%drd line is " %counter 
	print f.readline()
	
	
current_file=open(input_file)
print "Lets print the content"
content_file(current_file)
print"Lets rewind now"
rewind(current_file)
print"Now the curser is back to beginning"
counter=1
line_print(counter,current_file)
rewind2(current_file)
cunter=1
line_print(counter,current_file)



