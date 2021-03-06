# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    k=0
    for char in secret_word:
      if char not in letters_guessed:
        k=1
        break
    if k==0:
      return True
    if k==1:
      return False 
    # FILL IN YOUR CODE HERE AND DELETE "pass"



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    k = ''
    for char in secret_word:
      if char not in letters_guessed:
        char = '_ '
      k = k+char
    return k      



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    k= ''
    a = string.ascii_lowercase
    for i in a:
      if i not in letters_guessed:
        k = k+i
    return k



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warn = 3
    gues = 6
    l_g=[]
    word = choose_word(wordlist)
    print("Welcome to the game Hangman!\nI'm thinking of a word that is",len(word),"letters long\n-------------")
    i=0
    print("You have ",warn," warnings left.")
    while i!=1:
      print("You have ",gues," guesses left.\nAvailable letters:",get_available_letters(l_g))
      try:
        vvk = input("Please guess a letter: ")
        if vvk.isalpha() == False:
          raise ValueError
        vvk = vvk.lower()
        if vvk in l_g:
          print("Oops! You've already guessed that letter.")
          if warn>=1:
            warn -=1
            print("You have ",warn," warnings left.",get_guessed_word(word,l_g),"\n------------")
          elif gues>1:
            gues -=1
            print("You have no warnings left.",get_guessed_word(word,l_g),"\n------------")
          else:
            i=1
        else:
          l_g.append(vvk)
          if vvk in word:
            print("Good guess:",get_guessed_word(word,l_g),"\n------------")
            if is_word_guessed(word,l_g)==True:
              score = gues*(len(word))
              print("Congratulations, you won! Your total score for this game is:",score)
              break
          else:
            if vvk=='a' or vvk=='e' or vvk=='i' or vvk=='o' or vvk=='u':
              if gues>2:
                print("Oops! That letter is not in my word.",get_guessed_word(word,l_g),"\nPlease guess a letter: ",get_available_letters(l_g),"\n------------")
                gues -=2
              else:
                i=1
                print("Sorry, you ran out of guesses. The word was",word)
            else:
              if gues>1:
                print("Oops! That letter is not in my word.",get_guessed_word(word,l_g),"\nPlease guess a letter: ",get_available_letters(l_g),"\n------------")
                gues -=1
              else:
                i=1
                print("Sorry, you ran out of guesses. The word was",word)
      except ValueError:
        print("Oops! That is not a valid letter.",end='')
        if warn>=1:
          warn -=1
          print(" You have",warn,"warnings left:",get_guessed_word(word,l_g))
        elif gues>1:
          gues -= 1
          print(" You have no warnings left:",get_guessed_word(word,l_g))
        else:
          i=1
          print(" Sorry, you ran out of guesses. The word was",word)
        

      



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    if len(my_word)!=len(other_word):
      return False
    else:
      ll=[]
      for i in range(0,len(my_word)):
        if my_word[i]=="_":
          ll.append(other_word[i])
        elif my_word[i] in ll:
          return False
        elif my_word[i]!=other_word[i]:
          return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    k1=0
    my_word = my_word.replace(" ", "")
    for w in wordlist:
      if match_with_gaps(my_word,w)==True:
        print(w,end=" ")
        k1+=1
    if k1==0:
      print("No matches found.")
    else:
      print()



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warn = 3
    gues = 6
    l_g=[]
    word = choose_word(wordlist)
    print("Welcome to the game Hangman!\nI'm thinking of a word that is",len(word),"letters long\n-------------")
    i=0
    print("You have ",warn," warnings left.")
    while i!=1:
      print("You have ",gues," guesses left.\nAvailable letters:",get_available_letters(l_g))
      try:
        vvk = input("Please guess a letter: ")
        if vvk=="*":
          show_possible_matches(get_guessed_word(word,l_g))
          continue
        elif vvk.isalpha() == False:
          raise ValueError
        vvk = vvk.lower()
        if vvk in l_g:
          print("Oops! You've already guessed that letter.")
          if warn>=1:
            warn -=1
            print("You have ",warn," warnings left.",get_guessed_word(word,l_g),"\n------------")
          elif gues>1:
            gues -=1
            print("You have no warnings left.",get_guessed_word(word,l_g),"\n------------")
          else:
            i=1
        else:
          l_g.append(vvk)
          if vvk in word:
            print("Good guess:",get_guessed_word(word,l_g),"\n------------")
            if is_word_guessed(word,l_g)==True:
              score = gues*(len(word))
              print("Congratulations, you won! Your total score for this game is:",score)
              break
          else:
            if vvk=='a' or vvk=='e' or vvk=='i' or vvk=='o' or vvk=='u':
              if gues>2:
                print("Oops! That letter is not in my word.",get_guessed_word(word,l_g),"\nPlease guess a letter: ",get_available_letters(l_g),"\n------------")
                gues -=2
              else:
                i=1
                print("Sorry, you ran out of guesses. The word was",word)
            else:
              if gues>1:
                print("Oops! That letter is not in my word.",get_guessed_word(word,l_g),"\nPlease guess a letter: ",get_available_letters(l_g),"\n------------")
                gues -=1
              else:
                i=1
                print("Sorry, you ran out of guesses. The word was",word)
      except ValueError:
        print("Oops! That is not a valid letter.",end='')
        if warn>=1:
          warn -=1
          print(" You have",warn,"warnings left:",get_guessed_word(word,l_g))
        elif gues>1:
          gues -= 1
          print(" You have no warnings left:",get_guessed_word(word,l_g))
        else:
          i=1
          print(" Sorry, you ran out of guesses. The word was",word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
