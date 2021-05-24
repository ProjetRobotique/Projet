from threading import Thread
import time

from .robots import Robot
from .arene import Arene
from .view import Fenetre, MyApp, Frame_Cam
from .control import Controler


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
	r= Robot([])
"""

r= Robot([])
c= Controler(r)
a=Arene(r)
f= Fenetre(a, c, fps)

threada= Thread(target=a.boucle, args=(fps,))
threadc= Thread(target=c.boucle, args=(fps,))
threada.start()
threadc.start()

Frame_Cam(f.init_window, a, fps)

# boucle principale
f.init_window.mainloop()
