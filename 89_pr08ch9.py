with open("87_this.txt") as f :
    content = f.read()

    with open("88_copy.txt", 'w') as f:
        f.write(content)