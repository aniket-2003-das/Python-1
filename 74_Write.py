# f = open('75_another.txt','w') # to write in file,content gets erased and is written from starting.
f = open('75_another.txt','a') # to append file,can be run multiple times

f.write("This text is written to the file.\n")
f.write("This text is written to the file.\n")
f.write("This text is written to the file.\n")
f.write("This text is written to the file.\n")

f.close()

