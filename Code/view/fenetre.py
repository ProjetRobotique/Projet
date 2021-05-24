# coding: utf-8
from math import pi as PI
from tkinter import *
from tkinter import ttk
from threading import Thread
import time

from panda3d.core import *
from direct.showbase.ShowBase import ShowBase

from ..control.controler import Controler
from ..arene import Arene
from .view3D import Camera

class Fenetre:
	def __init__(self, arene, control, fps):
		# Ajout de l'arene
		self.arene= arene
		#Robot
		self.robot= self.arene.robot
		#Controler
		self.control= control

		# fenêtre principale
		self.init_window=Tk()
		self.init_window.title("C'est bien parti pour le 100/100")
		self.init_window.geometry("1000x775")
		self.init_window.config(background='#41B77F')

		#texte
		self.label_title = Label(self.init_window, text="Clique gauche sur une case pour placer ou retirer un objet, le robot est dans la case rouge", font = ("",14), bg='#41B77F', fg='white')
		self.label_title.pack(side=BOTTOM)

		# Création d'une Frame pour les attributs du Robot
		self.frame_attribut= LabelFrame(self.init_window, text= "Attributs du Robot", relief="sunken", labelanchor='n', bd=5)
		self.frame_attribut.pack()

		# Attribut
		self.label_pos= Label(self.frame_attribut, text="position [x : y] : "+str(self.robot.pos))
		self.label_pos.pack()
		self.label_angle= Label(self.frame_attribut, text="angle: "+str((self.robot.angle/2*PI)*360)+" degrés")
		self.label_angle.pack()
		self.label_vitesse_roue= Label(self.frame_attribut, text="vitesse roues: "+str(self.robot.vitesse_roue))
		self.label_vitesse_roue.pack()

		# Création d'une Frame pour le contrôle du robot
		self.frame_control= LabelFrame(self.init_window, text="Contrôle Robot",labelanchor='n' ,relief="sunken", bd=5)
		self.frame_control.pack(side=LEFT)

		#bouton de contrôle du Robot
		self.button_arret = Button(self.frame_control, text="arreter", command= lambda: self.control.signal("arret"))
		self.button_arret.pack()

		self.button_turnLeft = Button(self.frame_control, text="Tourner Gauche", command=lambda:self.control.signal("tournerGauche"))
		self.button_turnLeft.pack()

		self.button_turnRight = Button(self.frame_control, text="Tourner Droite", command=lambda:self.control.signal("tournerDroite"))
		self.button_turnRight.pack()

		self.button_forward = Button(self.frame_control, text="Avancer", command=lambda:self.control.signal("avancer"))
		self.button_forward.pack()
		
		self.button_carre = Button(self.frame_control, text="Tracer Carre", command=lambda:self.control.signal("tracerCarre"))
		self.button_carre.pack()

		self.button_balise = Button(self.frame_control, text="balise", command=lambda:self.control.signal("balise"))
		self.button_balise.pack()
		
		self.button_quit = Button(self.init_window, text="cliquer pour quitter", command=self.quit)
		self.button_quit.pack(side=RIGHT)

		# les 2 couleurs à utiliser
		self.couleurs = {0: "white", 1: "#41B77F", 2: "red", 3:"purple"}

		# dimensions du canevas
		self.can_width = 620
		self.can_height = 620

		# taille d'une case
		self.size = 25

		# création canevas
		self.can = Canvas(self.init_window, width=self.can_width, height=self.can_height)
		self.can.pack()

		self.can.bind("<Button-1>", self.modifierTableau)

		self.grille_affiche=[]
		for i in range(len(self.arene.tableau)):
			L=[]
			for j in range(len(self.arene.tableau[i])):
				L.append(self.can.create_rectangle(i * self.size, j * self.size , i * self.size + self.size, j * self.size + self.size, fill = self.couleurs[self.arene.tableau[i][j]]))
			self.grille_affiche.append(L)

		self.init_window.after(int((1./fps)*1000), self.updateFenetre)


	def afficher(self):
		"""
		Fonction d'affichage du tableau ; 1 élément = 1 case
		La couleur de la "case" dépend de l'état de l'élement correspondant, 0 ou 1
		"""
		for i in range(len(self.arene.tableau)):
			for j in range(len(self.arene.tableau[i])):
				self.can.itemconfig(self.grille_affiche[i][j] , fill = self.couleurs[self.arene.tableau[i][j]])

	# A revoir, avec Arene
	def modifierTableau(self,evt):
		pos_x = int(evt.x / self.size)
		pos_y = int(evt.y / self.size)
		# inverser la valeur de l'élément cliqué si c'est un obstacle ou une case vide
		# ne fait rien si on clique sur le robot
		if self.arene.tableau[pos_x][pos_y] == 2:
			self.arene.tableau[pos_x][pos_y] = 2
		elif self.arene.tableau[pos_x][pos_y] == 0:
			self.arene.tableau[pos_x][pos_y] = 1
		else:
			self.arene.tableau[pos_x][pos_y] = 0

	def updateFenetre(self):
		self.afficher()
		self.label_pos.configure(text="position: "+str(self.arene.robot.pos))
		self.label_angle.configure(text="angle: "+str(self.arene.robot.angle))
		self.label_vitesse_roue.configure(text="vitesse roues: "+str(self.robot.vitesse_roue))
		self.init_window.after(50, self.updateFenetre)

	def quit(self):
		self.arene.exit=True
		self.control.exit=True
		time.sleep(0.5)
		self.init_window.destroy()



class Frame_Cam(ttk.Frame):
    def __init__(self, parent, arene, fps):
    
        ttk.Frame.__init__(self, parent)
        self.app = parent
        self.app3d = None
        self.arene= arene
        
        # create frame
        self.ives = ttk.Frame(parent)  # add a frame to the canvas
        self.ives.pack()
    
        self.launch_panda3d_app(fps)  # launch panda3d app

    def launch_panda3d_app(self, fps):
        # this is in case someone tries to launch a second panda3d app
        try: base.destroy()
        except NameError: pass
    
        self.app3d = Camera(self.arene, self.ives, fps)
        
        try:
            self.app3d.run()
        except SystemExit:
            base.destroy()  # so if i close the panda3d window it will not shut down tkinter as well



		