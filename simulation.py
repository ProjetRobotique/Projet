from robot import Robot
from arene import Arene
from fenetre import Fenetre

# programme
a=Arene()
f= Fenetre(a)
f.afficher()
# binding de la fonction modifierTableau sur le canevas
f.can.bind("<Button-1>", f.modifierTableau)

# boucle principale
f.init_window.mainloop()