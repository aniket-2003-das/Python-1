letter = '''Dear <|Name|>,
greetings from abc house
Im happpy to tell you about your selection
you are selected!
Date: <|Date|>
Have a great day.
thanks and regards.
'''
name = input("enter your name\n")
Date = input("enter Date\n")
letter=letter.replace("<|Name|", name)
letter=letter.replace("<|Date|", Date)
print(letter)


