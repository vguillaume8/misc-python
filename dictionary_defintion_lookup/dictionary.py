# import library
import json

# Loading the json data as python dictionary
data = json.load(open("dictionary.json"))

# Function for retriving definition
def retrive_definiton(word):
    # Removing case-sensitivity from the program
    # For example 'Rain' and 'rain' will give the same output
    # Converting all letters to lower because out data is in that format
    word = word.lower()


    # Check for non existing words
    if word in data:
        return data[word]
    # To make sure the program return the definition of words that start with a capital leter
    elif word.title() in data:
        return data[word.title()]
    else:
        return ("The word does not exist, please double check it.")

# Input from user
word_user = input("Enter a word: ")

# Retrive the definition using function and print the result
print(retrive_definiton(word_user))
