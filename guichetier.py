#coding:utf-8

"""classe mère"""

class agents:
	def __init__(self, nom, ide):
		self.nom = nom
		self.ide = ide

	def travailler(self): #Methode de la classe agents
		print("L'agent {}, matricule {} travaille dans cette banque et il est {}:".format(self.nom, self.ide, self.poste))
		print("\t §%§%§%§%§%§%§%§%§%§%§%§%§%")

"""classe fille"""

class guichetier(agents):#la classe guichetier herite de la classe agents
	def __init__(self, nom_guichetier, ide_guichetier, poste):
		agents.__init__(self, nom_guichetier, ide_guichetier)
		self.poste = poste


	def retrait(montant, solde = 10000): #Fonction permettant de faire le retrait
		print("Operations de retrait :)")
		print("\t %§%§%§%§%§%§%§%§%§%§%§%§")
		montant = input("Entrer le montant à retitrer:")
		montant = int(montant)
		if montant >= solde:
			print("Désolé, votre solde est insuffisant.....")
		else:
			solde -= montant
			print("\t §%§%§%§%§%§%§%§%§%")
			print("Retrait effectué avec succès... :) Nouveau solde :{}".format(solde))
			print("\t §%§%§%§%§%§%§%§%§%§")

#Programme Principal

g1 = guichetier("DOUNIA DONATIEN", "18A036FS", "Guichetier") # Nouvelle instance de la classe guichetier

g1.travailler #Appel de la methode

g1.retrait() #Appel de la fonction
