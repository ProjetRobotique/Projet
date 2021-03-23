from robot import Robot
from math import pi as PI
import time
from strategy import StrategyTourneGauche, StrategyAvance

class Controler:
	def __init__(self, robot):
		self.exit=False
		self.robot= robot
		self.enMarche= False
		self.tab=[0 for i in range(7)]
		self.actionCourant=-1
		self.s_turnLeft= StrategyTourneGauche(self.robot)

	def boucle(self,fps):
		while True:
			if self.exit:
				break
			self.update(fps)
			time.sleep(1./fps)

	def update(self, fps):
		action=-1
		for i in range(len(self.tab)):
			if self.tab[i]==1:
				action=i
				break
		if action==-1:
			return
		print(self.tab)
		if action==0:
			self.arret()
			self.tab[action]=0
		elif action==1:
			self.tourneRobot10()
			self.tab[action]=0
		elif action==2:
			self.tourneRobot_10()
			self.tab[action]=0
		elif action==3:
			self.augmenterVitesseRobot()
			self.tab[action]=0
		elif action==4:
			self.diminuerVitesseRobot()
			self.tab[action]=0
		elif action==5:
			if not self.s_turnLeft.stop():
				self.s_turnLeft.run(fps)
			else: self.tab[action]=0

	def signal(self, intention):
		print("Signal recu: "+ intention)
		indice=-1
		if intention=="arret":
			indice=0
		elif intention=="tourneRobot10":
			indice=1
		elif intention=="tourneRobot_10":
			indice=2
		elif intention=="augmenterVitesseRobot":
			indice=3
		elif intention=="diminuerVitesseRobot":
			indice=4
		elif intention=="tournerGauche":
			indice=5
			self.s_turnLeft.start()


		if indice==-1:
			print("Controler: Erreur indice=-1")
		elif self.tab[indice]==0:
			self.tab[indice]=1

	def arret(self):
		self.robot.changerVitesseRoue(0, "LEFT")
		self.robot.changerVitesseRoue(0, "RIGHT")

	def augmenterVitesseRobot(self):
		self.robot.changerVitesseSimple(1)
		
	def diminuerVitesseRobot(self):
		self.robot.changerVitesseSimple(-1)

	def tourneRobot(self):
		self.robot.changerAngle(PI/2)

	def tourneRobot10(self):
		self.robot.changerAngle(PI/9)
	
	def tourneRobot_10(self):
		self.robot.changerAngle(-PI/9)

	def tracerCarre(self):
		return

	def speedUp(self):
		self.robot.changerVitesseRoue(1, "LEFT")
		self.robot.changerVitesseRoue(1, "RIGHT")

	def turnLeft(self):
		self.robot.changerVitesseRoue(1, "RIGHT")

	def turnRight(self):
		self.robot.changerVitesseRoue(1, "LEFT")
