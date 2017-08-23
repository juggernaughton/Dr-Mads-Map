from sys import exit
from random import randint

class Scene(object):
	print "This class is not configured yey. Implement as subclass."
	exit(1)

class MainRoom(Scene):
	def enter(self):
		print "You are in the main room"

class Multiplication(Scene):
	def enter(self):
		print "You are in the Multiplication Room."
	
class Division(Scene):
	
	def enter(self):
		print "You are in the Division Room."
	
class Addition(Scene):
	
	def enter(self):
		print "You are in the Addition Room."

class Engine(Scene):
	
	scenes = {
		"main_room": MainRoom(),
		"multiplication": Multiplication(),
		"division": Division(),
		"addition": Addition()
	}

	def __init__(self, start_scene):
		self.first_scene = start_scene
		print self.first_scene

 	def play(self):
 		current_scene = self.first_scene

	
startgame = Engine('main_room').play()
#print startgame
