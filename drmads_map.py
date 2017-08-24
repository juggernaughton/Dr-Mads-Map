from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		print "This class is not configured yet. Implement as subclass. Ya know?"
		exit(1)

class MainRoom(Scene):
	def enter(self):
		print "You are in the main room"
		print "You have two choices: 'stay' in the main room, or... 'run' to your left.\n"
		action = raw_input("> ")
		
		if action == 'stay':
			print "You chose to stay in the main room like a little bitch!"
			return 'main_room'
		elif action == 'run':
			print "You chose to run like the little bitch you are."
			return 'multiplication'
		else:
			print "\nYou suck at this bruh.\n"
			exit(1)
			
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
		print "Engine __init__ has start_scene", start_scene
		print "\n\n"
	
 	def play(self):
 		current_scene = Engine.scenes.get(self.first_scene)
 		print "current_scene is: ", current_scene

 		
 		while True:
 			print "\n\t\t-----------------"
 			next_scene_name = current_scene.enter()
 			print "This is the current scene: ", next_scene_name
 			current_scene = Engine.scenes.get(next_scene_name)
  			print "This is the next scene: ", current_scene
	
startengine = Engine('main_room')

startengine.play()
 

#print startgame
