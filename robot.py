# coding: utf-8

from math import *
class Robot:
   def __init__(self,carte,nom):
      self.id= nom
      self.map = carte #le robot recupere la grille
      self.vitesse = 0.0
      self.pos = [0.0,0.0]
      self.angle = 0
   
   def seDeplacer(self,time,acc):
      self.pos[0] = self.pos[0] + self.vitesse * cos(self.angle) * time
      self.pos[1] = self.pos[1] + self.vitesse * sin(self.angle) * time + 1/2 * acc * time**2
      # Arrondi de la position du robot à 3 chiffre après la virgule
      self.pos[0]= round(self.pos[0], 3)
      self.pos[1]= round(self.pos[1], 3)
    
   def changerVitesse(self,tours_min): #prend en argument le nombre de tours par minutes en plus ou en moins voulus.
      self.vitesse = self.vitesse + (tours_min/60) # * perimetre de la roue (valeur de son rayon à demander)       
      if self.vitesse < 0.0 :
          self.vitesse = 0.0
      #demander la vitesse max du robot.
      
   def changerVitesseSimple(self,vitesse):
      self.vitesse = self.vitesse + vitesse
      if self.vitesse < 0.0 :
          self.vitesse = 0.0
      
   def changerAngle(self,degree):
      self.angle = self.angle + degree

   def placerRobot(self,x, y):
      self.pos[0] = x
      self.pos[1] = y
      
   def mapUpdate(self,NouvelleCarte):
      self.map= NouvelleCarte