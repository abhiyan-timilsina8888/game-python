import random

def gamewin(computer, player):
    if computer==player:
        return None
    elif computer=="r":
        if player=="p":
            return True
        elif player == "s":
            return False
    elif computer=="p":
        if player=="s":
            return True
        elif player == "r":
            return False    
    elif computer=="s":
        if player=="p":
            return True
        elif player == "r":
            return False
        
player=input("your's turn : rock(r) paper(p) and sissor(s)? ")        

print("computer's turn : rock(r) paper(p) and sissor(s)?")
ranNum= random.randint(1,3)
print(ranNum)
if ranNum==1:
    computer ='r'
elif ranNum==2:
    computer ='p'
elif ranNum==3: 
    computer ='s'
    
a=gamewin(computer,player)

print(f"computer choose {computer}")
print(f"player choose {player}")


if a== None:
    print("the game is tie!")
elif a:
    print("you won the game!")
else:
    print("you loose the game")


    






