# coding: utf-8
from arene import Arene
from math import pi as PI
from tkinter import *
from threading import Thread
from controler import Controler
import time

class Fenetre:
	def __init__(self, arene, control):
		# Ajout de l'arene
		self.arene= arene

		# En marche
		self.exit= False

		# Vitesse du robot
		self.arene.robot.vitesse=2

		#Robot
		self.robot= self.arene.robot

		#Controler
		self.control= control

		self.init_window=Tk()
		# fenêtre principale
		self.init_window.title("C'est bien parti pour le 100/100")
		self.init_window.geometry("1000x775")
		self.init_window.config(background='#41B77F')

		self.info= Label(self.init_window, text="Information:\n", relief="sunken", bd=5)
		self.info.pack()

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
		self.label_vitesse= Label(self.frame_attribut, text="vitesse: "+str(self.robot.vitesse*0.15*3.6)+" km/h")
		self.label_vitesse.pack()

		# Création d'une Frame pour le contrôle du robot
		self.frame_control= LabelFrame(self.init_window, text="Contrôle Robot",labelanchor='n' ,relief="sunken", bd=5)
		self.frame_control.pack(side=LEFT)

		#bouton de contrôle du Robot
		self.button_demarrer = Button(self.frame_control, text="demarrer", command= lambda: self.control.signal("demarrer"))
		self.button_demarrer.pack()

		self.button_arret = Button(self.frame_control, text="arreter", command= lambda: self.control.signal("arret"))
		self.button_arret.pack()

		self.button_haut = Button(self.frame_control, text="avance", command= self.arene.avancerRobot)
		self.button_haut.pack()
		
		self.button_tourne= Button(self.frame_control, text="tourne à droite", command= lambda: self.control.tourneRobot)
		self.button_tourne.pack()
		
		self.button_tourne10= Button(self.frame_control, text="tourne de 10 degrés", command=lambda: self.control.signal("tourneRobot10"))
		self.button_tourne10.pack()
		
		self.button_tourne_10= Button(self.frame_control, text="tourne de -10 degrés", command=lambda: self.control.signal("tourneRobot_10"))
		self.button_tourne_10.pack()
		
		self.button_augmenteVitesse = Button(self.frame_control, text="accelerer", command=lambda:self.control.signal("augmenterVitesseRobot"))
		self.button_augmenteVitesse.pack()
		
		self.button_diminueVitesse = Button(self.frame_control, text="ralentir", command=lambda:self.control.signal("diminuerVitesseRobot"))
		self.button_diminueVitesse.pack()

		self.button_quit = Button(self.init_window, text="cliquer pour quitter", command=self.quit)
		self.button_quit.pack(side=RIGHT)

		# les 2 couleurs à utiliser
		self.couleurs = {0: "white", 1: "#41B77F", 2: "red"}

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

	def boucle(self,fps):
		while True:
			# Demander au prof si c'est correcte
			if self.exit:
				break
			self.updateFenetre()
			time.sleep(1./fps)

	def updateFenetre(self):
		self.afficher()
		self.label_pos.configure(text="position: "+str(self.arene.robot.pos))
		self.label_vitesse.configure(text="vitesse: "+str(self.arene.robot.vitesse*0.15*3.6)+" km/h")
		self.label_angle.configure(text="angle: "+str(self.arene.robot.angle*180./PI%360))

	def quit(self):
		self.exit= True
		self.arene.exit=True
		self.control.exit=True
		self.init_window.destroy()

