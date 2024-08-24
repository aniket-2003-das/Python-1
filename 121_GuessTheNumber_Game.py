# Guess the number game
import random
randNumber = random.randint(1,100)
# print(randNumber)
userGuess = None 
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your Guess:\n"))
    guesses +=1
    if(userGuess == randNumber):
        print("you guessed it right!")
    else:
        if(userGuess>randNumber):
            print("you guessed it wrong! Enter a smaller number")
        else:
            print("you guessed it wrong! Enter a larger number")

print(f"You guessed the number in -: \n {guesses} guesses")

with open("122_highscore.txt", "r") as f:
    highscore = int(f.read()) # first save int literal in file.

if(guesses<highscore):
    print("congratulations you have just brocken the highscore")
    with open("122_highscore.txt", "w") as f:
        f.write(str(guesses))
