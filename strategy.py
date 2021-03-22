from robot import Robot
import math

class StrategyAvance:
	def __init__(self, robot):
		self.robot= robot
		self.distance=10
		self.distanceCourant=0

	def run(self, fps):
		rayonRoue= self.robot.rayonRoue
		self.robot.changerVitesseRoue(1, "LEFT")
		self.robot.changerVitesseRoue(1, "RIGHT")
		self.distanceCourant+=(math.pi*vitesse_avance*rayonRoue)/(180.0*fps)
		if self.stop():
			self.robot.changerVitesseRoue(0, "LEFT")
			self.robot.changerVitesseRoue(0, "RIGHT")

	def start(self):
		self.distanceCourant=0

	def stop(self):
		if self.distanceCourant>= self.distance:
			return True
		return False


class StrategyTourneGauche:
	def __init__(self, robot):
		self.robot= robot
		self.angle=0
		self.angleCourant=90

	def run(self, fps):
		rayonRoue= self.robot.rayonRoue
		rayonRobot= self.robot.rayonRobot
		vitesse_tourne= 1
		self.robot.changerVitesseRoue(1, "RIGHT")
		# Calcule de l'angle du Robot
		self.angleCourant= (self.angleCourant+((rayonRoue*vitesse_tourne*1.0)/(fps*rayonRobot)))%360
		if self.stop():
			self.robot.changerVitesseRoue(0, "RIGHT")

	def start(self):
		self.angleCourant=0

	def stop(self):
		if self.angleCourant>= self.angle:
			return True
		return False
