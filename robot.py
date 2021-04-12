# coding: utf-8
from gopigo import Robot2I013
from math import *
class Robot:
   WHEEL_BASE_WIDTH = 117  # distance (mm) de la roue gauche a la roue droite.
   WHEEL_DIAMETER   = 66.5 #  diametre de la roue (mm)
   MOTOR_LEFT=1
   MOTOR_RIGHT=2
   
   def __init__(self,carte):
      self.map = carte #le robot recupere la grille
      self.vitesse = 0.0
      self.pos = [0.0,0.0]
      self.angle = 0
      self.vitesse_roue=[0,0] # En degre par seconde
      self.crayon=0
      
   def get_distance(self):
      ListeObstacle=[]
      TAILLE_ARENE_X = len(self.map)
      TAILLE_ARENE_Y = len(self.map[0])
      for j in range(TAILLE_ARENE_Y):
         for i in range(TAILLE_ARENE_X):
            if self.map[i][j]==1: #on recupere la position des obstacles de la map 
               ListeObstacle.append((j,i)) 
      #on test s'il y a un obstacle devant le robot
      u=self.pos[0]
      v=self.pos[1]
      while(u>= 0 and u<TAILLE_ARENE_X and v>= 0 and v<TAILLE_ARENE_Y):
         #on prolonge le vecteur angle jusqu'à trouver un obstacle
         u-=cos(self.angle*pi/180.0)
         v-=sin(self.angle*pi/180.0)
         print(u,v)
         for obstacle in ListeObstacle: 
            x,y= obstacle
            if (x==floor(u) and y==floor(v)):
               print("Obstacle trouve")
               return sqrt((y-self.pos[1])**2+(x-self.pos[0])**2) #calcule de la distance entre le robot et l'obstacle
      print("Obstacle pas trouve")
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
      
   def up(self):
   	self.crayon=1
   
   def down(self):
   	self.crayon=0
  
  
class Robot_Proxy:
   WHEEL_BASE_WIDTH = 117  # distance (mm) de la roue gauche a la roue droite.
   WHEEL_DIAMETER   = 66.5 #  diametre de la roue (mm)
   MOTOR_LEFT=1
   MOTOR_RIGHT=2

   def __init__(self,carte, robot):
      self.map = carte #le robot recupere la grille
      self.pos = [0.0,0.0]
      self.angle = 0
      self.vitesse_roue=[0,0] # En degre par seconde
      self.robot= robot
      self.crayon= 0
      
   def up(self):
   	self.crayon=1
   	self.robot.up()
   
   def down(self):
   	self.crayon=0
   	self.robot.down()
   	

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
