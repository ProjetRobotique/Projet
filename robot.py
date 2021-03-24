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
      
   def getDistance(self):
      ListeObstacle=[]
      TAILLE_ARENE_X = len(map)
      TAILLE_ARENE_Y = len(map)
      for i in TAILLE_ARENE_X:
         for j in TAILLE_ARENE_Y:
            if map[i][j]==1: #on recupere la position des obstacles de la map 
               ListeObstacle.append((i,j)) 
      #on test s'il y a un obstacle devant le robot
      u=self.pos[0]
      v=self.pos[1]
      while(u>= 0 and u<=TAILLE_ARENE_X and v>= 0 and v<=TAILLE_ARENE_Y):
         #on prolonge le vecteur angle jusqu'à trouver un obstacle
         u+=0.01*cos(self.angle)
         v+=0.01*sin(self.angle)
         for obstacle in ListeObstacle: 
            x,y= obstacle
            if (x==floor(u) and y==floor(v)): 
               return sqrt((y-pos[1])**2+(x-pos[0])**2) #calcule de la distance entre le robot et l'obstacle
      return -1 #retourne -1 si aucun obstacle devant le robot              
      
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
