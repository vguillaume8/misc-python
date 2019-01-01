# import library
import json
import difflib #Text proccessing servuces
from difflib import get_close_matches

# Loading the json data as python dictionary
data = json.load(open("dictionary.json"))

# Function for retrieving definition
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
    # To make sure the program returns the definiton of acronyms
    elif word.upper() in data:
        return data[word.upper()]

    # searches for a similar word
    elif len(get_close_matches(word, data.keys())) > 0:
        action =  raw_input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])

        # If the answer is yes, retrieve definition of suggested word
        if(action == "y"):
            return data[get_close_matches(word, data.keys())[0]]

        elif (action == "n"):
            return ("The word doesn't exist, yet.")

        else:
            return ("We don't understand you entry")


# Input from user
word_user = raw_input("Enter a word: ")

# Retrive the definition using function and print the result
output = (retrive_definiton(word_user))

# If a word has more than one definition, print them recursively
if type(output) == list:
    for item in output:
        print "-", item

# For words having single definition
else:
    print "-", output

