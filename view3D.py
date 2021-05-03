from direct.showbase.ShowBase import ShowBase
from cube import CubeMaker
from pandac.PandaModules import * 
from direct.directtools.DirectGeometry import LineNodePath 

from panda3d.core import GeomVertexFormat, GeomVertexData, GeomVertexWriter, GeomTriangles, Geom, GeomNode, NodePath, GeomPoints, Point3,Vec3,Vec4


class MyApp(ShowBase):
    def __init__(self, tab):
        ShowBase.__init__(self)
        self.grid()
        self.cam.setPos(0.0, -20, 5.0)
        self.cam.setHpr(0.0, -10, 0.0)
        self.tab= tab
        self.arene= tab
        self.cube= CubeMaker(0.5).generate()
        self.cube.setPos(-10, 10, 0.5)
        self.cube.reparentTo(render)
        for y in range(len(tab)):
        	for x in range(len(tab[0])):
        		if tab[y][x]==1:
        			self.arene[y][x]= CubeMaker(0.5).generate()
        			self.arene[y][x]= setPos(self.cube, x+0.5, -y-0.5, 0.0)
        			self.arene[y][x].reparentTo(render)

    def grid(self):
    	raws1unit = 20
    	rawsfithunit = 100
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


tab=[]
app = MyApp(tab)
app.run() 