# coding: utf-8
from .robots import Robot, Robot_Proxy
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
		self.ts=time.time()
	

	def boucle(self,fps):
		while True:
			if self.exit:
				break
			self.updateArene(fps)
			time.sleep(1./fps)

	def updateArene(self,fps):
		self.robot.map= self.tableau
		tab = self.robot.vitesse_roue
		rayonRoue= Robot.WHEEL_DIAMETER*0.5
		rayonRobot= Robot.WHEEL_BASE_WIDTH
		x=self.robot.pos[0]
		y=self.robot.pos[1]

		vitesse_avance= min(tab[0], tab[1])
		vitesse_tourne= tab[1]-tab[0]

		# Calcule de la position du Robot 
		distance= (math.pi*vitesse_avance*rayonRoue*(self.ts-time.time()))/(180.0*fps)
		x+= distance*math.cos(self.angle*math.pi/180.0)
		y+= distance*math.sin(self.angle*math.pi/180.0)


		# Calcule de l'angle du Robot
		self.angle= (self.angle+((rayonRoue*vitesse_tourne*1.0*(time.time()-self.ts))/(rayonRobot)))%360
		self.robot.angle= self.angle
		self.ts=time.time()

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
		if self.tableau[int(y)][int(x)]!=1:
			self.tableau[int(self.robot.pos[1])][int(self.robot.pos[0])]=0
			self.tableau[int(y)][int(x)]=2
			self.robot.pos= [x,y]

