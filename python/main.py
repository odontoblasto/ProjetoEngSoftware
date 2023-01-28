
import random

def query(listCards):

  answer = ["irmã","irmão","tio","tia","avô","avó","primo","prima"]
  print(" - Query - ")
  print(listCards)
  wrong_answer = int(random.randint(0,len(answer)))
  print(answer[wrong_answer])
  menu()
  
def aboutUs():
  print("\n\n- Sobre - \n\n")
  print("\n\nSobre o Projeto Alzhma - \n\n")
  print("\n\nInformações sobre a estimulação Cognitiva Digital\n\n")
  option = int(input(" Digite qualquer tecla para sair\n\n "))
  if option:
    menu()

def play():
  print("\n\n- Construindo Lembranças - \n\n")
  print("\n\nJogar - \n\n")
  # construção objeto Card(lembrança)
  listCards = []
  print("- Criando Cards -\n\n")
  option = input(" Deseja criar um Card ? S/N\n\n")
  while option =='S':
    option = input("\nCategoria :\n")
    option1 = input("\nDescrição : \n")
    card = dict(categoria = option,descrição= option1)
    listCards.append(card)
    option = input("\n\n Deseja criar um Card ? S/N\n\n")
  #print(card,listCards)
  option = int(input("\n\n Digite 1 para Jogar ou 2 para Menu\n\n"))
  if option == 1:
    query(listCards)
  menu()
  #menu()
   
def menu():
  print("- Home - \n\n")
  print(" Projeto Alzhma - Python\n\n")
  print("1- Sobre o Projeto\n ")
  print("2- Jogar  \n")
  option = int(input("Escolha uma opção :\n "))
  while option < 1 or option > 2:
    option = int(input(" Digite 1 ou 2 para continuar...\n"))
  # fazer validação option
  if option == 1:
      aboutUs()
    
  elif option == 2:
    play()

  else:
    menu()


menu()
  
