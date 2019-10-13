# Python 3 code to print MAC 
# in formatted way and easier 
# to understand 

import re, uuid 
from os import path
# joins elements of getnode() after each 2 digits. 
# using regex expression 
f = open('macAdd.txt', 'w')
print ("The MAC address successfully written to file... ", end="") 
print (':'.join(re.findall('..', '%012x' % uuid.getnode())), file=f) 
