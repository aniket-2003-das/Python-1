myDict = {
    "nwjw":"oiknwsj",
    "hjsu":"kimkwu",
    "ksnw":"osjjw"
}
print("optins are", myDict.keys())
a = input("enter the hindi word\n")
# print("the meaning of your word is:", myDict[a]) throws an error
print("the meaning of your word is:", myDict.get(a)) # returns null value if key is not present in dictionary.

