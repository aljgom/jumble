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
 
# Wrapper function, sets the lists to call recursive function, and prints the result    
def jumble2(word):
    global unique, result
    result =[]
    word = list(word)	                    # sort letters
    word.sort()
    unique = [word[0]]                      # will countain a list of each different character
    charcount = [1]                         # list of how many times each character repeats
    for i in xrange(1,len(word)):           # fill up unique and charcount
        if word[i] != word[i-1]:
            unique.append(word[i])
            charcount.append(1)
        else: charcount[-1] += 1  
    _jumble2(charcount,[''])
    result.sort()
    print result
	
# Recursive function to find all permutations of
# all subsets of the set of letters (represented in unique and charcount)
# finds if any combination is an english word
def _jumble2(charcount,prefix):
    global unique, result 
    for i in xrange(0,len(unique)):         # for every unique letter
        if charcount[i] > 0:
            prefix.append(unique[i])        # add the next unique available letter to the word
            charcount[i] -=1                # substract the count for that letter
            if "".join(prefix) in worddict: # we get one result. Compare with the dictionary to see if it's an English word
                result += ["".join(prefix)]
                print "".join(prefix)
            _jumble2( charcount,prefix)     # use recursion with the remaining characters
            charcount[i]+=1                 # remove the letter and increase it's counter
            prefix.pop()                    
    

# Wrapper function, sets the lists to call recursive function, and prints the result  
def jumble3(word):
    global unique
    word = list(word)	                    # sort letters
    word.sort()
    unique = [word[0]]                      # will countain a list of each different character
    charcount = [1]                         # list of how many times each character repeats
    for i in xrange(1,len(word)):           # fill up unique and charcount
        if word[i] != word[i-1]:
            unique.append(word[i])
            charcount.append(1)
        else: charcount[-1] += 1
    result=[]
    testwords = _jumble3(charcount)
    for w in testwords:
        if w in worddict:result+=[w]
    result.sort()
    print result
 
# Recursive function, returns all permutations of
# all subsets of the set of letters (represented in unique and charcount)
def _jumble3(charcount):
    global unique, memo
    key =0
    for i in xrange(0,len(unique)):         # make a key for the dictionary
        key *=10
        key += charcount[i] 
    if key in memo : return list(memo[key]) # if the value has already been calculated, return it
    ret=[]
    temp=[]
    for i in xrange(0,len(unique)):         # for each available letter
        if charcount[i] > 0:
            ret += [unique[i]]
            charcount[i] -=1
            temp = _jumble3( charcount)     # user recursion with remainig letters
            for j in xrange(0,len(temp)):
                temp[j]= unique[i] +temp[j] # add new letter to the result
            ret += temp                     # add result to return list
            charcount[i] +=1
    memo[key] = list(ret)		    # store the result to have it ready if the function is called again with the same value
    return ret



# Read the list of english words from the file into the worddict list
f = open('wordlist.txt','r')
worddict = []					
for line in f:
    worddict+=[line[0:-1]]
    
unique =[]
result =[]
memo = {}		# is a dictionary of return values for the _jumble3 function

word = 'ablebcd'
print 'Running jumble2'
jumble2(word)
print 'Running jumble3'
jumble3(word)



