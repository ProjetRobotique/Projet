# coding: utf-8
from math import pi as PI
import time
from ..robots import Robot
from .strategy import StrategyTourner, StrategyAvance, StrategySequence, StrategyChercherBalise

class Controler(object):
	def __init__(self, robot):
		self.exit=False
		self.robot= robot
		self.tab=[0 for i in range(7)]
		self.actionCourant=-1
		self.s_turnLeft= StrategyTourner(self.robot, 90, 0)
		self.s_turnRight= StrategyTourner(self.robot, 90, 1)
		self.s_forward= StrategyAvance(self.robot, 70)
		carre= [self.s_forward, self.s_turnLeft, self.s_forward, self.s_turnLeft, self.s_forward, self.s_turnLeft, self.s_forward]
		self.s_carre= StrategySequence(self.robot, carre)
		self.s_suivreBalise= StrategySequence(self.robot, [StrategyChercherBalise(self.robot), StrategyAvance(self.robot, 20)])


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
		# s'arrêter
		if action==0:
			self.robot.stop()
			self.tab[action]=0
		# Avancer
		elif action==1:
			if not self.s_forward.stop():
				if self.s_forward.run()==1:  self.tab[action]=0
			else: self.tab[action]=0
		# Suivre Balise
		elif action==2:
			if not self.s_suivreBalise.stop():
				self.s_suivreBalise.run()
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
		elif intention=="balise":
			indice=2
			self.s_suivreBalise.start()

		if indice==-1:
			print("Controler: Erreur indice=-1")
		elif self.tab[indice]==0:
			self.tab[indice]=1
