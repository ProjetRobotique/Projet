# coding: utf-8
from tkinter import *
from robot import *
from math import pi as PI

TAILLE_ARENE_X = 25
TAILLE_ARENE_Y = 25
class Arene:
	def __init__(self, control, robot):
		self.exit= False
		
		# Controle du Robot
		self.control= control
		
		# matrice à deux dimensions
		self.tableau = []
		for i in range(TAILLE_ARENE_X):
		    self.tableau.append([0] * TAILLE_ARENE_Y)
		
		# Ajout du Robot dans l'Arène
		self.robot= robot
		self.robot.pos = [10.0,10.0]
		pos= self.robot.pos
		self.tableau[int(pos[0])][int(pos[1])] = 2 #conversion des floats en entier
	
	def avancerRobot(self):
		x= self.robot.pos[0]
		y= self.robot.pos[1]
		self.tableau[int(x)][int(y)] = 0 #conversion des floats en entier
		self.robot.seDeplacer(1,0)
		newpos= self.robot.pos
		if (newpos[0]<0 or newpos[0]>=TAILLE_ARENE_X or newpos[1]<0 or newpos[1]>=TAILLE_ARENE_Y):
			self.robot.pos = [x,y]
		pos= self.robot.pos
		if self.tableau[int(pos[0])][int(pos[1])]==1:
			print("Le robot est sur la même case qu'un obstacle")
		self.tableau[int(pos[0])][int(pos[1])]=2 #conversion des floats en entier
	
	def boucle(self,fps):
		while True:
			if self.exit:
				break
			if self.control.enMarche:
				self.avancerRobot()
			self.updateArene()
			time.sleep(1./fps)

	def updateArene(self):
		x= self.robot.pos[0]
		y= self.robot.pos[1]
		self.tableau[int(x)][int(y)]=0 #conversion des floats en entier
		if self.tableau[int(x)][int(y)]==1:
			print("Le robot est sur la même case qu'un obstacle")
		self.tableau[int(x)][int(y)]=2

