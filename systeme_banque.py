#coding:utf-8
from time import sleep

class Client():
	def __init__(self, nom, prenom, numero_id, mdp):
		self.nom = nom
		self.prenom = prenom
		self.numero_id = numero_id
		self.mdp = mdp

### ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++###
### ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++###

class Gestionnaire(Client):
	def __init__(self, nom, prenom, numero_id, mdp):
		Client.__init__(self, nom, prenom, numero_id, mdp)
		self.numero_compte = 0

	def ajout_client(self):
		message = "Enregistrement du client"
		print(message.upper())

		print("\n\n******************************\n")

		print("Veillez remplire ce formulaire (*) \n")

		try:
			self.nom = str(input("Nom:  "))
			self.prenom = str(input("Prénom:  "))
			self.numero_id = str(input("Numero ID:  "))
			self.mdp = (input("Mot de passe (04 chiffres):  "))
		except:
			print("Veillez rentrer des bonnes informations.")

		"""if (len(self.mdp) > 4):
			print("Le nombre de chiffre dépasse 04, recommencer")
			self.mdp = int(input("Mot de passe (04 chiffres):  "))"""

		self.numero_compte += 1

		if ((self.nom is None or self.prenom is None) and (self.numero_id is None or self.mdp is None)):
			print("Erreur d'enregistrement, manque d'information")
		else:
			sleep(1)
			print("Votre numéro de compte est >> A{} << " .format(self.numero_compte))

			sleep(2)

			print("\nBienvenue {} {}, votre enregistrement à notre banque a réussit." .format(self.prenom, self.nom))

			sleep(2)
		print("\n========== Enregistrement terminé ==========")

	def supression_compte(mdp):
		message = "Supression de compte"
		print(message.upper())

		print("\n\n******************************\n")

		print("Vérification d'informations:")

		nom1 = str(input("Votre nom:  "))
		mot_de_passe = str(input("Votre mot de passe:  "))

		if (mot_de_passe == mdp):

			print("Voulez-vous suprimmer votre compte ?? (1 = oui et 0 = nom)")
			reponse = int(input(">>  "))

			if reponse == 1:
				print("supression de compte en cours...")
				sleep(5)
				print(">> Compte suprimer <<")
			elif reponse == 0:
				print("Supression de compte annuler")
		else:
			print("Erreur... (pas de base de données pour vérification information)")

	def modification_de_compte(self, nom, prenom, mdp, numero_id):
		message = "Modification de compte"
		print(message.upper())

		print("\n\n******************************\n")

		print("Modification de mot de passe:  \n")
		try:
			ancien_psw = int(input("Entrer l'ancien mot de passe: "))
		except:
			print("Le mot de passe doit etre des chiffres")
		if ancien_psw == mdp:
			new_psw = int(input("Entrer un nouveau mot de passe: "))
			if (len(new_psw) > 4):
				print("Le nombre de chiffre dépasse 04, recommencer")
				new_psw = int(input("Mot de passe (04 chiffres):  "))
		else:
			print("Mot de passe incorrect (faute de base de données pour récupération d'information)")

		print("\n========== Modification effectuer ==========")

	def emprunt(self):
		message = "Emprunt d'argent à partir d'un compte courant"
		print(message.upper())

		print("\n\n******************************\n")

		nb_dette = 0

		nouveau_solde = int(input("Votre salaire:  "))

		print("Votre salaire mensuel est de:'{}' fcfa" .format(nouveau_solde))

		salaire = 100000

		if nouveau_solde <= salaire:
			print("Taux d'interet 15%")
			print("Etes vous pret à emprunter ?? (1 = oui)")
			reponse = int(input(">>  "))

			if reponse == 1:
				interet = (nouveau_solde * 15) / 100
				emprunter = int(input("Entrer la somme à emprunter: "))

				nb_dette += 1

				print("Vous avez emprunter {} fcfa, et la banque en coupe l'interet dans votre salaire apres un mois" .format(emprunter))

				solde_apres_emp = nouveau_solde - interet

				print("Vous avez empruntez déjà >>{} fois<< " .format(nb_dette))

				if nb_dette > 1:
					print("Vous pouvez plus empruntez, vous avez une dette")
			else:
				pass
		elif nouveau_solde >= 100000:
			print("Pour le moment nous ne pouvons pas vous faire d'emprunt.")
		else:
			print("Allez voir ailleur svp...")


### ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++###
### ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++###

