from sys import argv

scriptName, filename = argv #enter file name in shell

text = open(filename) #open the file entered and save it in variable "text"

print "Here's your file %r:" % filename
print text.read() #readinf the content and printing it from "text"

print "Type the filename again:"
file_again = raw_input()
text_again = open(file_again)

print text_again.read()
print"""
get the file name either through raw_input or thru argv
open the file and assign it some "variable name""
read the "variable name" and print it
"""