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

	def start(self):
		self.distanceCourant=0

	def stop(self):
		if self.distanceCourant>= self.distance:
			self.robot.changerVitesseRoue(0, "LEFT")
			self.robot.changerVitesseRoue(0, "RIGHT")
			return True
		return False


class StrategyTourneGauche:
	def __init__(self, robot):
		self.robot= robot
		self.angleCourant=0
		self.angle=90

	def run(self, fps):
		rayonRoue= self.robot.rayonRoue
		rayonRobot= self.robot.rayonRobot
		vitesse_tourne= 10
		self.robot.changerVitesseRoue(vitesse_tourne, "RIGHT")
		# Calcule de l'angle du Robot
		self.angleCourant+= (rayonRoue*vitesse_tourne*1.0)/(fps*rayonRobot)

	def start(self):
		self.angleCourant=0

	def stop(self):
		print(self.angleCourant)
		if self.angleCourant>= self.angle:
			self.robot.changerVitesseRoue(0, "RIGHT")
			return True
		return False
