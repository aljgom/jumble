Jumble
====================
##Instructions 
Can you create a program to solve a word jumble?  
([More info here.](http://en.wikipedia.org/wiki/Jumble))  The program should accept a string 
as input, and then return a list of words that can be
created using the submitted letters.  For example, on
the input "dog", the program should return a set of 
words including "god", "do", and "go".
 
Please implement the program in Python but refrain
from using any helper modules or imports (e.g. itertools). 
In order to verify your words, just download an 
English word list.

##Implementation
The file `jumble.py` contains the first implementations of the solution.

The function `jumble2(word)` solves the problem by finding every permutation of 
every subset of the provided letters. It does so efficiently, without creating 
unnecessary calculations when there's repeated characters, and using little memory

The function `jumble3(word)` is similar to `jumble2(word)` but it uses memoization
to increase speed. It is quite faster than `jumble2(word)`, but it uses a lot of memory
(exponential)

In the end, even though `jumble3(word)` finds all the possible permutations a lot faster,
both functions end up taking about the same amount of time after looking for each word in the 
dictionary

We need something FASTER!

##Better Solution
The file `jumble_fast.py` uses a different approach. It pre processes the words file,
by grouping all the words that are anagrams with each other, and creating a dictionary
of anagrams, each key is a set of letter and the value is a list with all the anagrams
from that set of letters. We need to do this only once, so we save the resulting 
dictionary on a file for any future use of the program

Then the function `jumble(word)` needs to only find all the subsets of its input string,
and it's not necessary to find all the permutations of each of the subsets.

We compare each of the subsets with the dictionary of anagrams, and if we find a match
we add all the words from the entry to the result list.

This method performs at O(2^n) time, but it's much faster than the other 2 previous methods





