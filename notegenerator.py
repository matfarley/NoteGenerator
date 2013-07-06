from random import *

# main class for the note generator.  contains the list of notes and calls the rand_int
# function to print a random index
class NoteGenerator:
    def __init__(self):
        notes = ["G#/Ab","A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", 
        "E", "F", "F#/Gb", "G"]
        index = randint(0,11)
        print "Find this note:"
        print notes[index]
        pause = raw_input("--->")

# introduction spiel
print
print "Welcome to the Random Note Generator"
print "press CTRL-D to exit"
print

# keeps running until Ctrl-D
try:
   while True:
        start = NoteGenerator()
        start
	
except EOFError:
	print "Exit"

	