#  remove_and_split function 

def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()


this = "     harry is a good boy     "
print(this)

n = remove_and_split(this, "harry")
print(n)

print(this.strip())
print(this.split())

# split segregates words and prints them as a list using ''.
# strip removes blank charectar spaces within the string.