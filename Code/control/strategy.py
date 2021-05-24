# coding: utf-8
import math
import time
from ..robots import Robot
from ..view import balise

class StrategyAvance:
	def __init__(self, robot, distance):
		self.robot= robot
		self.distance= distance
		self.distanceCourant=0
		self.appelTime= 0
	
	def run(self):
		d=self.robot.get_distance()
		if d<3 and d>=0:
			print("Trop près")
			self.robot.stop()
			return 1
		temps= time.time()- self.appelTime
		rayonRoue= self.robot.WHEEL_DIAMETER /2
		self.robot.set_motor_dps(3, 90)
		if self.appelTime!=0:
			self.distanceCourant+=(math.pi*min(self.robot.vitesse_roue[0], self.robot.vitesse_roue[1] *rayonRoue*temps))/(180.0)
		self.appelTime = time.time()
		return 0
	
	def start(self):
		self.distanceCourant=0
		self.appelTime=0


	def stop(self):
		if self.distanceCourant>= self.distance:
			self.robot.stop()
			return True
		return False


class StrategyTourner:
	def __init__(self, robot, angle, direction):
		self.robot= robot
		self.angleCourant=0
		self.angle= angle
		self.direction= direction
		self.appelTime= 0
	
	def run(self):
		temps= time.time()- self.appelTime
		rayonRoue= self.robot.WHEEL_DIAMETER*0.5
		rayonRobot= self.robot.WHEEL_BASE_WIDTH
		vitesse_tourne= 100
		if (self.direction==0):
			self.robot.set_motor_dps(1, vitesse_tourne)
		else: self.robot.set_motor_dps(2, vitesse_tourne)
		# Calcule de l'angle du Robot
		if self.appelTime!=0:
			self.angleCourant+= (rayonRoue*vitesse_tourne*1.0*temps)/rayonRobot
		self.appelTime= time.time()
		self.stop()
		

	def start(self):
		self.angleCourant=0
		self.appelTime=0

	def stop(self):
		if self.angleCourant>= self.angle:
			self.robot.set_motor_dps(3, 0)
			return True
		return False

class StrategySequence:
	def __init__(self, robot, tab):
		self.robot= robot
		self.tab= tab
		self.action=0

	def run(self):
		if self.tab[self.action].stop():
			self.action+=1
			if self.stop(): return
			else: self.tab[self.action].start()
		if self.tab[self.action].run()==1: self.action+=1

	def start(self):
		self.action=0
		self.tab[self.action].start()

	def stop(self):
		return self.action>=len(self.tab)


class StrategyChercherBalise:
	def __init__(self, robot):
		self.robot= robot
		self.appelTime= 0
		self.s_turnLeft= StrategyTourner(self.robot, 30, 0)
		self.fin=False
		self.i=0
		self.turn=False
	
	def run(self):
		if not self.turn:
			val= balise.chercherBalise(self.robot.get_image())
			if val=="balise absent":
				self.turn=True
				self.s_turnLeft.start()
				self.i+=1
			else:
				self.fin=True
		else:
			if not self.s_turnLeft.stop():
				self.s_turnLeft.run()
			else: self.turn=False
		

	def start(self):
		self.fin=False
		self.turn= False
		self.i=0

	def stop(self):
		return self.fin or self.i>12
