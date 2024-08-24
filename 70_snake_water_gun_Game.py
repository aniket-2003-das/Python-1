# SNAKE-WATER-GUN GAME 

import random
randNo = random.randint(1,3)
#print(randNo)

# Game algorithms.
def game(comp,you):

    
    if comp ==you:
        return None



    elif comp == 's':
        if you=='w':
            return False

        elif you == 'g':
            return True



    elif comp == 'w':
        if you=='g':
            return False

        elif you == 's':
            return True



    elif comp == 'g':
        if you=='s':
            return False

        elif you == 'w':
            return True

# Charectar selection for computer.

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'


# Charectar selection for player.

you = input("Your Turn : Snake(s) , Water(w) or Gun(g) ?\n ")

a = game(comp,you)

print(f"computer chosed {comp}")
print(f"you chosed {you}")

if a == None:
    print("MATCH TIED , REMATCH? ")

elif a:
    print("YOU WIN!")

else :
    print("YOU LOSE , REMATCH? ")
