from sys import exit
from random import randint

class Scene(object):
	print "This class is not configured yet. Implement as subclass."
	exit(1)

class MainRoom(Scene):
	def enter(self):
		print "You are in the main room"
		return 'main_room'

class Multiplication(Scene):
	def enter(self):
		print "You are in the Multiplication Room."
	
class Division(Scene):
	
	def enter(self):
		print "You are in the Division Room."
	
class Addition(Scene):
	
	def enter(self):
		print "You are in the Addition Room."

class Engine(object):
	
	scenes = {
		"main_room": MainRoom(),
		"multiplication": Multiplication(),
		"division": Division(),
		"addition": Addition()
	}

	def __init__(self, start_scene):
		self.first_scene = start_scene
		print "The first scene is %s ", self.first_scene
	
	def get_scene_name(self, scene_name):
		scene_name = Engine.scenes.get(self.first_scene)
	
 	def play(self):
 		current_scene = self.first_scene.get_scene_name()
 		
 		while True:
 			print "\n\t\t-----------------"
 			next_scene_name = current_scene.enter()
 			current_scene = self.first_scene.get_scene_name(next_scene_name) 

	
startengine = Engine('main_room')

print "startengine has %s from Engine", startengine
print self.first_scene
startengine.play()
 

#print startgame
