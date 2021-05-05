from direct.showbase.ShowBase import ShowBase
from panda3d.core import * 
from direct.directtools.DirectGeometry import LineNodePath 
from panda3d.core import GeomVertexFormat, GeomVertexData, GeomVertexWriter, GeomTriangles, Geom, GeomNode, NodePath, GeomPoints, Point3,Vec3, Vec4, WindowProperties 
from direct.task import Task

import sys
import time

from tkinter import *
from tkinter import ttk, Checkbutton, Canvas

from ..arene import Arene
from .cube import CubeMaker


class MyApp(ShowBase):
	def __init__(self, arene, ives_data, fps):
		self.fps= fps
		self.ives_data = ives_data
		ShowBase.__init__(self, windowType='onscreen')

		self.disableMouse()
		
		base.startTk()  # start Tk integration
		base.spawnTkLoop()  # make panda3d part of the Tk mainloop
		
		# main jobs of the 3d-viewer follow here
		self.exit=False
		self.grid()
		self.cam.setPos(0.0, -20, 5.0)
		self.cam.setHpr(0.0, -10, 0.0)
		self.arene= arene
		self.arene3D=[]
		self.cube= CubeMaker(0.5).generate()
		self.cube.setPos(-9.5, 9.5, 0.5)
		self.cube.reparentTo(render)
		for y in range(len(self.arene.tableau)):
			L=[];
			for x in range(len(self.arene.tableau[0])):
				if self.arene.tableau[y][x]==1:
					tmp= CubeMaker(0.5).generate()
					tmp;setPos(self.cube, x, -y, 0.0)
					tmp.reparentTo(render)
					L.append(tmp)
				else:
					L.append(0)
			self.arene3D.append(L)
		self.accept("escape", sys.exit)
		taskMgr.add(self.update, 'update')

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

	# update la vision de la camera
	def update(self, task):
		for y in range(len(self.arene.tableau)):
			for x in range(len(self.arene.tableau[0])):
				# Robot
				if  self.arene.tableau[y][x]==2:
					self.cam.setPos(self.cube, x, -y, 0.5)
					self.cam.setHpr(self.arene.angle, 0.0, 0.0)
				# Obstacle nouveau
				elif self.arene.tableau[y][x]==1 and self.arene3D[y][x]==0:
					self.arene3D[y][x]= CubeMaker(0.5).generate()
					self.arene3D[y][x].setPos(self.cube, x, -y, 0.0)
					self.arene3D[y][x].reparentTo(render)
				# Obstacle detruit
				elif self.arene.tableau[y][x]==0 and self.arene3D[y][x]!=0:
					self.arene3D[y][x].destroy()
					self.arene3D[y][x]=0
		return Task.again

