
class Compte():
   def __init__(self, id, MotDePasse):
      self.id = id
      self.MotDePasse = MotDePasse
      SalaireMensuel = 10000
      self.solde = 0
      self.EtatEmprunt = False
      self.SomEmpruntMax = SalaireMensuel * 3
      self.SoldeEmprunter = 0
   def emprunter(self):
      somme = input("veuillez entrer le montant a emprunter\n")
      somme = int(somme)
      if self.EtatEmprunt == True:
         print("desole vous avez une dette impayer")
      elif somme <= self.SomEmpruntMax:
         print("votre compte a ete crediter de...", somme)
         self.solde += somme
         self.EtatEmprunt = True
         print("votre nouveau solde est:\n", self.solde)
      else:
         print("desole vous ne pouvez pas emprunter cette somme")
  
mon = Compte(23, 46)
mon.emprunter()

