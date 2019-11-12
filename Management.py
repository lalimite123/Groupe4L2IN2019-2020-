# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:56:08 2019

@author: ligar
"""

class Add_c():

	def __init__(self, CName,  PasswordC, IdC):

		self.CName = CName

		self.IdC = IdC

		self.PasswordC = PasswordC

	def Gestionnaire(self, CName, PasswordC, IdC):

		Add_c.__init__(self, CName, PasswordC, IdC)

		self.idcompte = 0



	def New(self):
        
       
		self.CName = str(input("YOUR NAME:"))
        
        
		self.PasswordC = str(input("YOUR PASS WORD:"))
        
		self.IdC = int(input("YOUR ID:"))



		self.idcompte = idcompte + 1



		if ((self.CName is None or len(self.PasswordC) < 4  or self.IdC is None)):

			print("Error: be sure to fill everything")

		else:

			

			a = print("Welcome {0} your account has been registered and your ID is: {1}<< " .format(self.CName, self.numero_compte))





	def Delete(self, PasswordC):
        

		PASS = str(input("ENTER HIS PASSWORD:  "))



		if (name == self.CName and PASS == self.PasswordC):
            
            a = str(input("Do you want to remove your count?"))
        if (a == "YES"):

				  print("account successfully deleted")

        else 

				   print("thank you for keeping your account with us")
