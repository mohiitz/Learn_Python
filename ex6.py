x = "There are %d types of people" % 10
binary = "binary"
do_not="don't"
y="those who know %s and those who know %s." % (binary,do_not)

print x
print y

print "i said %r." %x
print "i also said %s." % y

hilarous= False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarous

w=" this is the left side of.."
e= "a string with a right side"

print w+e
import datetime
print " today's date is %s" % datetime.date.today()