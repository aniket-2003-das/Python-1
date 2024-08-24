from calendar import c


myDict = {
    "Fast": "In a quick Manner",
    "Harry": "A Coder",
    "marks": [1,3,4],
    "anotherdict":{'harry':'Player'} # NESTED DICTIONARY
}
print(myDict['marks'])
print(myDict['Fast'])
myDict['marks']=[45,56,67]
print(myDict['marks'])
print(myDict['anotherdict']['harry'])

