import time
import math

class Robot2I013(object):
    """ 
    Classe d'encapsulation du robot et des senseurs.
    Constantes disponibles : 
    LED (controle des LEDs) :  LED_LEFT_EYE, LED_RIGHT_EYE, LED_LEFT_BLINKER, LED_RIGHT_BLINKER, LED_WIFI
    MOTEURS (gauche et droit) : MOTOR_LEFT, MOTOR_RIGHT
    et les constantes ci-dessous qui definissent les elements physiques du robot
    """

    WHEEL_BASE_WIDTH         = 117  # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER           = 66.5 #  diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi # perimetre de la roue (mm)
    
    def __init__(self,controler,fps=25,resolution=None,servoPort = "SERVO1",motionPort="AD1"):
        """ 
            Initialise le robot
            :controler: le controler du robot, muni d'une fonction update et d'une fonction stop qui 
                        rend in booleen (vrai a la fin du controle, faux sinon)
            :fps: nombre d'appel a controler.update() par seconde (approximatif!)
            :resolution: resolution de la camera
            :servoPort: port du servo (SERVO1 ou SERVO2)
            :motionPort: port pour l'accelerometre (AD1 ou AD2)
        """

        print("robot initialisé")
        

    def set_led(self, led, red = 0, green = 0, blue = 0):
        """
        Allume une led.
        
        :led: une des constantes LEDs (ou plusieurs combines avec +) : LED_LEFT_EYE, LED_RIGHT_EYE, LED_LEFT_BLINKER, LED_RIGHT_BLINKER, LED_WIFI.
        :red: composante rouge (0-255)
        :green:  composante verte (0-255)
        :blue: composante bleu (0-255)
        """
        print("la led passée s'allume")

    def get_voltage(self):
        """ get the battery voltage """
        print("voici le voltage de la batterie")


    def set_motor_dps(self, port, dps):
        """
        Fixe la vitesse d'un moteur en nombre de degres par seconde
        :port: une constante moteur,  MOTOR_LEFT ou MOTOR_RIGHT (ou les deux MOTOR_LEFT+MOTOR_RIGHT).
        :dps: la vitesse cible en nombre de degres par seconde
        """


        if not (isinstance(port, int)):
            print("le port passé doit être un int, ca n'est pas le cas")
        elif not (isinstance(dps, int)):
            print("le dps passé doit être un int, ca n'est pas le cas")
        else:
            print("le moteur " + str(port) + " tourne maintenant à " + str(dps) + " degrès par seconde")


    def get_motor_position(self):
        """
        Lit les etats des moteurs en degre.
        :return: couple du  degre de rotation des moteurs
        """
        print("voici la position du moteur")
   
    def offset_motor_encoder(self, port, offset):
        """
        Fixe l'offset des moteurs (en degres) (permet par exemple de reinitialiser a 0 l'etat 
        du moteur gauche avec offset_motor_encode(self.MOTOR_LEFT,self.read_encoders()[0])
        
        :port: un des deux moteurs MOTOR_LEFT ou MOTOR_RIGHT (ou les deux avec +)
        :offset: l'offset de decalage en degre.
        Zero the encoder by offsetting it by the current position
        """
        
        if not (isinstance(port, int)):
            print("le port passé doit être un int, ca n'est pas le cas")
        elif not (isinstance(offset, int)):
            print("l'offset passé doit être un int, ca n'est pas le cas")
        else :
            print("l'offset du moteur " + port + " est maintenant fixé à " + offset)

    def get_distance(self):
        """
        Lit le capteur de distance (en mm).
        :returns: entier distance en millimetre.
            1. L'intervalle est de **5-8,000** millimeters.
            2. Lorsque la valeur est en dehors de l'intervalle, le retour est **8190**.
        """
        print("voici la distance à l'obstacle")

    def servo_rotate(self,position):
        """
        Tourne le servo a l'angle en parametre.
        :param int position: Angle de rotation, de **0** a **180** degres, 90 pour le milieu.
        """
        
        if not(isinstance(position, int)):
            print("la position passée doit être un int, ca n'est pas le cas")
        elif (position < 0) or (position > 180):
            print("la position passée doit être entre 0 et 180 degrès, ca n'est pas le cas", e)
        else:
            print("Le robot a maintenant une position de " + str(position))
            
    def stop(self):
        """ Arrete le robot """
        print("le robot s'arrete")

    def get_image(self):
        print("voici l'image")
