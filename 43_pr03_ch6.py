text = input("enter the text")
spam = False

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False


if(spam):
    print("the text is spam")
else:
    print("text is not a spam")
