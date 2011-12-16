import cmd
from flask import session

CONFUSED = "Not sure what you meant."

def interpret(scmd):
	scmd = scmd.lower()
	parts = scmd.split()
	if parts[0] == "move" or parts[0] == "go":
		return move(parts[1])
	
	return CONFUSED

def move(sdir):
	loc = str.split(session['room'], '_')
	x = int(loc[0])
	y = int(loc[1])
	if sdir == "left" or sdir == "west":
		x = x - 1
	elif sdir == "right" or sdir == "east":
		x = x + 1
	elif sdir == "up" or sdir == "north":
		y = y + 1
	elif sdir == "down" or sdir == "south":
		y = y - 1
	else:
		return CONFUSED

	session['room'] = str(x) + "_" + str(y)
	return "You are in room " + session['room']
