'''Can you create a program to solve a word jumble?  
(More info here.)  The program should accept a string 
as input, and then return a list of words that can be
created using the submitted letters.  For example, on
the input "dog", the program should return a set of 
words including "god", "do", and "go".
 
Please implement the program in Python but refrain
from using any helper modules or imports (e.g. itertools). 
In order to verify your words, just download an 
English word list (here are a few).  Then upload 
your program to GitHub or Gist, and send it back!
'''
 
import time
# Find all the words that are anagrams with each other and group them together
# use a dictionary structure to be able to look up anagrams of sets of letters
def preprocessDictionary():
    anagrams = {}
    f = open('wordlist.txt','r')
    for line in f:   
            if "'" in line or "-" in line: continue     # get rid of the words that contain an apostrophe or dash 
            key = list(line[0:-1])                   # don't use the last character since it's '\n'     
            key.sort()
            key = "".join(key)
            if key in anagrams:
                anagrams[key] = anagrams[key] + [line[0:-1]]
            else: anagrams[key] = [line[0:-1]]
    del anagrams['']                                   #remove the empty string from dictionary
    # save the dictionary
    f2=open ('anagrams.txt' , 'w')
    for key in anagrams.keys():
        line = key
        for word in anagrams[key]:
            line += " " + word
        line += '\n'
        f2.write(line)
        
# Returns a dictionary of anagrams, read from file        
def loadAnagrams():
    anagrams = {}
    f = open('anagrams.txt','r')
    for line in f:
        key = line.split(" ")[0]
        anagrams[ key ] = line[0:-1].split(" ")[1:]     #ignore the last character in line ('\n')
    return anagrams


# no word in the dictionary has more than 6 repeated letters, so if the input string
# has letters that repeat more than 6 times, get rid of them to avoid extra work,
# and avoid errors when creating the key
def trimExtraLetters(word):
    word = list(word)	                            # sort letters
    word.sort()
    count = 1
    ret = word[0]
    for i in xrange(1,len(word)):
        if word[i] != word[i-1] :
            count = 1
        else:
            if count >= 6 : continue                # if more than 6 repeats, stop adding repeated letters to the return word
            count+=1
        ret += word[i]
    return ret

# Receives a set of letters and returns all the words that can be created with those letters
def jumble(word):
    global anagrams
    word = trimExtraLetters(word)                   # returns the letters sorted, with maximum 6 repetitions each
    subsets = getSubsets(word)
    result =[]
    for i in xrange(0,len(subsets)):                # compare each of the subsets with the dictionary entries
        key = subsets[i]
        if key in anagrams: result+= anagrams[key]  # if it matches an entry, add those words to the result
    result.sort()
    return result

# Recursive function, receives a sorted set of letters and returns all the subsets that can be formed from those letters    
def getSubsets(word):
    if len(word)==0: return ['']  
    else:
        count = 1                                   # count how many times the first letter appears
        while count < len(word)-1 and word[count-1] == word[count]:
            count+=1
        temp = getSubsets(word[count:])             # get subsets starting at the next different letter
        ret = list(temp)
        for j in xrange(0,count):                   # merge the result with the first letter, multiple times if it's a repeated letter
            for i in xrange(0,len(temp)):
                temp[i] = word[0] + temp[i]
                ret += [temp[i]]                    # and add the results to the return list
    return ret




    
#preprocessDictionary()                                 # this function needs to be called only once to create the anagrams file  
anagrams = loadAnagrams() 								# global variable, contains the dictionary of anagrams    
word = 'abcdefghijklmnopqr'
print jumble(word)


