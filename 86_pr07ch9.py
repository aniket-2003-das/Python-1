content = True
i = 1
with open("84_logfilefrom_ibm.txt") as f:
    while content:
        content = f.readline()

        if 'python' in content.lower():
            print(content)
            print(f"yes. python is present in line number: {i}")
            print(i)
        i+=1
        