from Imc import Imc

def i(): #apenas para printar linha e realizar a divisória da tela
  print('-'*85)

i()
#Criação dos Objetos, foi usado os 5 exemplos para bater com os 5 cálculos
pac1 = Imc('Jonathan Felix',1,1)
pac2 = Imc('Ana Maia',1.80,75)
pac3 = Imc('Brenna Lucia',1.80,90)
pac4 = Imc('Charles Will',1.20,50)
pac5 = Imc('Panda Silva',1.10,90)

################### PACIENTE 1 ###################################
pac1.apresentar() 
i()
pac1.calc_imc() 
i()
print('\n')
################### PACIENTE 2 ###################################
pac2.apresentar()
i()
pac2.calc_imc()
i()
print('\n')
################### PACIENTE 3 ###################################
pac3.apresentar()
i()
pac3.calc_imc()
i()
print('\n')
################### PACIENTE 4 ###################################
pac4.apresentar()
i()
pac4.calc_imc()
i()
print('\n')
################### PACIENTE 5 ###################################
pac5.apresentar()
i()
pac5.calc_imc()
i()
print('\n')
