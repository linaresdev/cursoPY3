#!/usr/bin/python3
#-*- coding: utf-8 -*-

## REPEAT
def str_repeat(inp, rep):

	out = inp

	for row in range(1, rep):
		out += inp

	return out

def str_cover(string='', limit=50, cut=0):
	
	if( (cut != 0) and (cut < limit) ): 
		cut 	= limit - cut
		string 	= string[0:cut]+"..."

	index 	= len(string)
	limit 	= limit - index

	return string+str_repeat(' ', limit)



