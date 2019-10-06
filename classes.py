#coding:utf-8

class Humain():
	def __init__(self, nom, prenom, age):
		self.nom = nom
		self.prenom = prenom
		self.age = age
	def personne(self):
		print("{} {} a {}ans".float(self.nom, self.prenom, self.age))

h1 = Humain("Michel", "Toma", 30)		
