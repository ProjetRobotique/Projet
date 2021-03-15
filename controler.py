from robot import Robot
from math import pi as PI

class Controler:
	def __init__(self, robot):
		self.robot = robot
		self.enMarche = False

	def boucle(self,fps):
		while True:
			if self.exit:
				break
			self.update()
			time.sleep(1./fps)

	def update(self):
		self.changeAction()
		if self.action==-1:
			return
		# Execution de 1 commande
		if self.action==0:
			self.robot.seDeplacer(1,0)
		elif self.action==1:
			self.tourneRobot10()
		elif self.action==2:
			self.tourneRobot_10()
		elif self.action==3:
			self.augmenterVitesseRobot()
		elif self.action==4:
			self.diminuerVitesseRobot()
		if self.action!=0:
			self.tab[self.action]=0
			self.action+=1

	def changeAction(self):
		if self.action>=len(self.tab):
			self.action=0
		if self.tab[self.action]!=0:
			return
		self.action=-1
		for i in range(self.action+1,len(self.tab)):
			if self.tab[i]!=0:
				self.action=i
				break
		if self.action==-1:
			for i in range(0,self.action):
				if self.tab[i]!=0:
					self.action=i
					break

	def signal(self, intention):
		if intention=="demarrer":
			self.tab[0]=1
		elif intention=="arreter":
			self.tab[0]=0

		else:
			indice=-1
			if intention=="tourneRobot10":
				indice=1
			elif intention=="tourneRobot_10":
				indice=2
			elif intention=="augmenterVitesseRobot":
				indice=3
			elif intention=="diminuerVitesseRobot":
				indice=4

			if indice==-1:
				print("Controler: Erreur indice=-1")
			elif self.tab[indice]==0:
				self.tab[indice]=1	
	
	def augmenterVitesseRobot(self):
		self.robot.changerVitesseSimple(1)
		
	def diminuerVitesseRobot(self):
		self.robot.changerVitesseSimple(-1)

	def tourneRobot(self):
		self.robot.changerAngle(PI/2)

	def tourneRobot10(self):
		self.robot.changerAngle(PI/18)
	
	def tourneRobot_10(self):
		self.robot.changerAngle(-PI/18)

	def demarrer(self):
		self.enMarche = True

	def arret(self):
		self.enMarche = False
