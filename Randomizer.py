# This Randomizer was made in conjunction with SoupBot and should be used in accordance
# with SoupBot for expected results. Usage of this script in another environment might
# not complete what you want it to do. Cheers -Cr4_nk

import random, re, sys, unicodedata, time, math, subprocess
#from twisted.internet import reactor
#from twisted.internet import protocol
#from twisted.python import log
#from twisted.words.protocols import irc
#from selenium import webdriver

# Uncomment twisted/selenium imports if intention is to use more code then needed here :33

##################################################################################
############################### Settings #########################################
##################################################################################

Var1 = lambda: random.randint(0,9)
Var2 = lambda: random.randint(0,100)
print ('The following test will check if the Variable Number Generator works')
print (Var2())
print (Var2())
print (Var2())
print (Var2())
print (Var2())
print (Var2())
print (Var2())
print (Var2())

if Var1() == 0:
	print ('Variable is 0')
	subprocess.call("randscript/./0.py", shell=True)
elif Var1() == 1:
	print ('Variable is 1')
	subprocess.call("randscript/./1.py", shell=True)
elif Var1() == 2:
	print ('Variable is 2')
	subprocess.call("randscript/./2.py", shell=True)
elif Var1() == 3:
	print ('Variable is 3')
	subprocess.call("randscript/./3.py", shell=True)
elif Var1() == 4:
	print ('Variable is 4')
	subprocess.call("randscript/./4.py", shell=True)
elif Var1() == 5:
	print ('Variable is 5')
	subprocess.call("randscript/./5.py", shell=True)
elif Var1() == 6:
	print ('Variable is 6')
	subprocess.call("randscript/./6.py", shell=True)
elif Var1() == 7:
	print ('Variable is 7')
	subprocess.call("randscript/./7.py", shell=True)
elif Var1() == 8:
	print ('Variable is 8')
	subprocess.call("randscript/./8.py", shell=True)
elif Var1() == 9:
	print ('Variable is 9')
	subprocess.call("randscript/./9.py", shell=True)
	


