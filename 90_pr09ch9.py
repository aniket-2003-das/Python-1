file1 = "88_copy.txt"
file2 = "80_highscore.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2 :
    print("files are identical")
else:
    print("files are not identical")