class Guichetier(Gestionnaire):
	def __init__(self, nom, prenom, numero_id, mdp):
		Gestionnaire.__init__(self, nom, prenom, numero_id, mdp)
	
	def versement_argent(self):
		message = "Versement argent"
		print(message.upper())

		print("\n\n******************************\n")

		print("Versement sur quel compte: ??")
		print("1- Courant")
		print("2- salaire")
		#print("3- client")
		#print("2- étranger")

		reponse = int(input(">>  "))
		if reponse == 1:
			print("Versement sur un compte courant. nom client: >> {} <<" .format(self.nom))

			somme_a_verser = int(input("entrer la somme à verser. Somme minimale = 500 fcfa:  "))
			if somme_a_verser <= 500:
				print("la somme doit pas etre inférieur à 500 fcfa")
			else:
				sleep(2)
				nouveau_solde = somme_a_verser
				print("La somme verser dans votre compte courant est de {} fcfa " .format(nouveau_solde))

		###++++++++++ compte salarial +++++++++++###

		elif reponse == 2:
			print("Versement dans votre compte (salaire)")
			somme_a_verser = int(input("Entrer la somme:  "))
			sleep(2)
			print("La somme verser dans votre compte est {} " .format(somme_a_verser))
		else:
			print("Erreur de choix !!")

	def retrait_argent(mdp):
		message = "Retrait d'argent"
		print(message.upper())

		print("\n\n******************************\n")

		print("Retrait pour quel compte: ??")
		print("1. courant")
		print("2. salaire")

		#Controleur.verification_caisse()

		reponse = int(input(">>  "))
		if reponse == 1:
			somme_a_retirer = int(input("Entrer la somme à retirer pour votre compte courant: "))

			mot_de_passe = int(input("Entrer votre mot de passe: "))
			if mot_de_passe == mdp:
				if(somme_a_retirer > nouveau_solde or somme_a_retirer <= 0):
					print("La somme à retirer est inférieur ou supérieur à votre solde.")
				else:
					sleep(5)
					print("Vous avez effectuer un retrait de < {} > fcfa" .format(somme_a_retirer))
					sleep(2)

					solde_restant = nouveau_solde - somme_a_retirer

					print("Votre nouveau solde est de < {} > fcfa" .format(solde_restant))
			else:
				print("Erreur... (pas de base de données pour vérification information) ")

		###-------------------- compte salaire --------------------###

		elif reponse == 2:
			somme_a_retirer = int(input("Entrer la somme à retirer pour votre compte (Salaire): "))

			mot_de_passe = int(input("Entrer votre mot de passe: "))
			if mot_de_passe == mdp:
				if(somme_a_retirer > nouveau_solde or somme_a_retirer <= 0):
					print("La somme à retirer est inférieur ou supérieur à votre solde.")
				else:
					sleep(3)
					print("Vous avez effectuer un retrait de < {} > fcfa" .format(somme_a_retirer))
					sleep(2)

					solde_restant = nouveau_solde - somme_a_retirer

					print("Votre nouveau solde est de < {} > fcfa" .format(solde_restant))
			else:
				print("Erreur de mot de passe")
		else:
			print("Erreur de choix !!")

		print("\n=============== Retrait terminé ===============")

		###*************** Virement ***************###

		print("Voulez-vous faire des virements ?? (1 = oui / 0 = non)")
		reponse = int(input(">>  "))

		if reponse == 1:
			N_compte = int(input("Numero du compte:  "))
			nom_compte = str(input("Nom compte: "))
			nom_compte_virer = str(input("Nom compte virer: "))

			somme_a_virer = int(input("Somme à virer :  "))

			print("Virement à partir du compte {} pour compte << {} >> d'une somme de {} fcfa" .format(nom_compte_virer, nom_compte,somme_a_virer))
		elif reponse == 0:
			pass
		else:
			print("Erreur de choix...")

		print("\n============== Virement effectué ===============")


### ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++###
### ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++###

"""class Controleur():

	def verification_caisse():
		if (nouveau_solde is not None) and (somme_a_verser is not None):
			pass
		else:
			print("Il y a pas d'argent en caisse")"""

### ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++###
### +++++++++++++++++++++++++++++++++++ Programme principal ++++++++++++++++++++++++++++++++++++++++++++++++###
### ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++###

Gestio = Gestionnaire("Donald", "Aimerite", "698604247", "1234")
Guiche = Guichetier("Donald", "Aimerite", "698604247", "1234")

print("Que voulez vous faire: ")
print("1- Créer un compte")
print("2- Supression du compte")
print("3- Modification du compte")

reponse = int(input(">>  "))

print("\n\n******************************\n")

if reponse == 1:
	Gestio.ajout_client()

	print("\n\n******************************\n")

	sleep(3)

	print("Apres enregistrement vous pouvez: ")
	print("1- VERSEMENT D'ARGENT(Compte courant, salaire)")
	print("2- RETRAIT D'ARGENT")
	print("3- EMPRUNT D'ARGENT")

	sleep(2)

	print("Voulez-vous faire une opération ?? (1 = oui et 0 = non)")
	reponsec = int(input(">>  "))
	if reponsec == 1:
		print("Que voulez vous faire: [(1- versement), (2- retrait), (3- emprunt)]")
		reponse_client = int(input(">>  "))

		print("\n\n******************************\n")

		if reponse_client == 1:
			Guiche.versement_argent()
		elif reponse_client == 2:
			Guiche.retrait_argent()
		elif reponse_client == 3:
			Gestio.emprunt()
		else:
			pass
	elif reponsec == 0:
		print("Merci d'utiliser notre service.")
	else:
		pass

elif reponse == 2:
	Gestio.supression_compte()
elif reponse == 3:
	Gestio.modification_de_compte("Donald", "Aimerite", "698604247", "1234")
else:
	print("Auccun des choix n'a été fait.")
