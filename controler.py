# coding: utf-8
from robot import Robot
from math import pi as PI
import time
from strategy import StrategyTourneGauche, StrategyAvance, StrategySequence

class Controler(object):
	def __init__(self, robot):
		self.exit=False
		self.robot= robot
		self.tab=[0 for i in range(7)]
		self.actionCourant=-1
		self.s_turnLeft= StrategyTourneGauche(self.robot, 90, 0)
		self.s_turnRight= StrategyTourneGauche(self.robot, 90, 1)
		self.s_forward= StrategyAvance(self.robot, 70)
		carre= [self.s_forward, self.s_turnLeft, self.s_forward, self.s_turnLeft, self.s_forward, self.s_turnLeft, self.s_forward]
		self.s_carre= StrategySequence(self.robot, carre)
		
		self.s_angleTriangle = StrategyTourneGauche(self.robot,60,0)
		triangleEqui = [self.s_forward, self.s_angleTriangle, self.s_forward, self.s_angleTriangle, self.s_forward, self.s_angleTriangle]
                self.s_triangleEqui = StrategySequence(self.robot, triangleEqui)

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
		# s'arrêter
		if action==0:
			self.robot.stop()
			self.tab[action]=0
		# Avancer
		elif action==1:
			if not self.s_forward.stop():
				if self.s_forward.run()==1:  self.tab[action]=0
			else: self.tab[action]=0
		# tracer un carre
		elif action==4:
			if not self.s_carre.stop():
				self.s_carre.run()
			else: self.tab[action]=0
		# Tourner Gauche
		elif action==5:
			if not self.s_turnLeft.stop():
				self.s_turnLeft.run()
			else: self.tab[action]=0
		# Tourner Droite
		elif action==3:
			if not self.s_turnRight.stop():
				self.s_turnRight.run()
			else: self.tab[action]=0

	def up(self):
                self.robot.up()

	def signal(self, intention):
		print("Signal recu: "+ intention)
		indice=-1
		if intention=="arret":
			indice=0
		elif intention=="avancer":
			indice=1
			self.s_forward.start()
		elif intention=="tracerCarre":
			indice=4
			self.s_carre.start()
		elif intention=="tournerGauche":
			indice=5
			self.s_turnLeft.start()
		elif intention=="tournerDroite":
			indice=3
			self.s_turnRight.start()

		if indice==-1:
			print("Controler: Erreur indice=-1")
		elif self.tab[indice]==0:
			self.tab[indice]=1

	def down(self):
                self.robot.down()

