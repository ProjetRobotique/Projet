# coding: utf-8

from math import *
class Robot:
   rayonRoue  = 117  # distance (mm) de la roue gauche a la roue droite.
   rayonRobot = 66.5 #  diametre de la roue (mm)
   
   def __init__(self,carte,nom):
      self.id= nom
      self.map = carte #le robot recupere la grille
      self.vitesse = 0.0
      self.pos = [0.0,0.0]
      self.angle = 0
      self.vitesse_roue=[0,0] # En degre par seconde
   

   def seDeplacer(self,time,acc):
      self.pos[0] = self.pos[0] + self.vitesse * cos(self.angle)
      self.pos[1] = self.pos[1] + self.vitesse * sin(self.angle)
      # Arrondi de la position du robot à 3 chiffre après la virgule
      self.pos[0]= round(self.pos[0], 3)
      self.pos[1]= round(self.pos[1], 3)
    
   def changerVitesseRoue(self, dps, port): #prend en argument le nombre de tours par minutes en plus ou en moins voulus.
      i=-1
      if port=="LEFT":
         i=0
      elif port=="RIGHT":
         i=1
      else:
         print("Erreur")
         return
      if dps>=0:
         self.vitesse_roue[i]= dps
      
   def changerVitesseSimple(self,vitesse):
      self.vitesse = self.vitesse + vitesse
      if self.vitesse < 0.0:
          self.vitesse = 0.0
      
   def changerAngle(self,degree):
      self.angle = self.angle + degree

   def placerRobot(self,x, y):
      self.pos[0] = x
      self.pos[1] = y
      
   def mapUpdate(self,NouvelleCarte):
      self.map= NouvelleCarte