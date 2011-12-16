import cmd
from flask import session

CONFUSED = u"Not sure what you meant."

def interpret(scmd):
	scmd = scmd.lower()
	parts = scmd.split()
	if parts[0] == "help":
		return helpverb(parts[1:])
	if parts[0] == "move" or parts[0] == "go":
		return move(parts[1])
	
	return CONFUSED

def helpverb(expr):
	return "MOVE or GO: NORTH, EAST, SOUTH, WEST (UP, RIGHT, DOWN, LEFT)"

def move(sdir):
	loc = str.split(session['room'], '_')
	x = int(loc[0])
	y = int(loc[1])
	if sdir in ("left", "west"):
		x -= 1
	elif sdir in ("right", "east"):
		x += 1
	elif sdir in ("up", "north"):
		y += 1
	elif sdir in ("down", "south"):
		y -= 1
	else:
		return CONFUSED

	session['room'] = str(x) + "_" + str(y)
	return "You are in room " + session['room']
