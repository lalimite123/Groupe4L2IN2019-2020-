class compteGG:

        def __init__(self,mt = 0.0,solde = 0.0):
        self._mt = m
        self._solde = solde
        
    def __str__(self):
         return "Solde disponible : {0}".format(self.solde)


    def infoSolde(self):
        print("Votre solde est de {0} FCFA ! ".format(self._solde))

    def versement(self,mt):
        self._solde += mt
        print("Versement de {0} FCFA éffectué !".format(mt))
        self.infoSolde()
    
    def retrait(self,mt):
        if(mt>solde):
            print("Solde insuffisant")
        else:
            self._solde -= mt
            print("Le montant débité est de {0} FCFA".format(mt))
        self.infoSolde()