# DICTIONARY METHODS :- 

myDict = {
    "fast": "In a quick Manner",
    "harry": "A Coder",
    "marks": [1,3,4],
    "anotherdict":{'harry':'Player'}, # NESTED DICTIONARY
    1:2
}
# dictionary meathods
print(myDict.keys())
print(type(myDict.keys()))#  type is dict_keys
print(list(myDict.keys()))# print the keys of the dictionary
print(myDict.values())# prints values
print(myDict.items())# prints keys and values
 
print(myDict)
updateDict ={
    "lovish": "friend",
    "shubham":"friend",
    "harry": "A teacher",

}
myDict.update(updateDict) # updated dictionary by adding key value pairs
print(myDict)
# same result
print(myDict.get("harry"))# returns none
print(myDict["harry"])# throws an error need to write correct keys.
