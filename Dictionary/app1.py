import json
import difflib
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

word = input("Enter a Word: ")

def meaning(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    elif word.title() in data.keys():
        return data[word.title()]
    elif word.upper() in data.keys():
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
         ans = input("Did you mean %s insted? Y/N: " % get_close_matches(word, data.keys())[0])
         if ans == 'Y':
             return data[ get_close_matches(word, data.keys())[0]]
         elif ans == 'N':
             return "The Word Doesnt Exist! Please Double Check Your Query!"
         else:
             return "we didn't understand your query!"
    else:
        return "Please check the word you typed!"

print(meaning(word))
