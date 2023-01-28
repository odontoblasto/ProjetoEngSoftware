import random

listCardsCreated = [{'categoria':'pessoa','descrição':'mãe'}]

def shuffle(listCardsCreated):

    listCardsDescriptionDisplay = []
    listCardsDescriptionWrong = ['mãe','pai','filho','filha','tio','tia','prima','primo','avô','avó']
    listCardsDescriptionDisplay.append(listCardsCreated[0]['descrição'])

    print("\n\n - Vamos Lembrar.... ? - \n")

    while len(listCardsDescriptionDisplay) == 1 or len(listCardsDescriptionDisplay) < 5 :
        option = random.randint(0,len(listCardsDescriptionWrong)-1)
        if not listCardsDescriptionWrong[option] in listCardsDescriptionDisplay:
            listCardsDescriptionDisplay.append(listCardsDescriptionWrong[option])

    #print(listCardsDescriptionDisplay)
    shuffleDisplayAnswer(listCardsDescriptionDisplay)

def shuffleDisplayAnswer(listCardsDescriptionDisplay):

    listDisplayShuffledAnswer = []
    for i in range(5):

        option = random.randint(0, len(listCardsDescriptionDisplay) - 1)
        #print(listCardsDescriptionDisplay[option])
        listDisplayShuffledAnswer.append(listCardsDescriptionDisplay[option])
        del listCardsDescriptionDisplay[option]
    #print(listDisplayShuffledAnswer)
    display(listDisplayShuffledAnswer,listCardsCreated)

def display(listDisplayShuffledAnswer,listCardsCreated):

    rightAnswer = listCardsCreated[0]['descrição']

    score = 0
    attempts = 0
    flag = True

    while flag:

        print("\nQuem é essa pessoa ?")
        for i in listDisplayShuffledAnswer:
            print(i)

        option = input("Digite a opção CORRETA :\n")
        if option == rightAnswer:
            score += 100
            attempts += 1
            print("Parabéns você acertou !!!\n")
            #print("\nscore : ",score,"\nattempts : ",attempts)
            statistics(score,attempts)
            return
        else:
            score += 0
            attempts += 1
            print("\nTente de novo ...")
        print("\nscore : ", score, "\nattempts : ", attempts)
        print("Digite qualquer tecla para tentar de novo...")
        option = input("Ou N para sair....")

        if option =='N':
            flag = False
            print("\n\n FIM\n\n")
            statistics(score,attempts)

def statistics(score,attempts,name = 'teste',date = 'testedate'):

    print("- Seus Jogos -")
    print('\n\nNome : ',name, '\nData : ',date)
    print('Sua pontuação : ',score,'\nNúmero de tentativas :',attempts)
    return
# importar modulo Date


shuffle(listCardsCreated)

