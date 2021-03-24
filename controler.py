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
			self.speedUp()
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
		elif intention=="demarrer":
			indice=1
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

	def speedUp(self):
		self.robot.changerVitesseRoue(1, "LEFT")
		self.robot.changerVitesseRoue(1, "RIGHT")

	def turnLeft(self):
		self.robot.changerVitesseRoue(1, "RIGHT")

	def turnRight(self):
		self.robot.changerVitesseRoue(1, "LEFT")
