with open("84_logfilefrom_ibm.txt") as f:
    content = f.read()

if 'python' in content.lower() :
    print("python is present")
else:
    print("no python is not present")