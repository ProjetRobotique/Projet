from robot import Robot
from arene import Arene
from fenetre import Fenetre
from controler import Controler
from threading import Thread
import time

r=0
fps=20

try:
	print("robot reel")
	from robot2I013 import Robot2I013
	r= Robot2I013()
except:
	print("gopigo")
	from gopigo import Robot2I013
	from robot import Robot_Proxy
	r= Robot_Proxy([], Robot2I013())

r= Robot([])
c= Controler(r)
a=Arene(r)
f= Fenetre(a, c)

threadf= Thread(target=f.boucle, args=(fps,))
threada= Thread(target=a.boucle, args=(fps,))
threadc= Thread(target=c.boucle, args=(fps,))
threadf.start()
threada.start()
threadc.start()


# boucle principale
f.init_window.mainloop()
