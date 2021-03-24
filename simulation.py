from robot import Robot
from arene import Arene
from fenetre import Fenetre
from threading import Thread
from controler import Controler

fps=20
# programme
r= Robot([],"Robot")
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
