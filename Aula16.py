##`CRIE UM MÓDULO QUE SEJA CAPAZ DE FAZER A OPERAÇÃO DE UM BANCO,A PRINCIPIO APENAS SAQUES E DEPOSITO

menu.py

def menu():
    print(''' 
          
          1 - para saque
          2 - para deposito
          3 - Verificar         
          
          
          
          ''')


#-------------------------------------------------------

deposito.py

def deposito(a,b):
    print(a+b)


#---------------------------------------------------------
saque.py

def saque(a,b):
    print(a-b)

#-----------------------------------------------------------
main.py

from deposito import deposito
from saque import saque 
from menu import menu 


menu()
value = 100
def operation():
   
    choose = input('Digite a operação:')
    
    if choose == '1':
       meu_saque= float (input('digite o valor: '))
       print('Valor em conta R$')
       saque(value,meu_saque)
    elif choose == '2':
       meu_deposito= float (input('digite o valor: '))
       print('Valor em conta R$')
       deposito(value, meu_deposito)
    else: 
        print('Escolha uma opção valida')
        operation()          


operation()

def loop():
    choose2 = input('Deseja continuar? S/N')
    print(choose2)
    while choose2 == 'S': 
          operation()       
        

loop()
