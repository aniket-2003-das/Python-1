def game():
    return 66888


score = game()
with open("80_highscore.txt") as f :
    highscorestr = f.read()


if highscorestr =='':
    with open("80_highscore.txt","w") as f :
        f.write(str(score))


elif int(highscorestr)<score :
    with open("80_highscore.txt","w") as f :
        f.write(str(score))
