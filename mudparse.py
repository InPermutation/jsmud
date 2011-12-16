from flask import session

CONFUSED = u"Not sure what you meant."

def interpret(line):
    tmp = line.lower().split()
    command = tmp[0]
    args = tmp[1:]
    if command == "help":
        return helpverb(args)
    if command in ('move', 'go'):
        return move(args[0])

    return CONFUSED

def helpverb(expr):
    return "MOVE or GO: NORTH, EAST, SOUTH, WEST (UP, RIGHT, DOWN, LEFT)"

def move(direction):
    x, y = [int(loc) for loc in session['room'].split('_')]
    if direction in ("left", "west"):
        x -= 1
    elif direction in ("right", "east"):
        x += 1
    elif direction in ("up", "north"):
        y += 1
    elif direction in ("down", "south"):
        y -= 1
    else:
        return CONFUSED

    session['room'] = str(x) + "_" + str(y)
    return "You are in room " + session['room']
