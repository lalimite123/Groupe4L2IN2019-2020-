#coding:utf-8

class Argents():
# la class argents est parente
	

	def __init__(self, Nom, Prenom, ID):
		
		self.Nom = Nom
		self.Prenom = Prenom
		self.ID = ID  


class Gestionnaire(Argents):
	"""docstring for Gestionnaire elle est la une classe fille de Argent"""
	def Ajout(self, nom1, password1):
		self.nom1=nom1
		self.password1=password1

		nom = input("\t Quel est votre nom chere client")
		print("\t Creation du compte a reussi")
		print("\t BIENVENUE DANS NOTRE BANQUE",nom)
		print("\t *****************************")

		#fin de la procedure ajout
	def Suppresion(self, nom1, password1):
		self.nom1=nom1
		self.password1=password1
		print("\t***************************")
		print("\t*connexion au compte creer*")
		print("\t***************************")
		nom2 = input("\t entrer le nom de votre compte :")
		password2 = input("\t entrer votre mot de pass :")
		#conition de verification
		if nom2==nom1 and password2==password1:
			choix = input("SI voulez vraiment le surpprimer entrer 1 sinon 0 :")
			choix = int(choix)
			if choix == 1:
				print("votre compte à été surpprimer")
			"""else: 
				print(choixmenu())"""
		else: print("vaut information sont incorrect dsl")	
		
		
	

# programme principale

g1 = Gestionnaire("aime", "boaw", "01")

print("1)creer un compte")
print("2)surpprimer un compte")
print("3)infos lier aux emprunt")
choixmenu =input("faite votre choix  :")
choixmenu =int(choixmenu)
nom1= input("\t entrer le nom de votre compte :")
password1 = input("\t entrer votre mot de pass :")

if choixmenu == 2 :

	
	g1.Suppresion(nom1, password1)
elif choixmenu == 1:
	g1.Ajout(nom1, password1)
else :
	print("comende incorrect")


	


 	
#g1.Ajout(nom1, password1)



