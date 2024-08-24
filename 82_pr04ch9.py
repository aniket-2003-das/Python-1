with open("72_sample.txt") as f :
    content = f.read()

content = content.replace("donkey", "$$$$$$")

with open("72_sample.txt", "w") as f :
    f.write(content)
