#!/usr/bin/env python3

import turtle as t
import random as r
title = 'Rainbow Triangle'
t.title(title)
t.showturtle()
t.colormode(255)
t.speed(5)
t.width(3)
def triangle():
	x = 1
	if x == 1:
		while x == 1:
			t.color(r.randrange(0,255),r.randrange(0,255),r.randrange(0,255))
			t.begin_fill()
			t.forward(150)
			t.left(120)
			t.end_fill()
	elif x == 0:
		print('Failed to loop')
	else:
		print('Fatal Error! Please Reinstall.')
triangle()
