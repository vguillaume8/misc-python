# import library
import json

# Loading the json data as python dictionary
data = json.load(open("dictionary.json"))

# Function for retriving definition
def retrive_definiton(word):
    return data[word]

# Input from user
word_user = input("Enter a word: ")

# Retrive the definition using function and print the result
print(retrive_definiton(word_user))
