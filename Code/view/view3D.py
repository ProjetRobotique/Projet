from direct.showbase.ShowBase import ShowBase
from panda3d.core import * 
from direct.directtools.DirectGeometry import LineNodePath 
from panda3d.core import GeomVertexFormat, GraphicsEngine, GeomVertexData, GeomVertexWriter, GeomTriangles, Geom, GeomNode, NodePath, GeomPoints, Point3,Vec3, Vec4, WindowProperties 
from direct.task import Task
from direct.filter.CommonFilters import CommonFilters

import sys
import time

from tkinter import *
from PIL import Image
from random import random
import numpy as np


from ..arene import Arene
from ..robots import Robot
from .cube import CubeMaker

class Camera(ShowBase):
	def __init__(self, arene, ives_data, fps):
		self.fps= fps
		self.ives_data = ives_data
		ShowBase.__init__(self, windowType='onscreen')

		self.disableMouse()
		
		base.startTk()  # start Tk integration
		base.spawnTkLoop()  # make panda3d part of the Tk mainloop
		
		# main jobs of the 3d-viewer follow here
		# Grille
		self.grid()
		
		self.arene= arene
		# Arene 3d 
		self.arene3D=[]
		self.cube= CubeMaker(0.5).generate()
		self.cube.setPos(-9.5, 9.5, 0.5)
		self.cube.reparentTo(render)
		# Creation des obstacles
		for y in range(len(self.arene.tableau)):
			L=[];
			for x in range(len(self.arene.tableau[0])):
				if self.arene.tableau[x][y]==1:
					tmp= CubeMaker(0.5).generate()
					tmp.setPos(self.cube, x, -y, 0.0)
					tmp.reparentTo(render)
					L.append(tmp)
				else:
					L.append(0)
			self.arene3D.append(L)
		self.initBalise()
		self.cam.setPos(self.cube, self.arene.robot.pos[0], -self.arene.robot.pos[1], 0.1)
		# Ajout d'une tache qui actualise la camera
		taskMgr.add(self.update, 'update')

	# initalise une balise
	def initBalise(self):
		# coodonnee de la balise
		x= 15
		y= 0
		self.arene.tableau[x][y]=3
		
		# generation d'une balise
		self.balise= CubeMaker(0.5).generate()
		self.balise.setPos(self.cube, x, -y, 0.0)
		self.balise.reparentTo(render)
		self.balise.setColor(255, 255, 255)
		self.tex= loader.loadTexture('Image/balise.jpg')
		self.balise.setTexGen(TextureStage.getDefault(), TexGenAttrib.MWorldPosition)
		self.balise.setTexProjector(TextureStage.getDefault(), render, self.balise)
		self.balise.setTexPos(TextureStage.getDefault(), 0.5,0.5,0.5)
		self.balise.setTexture(self.tex)
		self.balise.setHpr(0, 90,0)

	# actualise la camera du robot
	def get_image_camera(self):
		self.graphicsEngine.renderFrame()
		self.texture = Texture()
		self.texture = self.win.getScreenshot()  
		data = self.texture.getRamImageAs('RGBA')
		image = np.frombuffer(data, np.uint8) 
		image.shape = (self.texture.getYSize(), self.texture.getXSize(), self.texture.getNumComponents())
		image = np.flipud(image)
		self.arene.robot.camera= Image.fromarray(image, mode='RGBA')
		return Task.again
	
	# update la vision de la camera
	def update(self, task):
		# camera Robot
		self.cam.setPos(self.cube, self.arene.robot.pos[0], -self.arene.robot.pos[1], 0.1)
		self.cam.setHpr(90-self.arene.angle, 0.0, 0.0)
		# Obstacle
		for y in range(len(self.arene.tableau)):
			for x in range(len(self.arene.tableau[0])):
				# Obstacle nouveau
				if self.arene.tableau[x][y]==1 and self.arene3D[x][y]==0:
					self.arene3D[x][y]= CubeMaker(0.5).generate()
					self.arene3D[x][y].setPos(self.cube, x, -y, 0.0)
					self.arene3D[x][y].reparentTo(render)
				# Obstacle detruit
				elif self.arene.tableau[x][y]==0 and self.arene3D[x][y]!=0:
					self.arene3D[x][y].removeNode()
					self.arene3D[x][y]=0
		self.get_image_camera()
		return Task.again
	
	# Trace une grille
	def grid(self):
		raws1unit = 20
		rawsfithunit = 10
		d = 0
		X1 = 10
		X2 = -10
		Y1 = 10
		Y2 = -10

		linesX = LineNodePath(render,'quad',2,Vec4(.3,.3,.3,.3))
		linesXX = LineNodePath(render,'quad',1,Vec4(.3,.3,.3,.3))
		axis = LineNodePath(render,'axis',4,Vec4(.2,.2,.2,.2))
		quad = LineNodePath(render,'quad',4,Vec4(.2,.2,.2,.2))


		x1 = (0,Y2,0) 
		x2 = (0,Y1,0) 

		x3 = (X2,0,0)
		x4 = (X1,0,0)
		axis.drawLines([[x1,x2],[x3,x4]]) 
		axis.create() 

		q1 = (X1,Y1,0)
		q2 = (X1,Y2,0)

		q3 = (q2)
		q4 = (X2,Y2,0)

		q5 = (q4)
		q6 = (X2,Y1,0)

		q7= (q6)
		q8 = (X1,Y1,0)

		quad.drawLines([[q1,q2],[q3,q4],[q5,q6],[q7,q8]]) 
		quad.create() 

		for l in range (raws1unit-1):
			d+= 1
			l1 = (X2+d,Y1,0)
			l2 = (X2+d,Y2,0)
	
			l3 = (X2,Y1-d,0)
			l4 = (X1,Y1-d,0)  
	
			linesX.drawLines([[l1,l2],[l3,l4]]) 
			linesX.create()

		for l in range (rawsfithunit):
			d-=.2
			lx1 = (X2+1+d,Y1,0)
			lx2 = (X2+1+d,Y2,0)
	
			lx3 = (X2,Y1-1-d,0)
			lx4 = (X1,Y1-1-d,0)  
	
			linesXX.drawLines([[lx1,lx2],[lx3,lx4]]) 
			linesXX.create()
