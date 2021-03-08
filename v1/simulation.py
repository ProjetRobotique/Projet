from robot2 import Robot
from affichageGraphique import Arene, Fenetre
from controleur import Controleur
from time import sleep

class Simulation:

    def __init__(self, robot, arene, controleur, fenetre, dep_robot_x, dep_robot_y):
        self.arene = arene
        self.robot = robot
        self.controleur = controleur
        self.fenetre = fenetre
        self.arene.placerRobot(dep_robot_x, dep_robot_y)

    def avance3sec(self):
        self.robot.setVitesse(1.08)
        
        for i in range(3):
            self.arene.placerRobot

        self.robot.setVitesse(0)

robot = Robot
arene = Arene(30, 25, robot)
fenetre = Fenetre(arene)
controleur = Controleur(robot, arene)
simulation = Simulation(robot, arene, controleur, fenetre, 15, 12)


fenetre.afficher()
fenetre.init_window.mainloop()
