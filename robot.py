# coding: utf-8

from math import *
class Robot:
   WHEEL_BASE_WIDTH = 117  # distance (mm) de la roue gauche a la roue droite.
   WHEEL_DIAMETER   = 66.5 #  diametre de la roue (mm)
   MOTOR_LEFT=1
   MOTOR_RIGHT=2
   
   def __init__(self,carte,nom):
      self.id= nom
      self.map = carte #le robot recupere la grille
      self.vitesse = 0.0
      self.pos = [0.0,0.0]
      self.angle = 0
      self.vitesse_roue=[0,0] # En degre par seconde
      
   def get_distance(self):
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
      
   def set_motor_dps(self, port, dps): #prend en argument le nombre de tours par minutes en plus ou en moins voulus.
      if port==self.MOTOR_LEFT:
         self.vitesse_roue[0]= dps
      elif port==self.MOTOR_RIGHT:
         self.vitesse_roue[1]= dps
      else:
         self.vitesse_roue=[dps,dps]
  
   def stop(self):
      self.vitesse_roue=[0,0]
      
   def mapUpdate(self,NouvelleCarte):
      self.map= NouvelleCarte
  

class Robot_Proxy:
   WHEEL_BASE_WIDTH = 117  # distance (mm) de la roue gauche a la roue droite.
   WHEEL_DIAMETER   = 66.5 #  diametre de la roue (mm)
   MOTOR_LEFT=1
   MOTOR_RIGHT=2

   def __init__(self,carte,nom, robot):
      self.id= nom
      self.map = carte #le robot recupere la grille
      self.pos = [0.0,0.0]
      self.angle = 0
      self.vitesse_roue=[0,0] # En degre par seconde
      self.robot= robot

   def set_motor_dps(self, port, dps): #prend en argument le nombre de tours par minutes en plus ou en moins voulus.
      if port==self.MOTOR_LEFT:
         self.vitesse_roue[0]= dps
      elif port==self.MOTOR_RIGHT:
         self.vitesse_roue[1]= dps
      else:
         self.vitesse_roue=[dps,dps]
      self.robot.set_motor_dps(port, dps)
     
   def get_distance(self):
      return self.robot.get_distance()  

   def stop(self):
      self.vitesse_roue=[0,0]
      self.robot.stop()

   def mapUpdate(self,NouvelleCarte):
      self.map= NouvelleCarte
