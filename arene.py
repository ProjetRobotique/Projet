# coding: utf-8
from robot import *
import math
import time

TAILLE_ARENE_X=25
TAILLE_ARENE_Y=25

class Arene:
	def __init__(self, robot):
		self.exit= False

		# matrice à deux dimensions
		self.tableau = []
		for i in range(TAILLE_ARENE_X):
		    self.tableau.append([0] * TAILLE_ARENE_Y)
		
		# Ajout du Robot dans l'Arène
		self.robot= robot
		self.robot.pos = [10.0,10.0]
		self.angle=0
		pos= self.robot.pos
		self.tableau[int(pos[0])][int(pos[1])]=2 #conversion des floats en entier
	
	def avancerRobot(self):
		x= self.robot.pos[0]
		y= self.robot.pos[1]
		self.tableau[int(x)][int(y)]=0 #conversion des floats en entier
		self.robot.seDeplacer(1,0)
		newpos= self.robot.pos
		if (newpos[0]<0 or newpos[0]>=TAILLE_ARENE_X or newpos[1]<0 or newpos[1]>=TAILLE_ARENE_Y):
			self.robot.pos= [x,y]
		pos= self.robot.pos
		if self.tableau[int(pos[0])][int(pos[1])]==1:
			print("Le robot est sur la même case qu'un obstacle")
		self.tableau[int(pos[0])][int(pos[1])]=2 #conversion des floats en entier

	def boucle(self,fps):
		while True:
			if self.exit:
				break
			self.updateArene(fps)
			time.sleep(1./fps)

	def updateArene(self,fps):
		tab = self.robot.vitesse_roue
		rayonRoue= self.robot.rayonRoue
		rayonRobot= self.robot.rayonRobot
		x=self.robot.pos[0]
		y=self.robot.pos[1]

		vitesse_avance= min(tab[0], tab[1])
		vitesse_tourne= tab[1]-tab[0]

		# Calcule de la position du Robot 
		distance= (math.pi*vitesse_avance*rayonRoue)/(180.0*fps)
		x+= distance*math.cos(self.angle*math.pi/180.0)
		y+= distance*math.sin(self.angle*math.pi/180.0)

		# Calcule de l'angle du Robot
		self.angle= (self.angle+((rayonRoue*vitesse_tourne*1.0)/(fps*rayonRobot)))%360
		self.robot.angle= self.angle

		# On vérifie si le robot sort du tableau en abscisse
		if x>=TAILLE_ARENE_X:
			x= TAILLE_ARENE_X-1
		elif self.robot.pos[0]<0:
			x=0
		# On vérifie si le robot sort du tableau en ordonnée
		if y>=TAILLE_ARENE_Y:
			y= TAILLE_ARENE_Y-1
		elif y<0:
			y=0
		# On vérifie s'il y a un obstacle
		if self.tableau[int(x)][int(y)]!=1:
			self.tableau[int(self.robot.pos[0])][int(self.robot.pos[1])]=0
			self.tableau[int(x)][int(y)]=2
			self.robot.pos= [x,y]


