from robot import Robot
from math import pi as PI
import time

class Controler:
	def __init__(self, robot):
		self.exit=False
		self.robot= robot
		self.enMarche= False
		self.tab=[0,0,0,0,0,0,0]

	def boucle(self,fps):
		while True:
			if self.exit:
				break
			self.update()
			time.sleep(1./fps)

	def update(self):
		action=-1
		for i in range(len(self.tab)):
			if self.tab[i]==1:
				action=i
				break
		if action==-1:
			return

		if action==0:
			self.demarrer()
			self.tab[action]=0
		elif action==1:
			self.arret()
			self.tab[action]=0
		elif action==2:
			self.tourneRobot10()
			self.tab[action]=0
		elif action==3:
			self.tourneRobot_10()
			self.tab[action]=0
		elif action==4:
			self.augmenterVitesseRobot()
			self.tab[action]=0
		elif action==5:
			self.diminuerVitesseRobot()
			self.tab[action]=0

	def signal(self, intention):
		print("Signal recu: "+ intention)
		indice=-1
		if intention=="demarrer":
			indice=0
		elif intention=="arret":
			indice=1
		elif intention=="tourneRobot10":
			indice=2
		elif intention=="tourneRobot_10":
			indice=3
		elif intention=="augmenterVitesseRobot":
			indice=4
		elif intention=="diminuerVitesseRobot":
			indice=5

		if indice==-1:
			print("Controler: Erreur indice=-1")
		elif self.tab[indice]==0:
			self.tab[indice]=1

	def demarrer(self):
		self.enMarche= True

	def arret(self):
		self.enMarche= False

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
