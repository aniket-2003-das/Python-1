words =["hi","is","donkey","raju"]

with open("72_sample.txt") as f :
    content = f.read()

for word in words:
     content = content.replace( word, "$$$$$$")

with open("72_sample.txt", "w") as f :
    f.write(content)