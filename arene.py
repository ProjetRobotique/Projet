from tkinter import *
from robot import *

class Arene:
	def __init__(self,matrice_x=25,matrice_y=25):
		self.init_window=Tk()
		# fenêtre principale
		self.init_window.title("C'est bien parti pour le 100/100")
		self.init_window.geometry("720x575")
		self.init_window.config(background='#41B77F')

		#texte
		self.label_title = Label(self.init_window, text="Bienvenue sur cette fenêtre inutile", font = ("",20), bg='#41B77F', fg='white')
		self.label_title.pack(side=BOTTOM)

		# matrice à deux dimensions
		self.tableau = []
		for i in range(matrice_x):
		    self.tableau.append([0] * matrice_y)
		
		# Ajout du Robot dans l'Arène
		robot= Robot(self.tableau, "robot")
		pos= robot.pos
		self.tableau[int(pos[0])][int(pos[1])]=2 #conversion des floats en entier
		 
		# les 2 couleurs à utiliser
		self.couleurs = {0: "white", 1: "#41B77F", 2: "red"}

		# dimensions du canevas
		self.can_width = 500
		self.can_height = 500

		# taille d'une case
		self.size = 25

		# création canevas
		self.can = Canvas(self.init_window, width=self.can_width, height=self.can_height)
		self.can.pack()


	def afficher(self,t):
		"""
		Fonction d'affichage du tableau ; 1 élément = 1 case
		La couleur de la "case" dépend de l'état de l'élement correspondant, 0 ou 1
		"""
		for i in range(len(t)):
			for j in range(len(t[i])):
				self.can.create_rectangle(i * self.size, j * self.size , i * self.size + self.size, j * self.size + self.size, fill = self.couleurs[self.tableau[i][j]])

	def modifierTableau(self,evt):
		pos_x = int(evt.x / self.size)
		pos_y = int(evt.y / self.size)
		# inverser la valeur de l'élément cliqué si c'est un obstacle ou une case vide
	   	# ne fait rien si on clique sur le robot
		if self.tableau[pos_x][pos_y] == 2:
			self.tableau[pos_x][pos_y] = 2
		elif self.tableau[pos_x][pos_y] == 0:
			self.tableau[pos_x][pos_y] = 1
		else:
			self.tableau[pos_x][pos_y] = 0

		self.afficher(self.tableau)

	def simulation(self):
		self.afficher(self.tableau)
		# binding de la fonction modifierTableau sur le canevas
		self.can.bind("<Button-1>", self.modifierTableau)
		# boucle principale
		self.init_window.mainloop()

#-------------------------------------------------------
# programme
a=Arene()
a.afficher(a.tableau)
# binding de la fonction modifierTableau sur le canevas
a.can.bind("<Button-1>", a.modifierTableau)
# boucle principale
a.init_window.mainloop()
