from Player import Giant , Solider , Support
from GameVars import GameVariables

def createGame() -> None:
      #team_limit=int(input("Kaça kaç dövüş olsun ?\n"))
    Players=[]
    print("A takiminizi seçiniz:\n")
    for i in range(GameVariables.team_limit):
        name = input("karakterinize isim veriniz: ")
        team = "A"

        print("1 - 3 arasi karakterinizin türünü seçiniz:\n ")
        species = int(input("1-Giant\n2-Solider\n3-Support:\n "))


        if species == 1:
            player = Giant(name , team)
            Players.append(player)
        elif species == 2:
            player = Solider(name , team)
            Players.append(player)
        else:
            player = Support(name , team)
            Players.append(player)

    print("B takiminizi seçiniz:\n")
    
    for i in range(GameVariables.team_limit):
        name = input("karakterinize isim veriniz: ")
        team = "B"

        print("1 - 3 arasi karakterinizin türünü seçiniz:\n ")
        species = int(input("1-Giant\n2-Solider\n3-Support:\n "))


        if species == 1:
            player = Giant(name , team)
            Players.append(player)
        elif species == 2:
            player = Solider(name , team)
            Players.append(player)
        else:
            player = Support(name , team)
            Players.append(player)
    
    print(Players)

def startGame():
    pass


