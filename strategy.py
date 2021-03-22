
class StrategyAvance:
	def __init__(self, control):
		self.enMarche=False
		self.control= control
		self.distance=10
		self.distanceCourant=0

	def run(self):
		self.enMarche=False


class StrategyTourneDroite:
	def __init__(self, control):
		self.enMarche=False
		self.control= control
		self.angle=0
		self.angleCourant=-90

	def run(self):
		self.enMarche=False
