class compteGG:

    def __init__(self):
        self.mt = 0.0
        self.solde = 0.0


    def infoSolde(self):
        print("Votre solde est de {0} FCFA ! ".format(self.solde))

    def versement(self,mt):
        self.solde += mt
        print("Versement de {0} FCFA éffectué !".format(mt))
        self.infoSolde()
    
    def retrait(self,mt):
        if(mt>self.solde):
            print("Solde insuffisant")
        else:
            self.solde -= mt
            print("Le montant débité est de {0} FCFA".format(mt))
        self.infoSolde()
ch = compteGG()
ch.versement(30000)
