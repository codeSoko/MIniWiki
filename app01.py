#Import libraries/methods which will further use 
import json
from difflib import get_close_matches

#load json file which is or data source
dat=json.load(open("data.json"))

#create a function which performs logical implementation
def meaning(word):
    word=word.lower()
    if(word in dat.keys()):
        return dat[word]
    elif len(get_close_matches(word,dat.keys()))>0:
        yn=input("Did you mean %s instead? If yes press Y or N if no. \n" % get_close_matches(word,dat.keys(),cutoff=0.7)[0])
        if yn.upper()=='Y':
            return dat[get_close_matches(word,dat.keys())[0]]
        elif yn.upper()=='N':
            return("This word doesn't exists")
        else:
            return "Sorry !! We do not understand you."
        
    else:
        return("Word does not found")
    
word=input("Please enter the word: ")
output =meaning(word)
#we need to check whether this output is list or string 
#if it is list this would retun in per line string format
if type(output)==list:
    for item in output:
        print (item)
#if in string it will simply return the output
else:
    print (output)