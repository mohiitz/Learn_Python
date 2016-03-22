def myname (*args):
	arg1,arg2 = args
	print "My name is %r and my surname is %r\n so my full name is %s %s" %(arg1,arg2,arg1,arg2)

def myname1(arg1,arg2):
	print "%r %r" %(arg1,arg2)
	
myname("Mohit","Nohwar")
myname1("Mohit","Nohwar")
