from threading import Thread
import time

from .robots import Robot
from .arene import Arene
from .view import Fenetre, MyApp, Frame_Cam
from .control import Controler


# refaire controler
# GET MOTOR POSITION
# PANDA 3D
# 25 mai soutenance
r=0
fps=20
"""
try:
	from .robot2I013 import Robot2I013
	from .robot import Robot_Proxy
	print("Robot Reel")
	r= Robot_Proxy([], Robot2I013())
except:
	print("Robot Virtuelle")
	#from .robot import Robot
	r= Robot([])"""

r= Robot([])
c= Controler(r)
a=Arene(r)
f= Fenetre(a, c)

Frame_Cam(f.init_window, a, fps)

threadf= Thread(target=f.boucle, args=(fps,))
threada= Thread(target=a.boucle, args=(fps,))
threadc= Thread(target=c.boucle, args=(fps,))
threadf.start()
threada.start()
threadc.start()


# boucle principale
f.init_window.mainloop()
