#!/usr/bin/python3
from os import execv
from sys import argv

str = "Rainbow Shapes"
str2 = "Created by T3CHNOLOG1C"
str3 = "Welcome to Rainbow Shape Selector!"
str4 = "Choose a Shape:"
print (str.center(50, '-'))
print (str2.center(50, '-'))
print()
print()
print (str3.center(50, '-'))
print()
print (str4.center(50, '-'))
menu = {}
menu['1']="Square"
menu['2']="Triangle"
menu['3']="Circle"
menu['4']="Star"
menu['5']="Exit"
while True:
	options=menu.keys()
	for entry in options:
			print(entry, menu[entry])
			
	selection=input("Select an Option:")
	if selection =='1':
			execv("./rainbowsquare.py", argv)
	elif selection =='2':
			execv("./rainbowtriangle.py", argv)
	elif selection =='3':
			execv("./rainbowcircle.py", argv)
	elif selection =='4':
			execv("./rainbowstar.py", argv)
	elif selection =='5':
			break
	else:
			print()
			print ("Unknown Option Selected! Please input a valid option.")
			print()
