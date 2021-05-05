from .robots import Robot
from .arene import Arene
from .view import Fenetre, MyApp, Frame_Cam
from .control import Controler


r= Robot([])
c= Controler(r)
a=Arene(r)
f= Fenetre(a, c)

Frame_Cam(f.init_window, a)

# boucle principale
f.init_window.mainloop()
