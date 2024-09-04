"""
Rhys Riggle
11/25/23 thru 11/29/23

Final Project - playing hangman w/ the computer ig?
- file w/ all possible words and hints (50 per level, 150 for random)
- computer prompts user to guess a letter, results in either true or false statement
- create class to guess word
"""
import random
class Hangman:
    def __init__(self, difficulty):
        self.difficulty = "" + difficulty
        if self.difficulty == "e":
            file = open("Words and Descs (Easy).txt", "r")
            self.words = []
            count = 1
            for line in file.readlines():
                count += 1
                if count % 2 == 0: #returns ever other line in the doc (the words, not the descs)
                    self.words.append(line.strip()) #gets rid of \n
            word_to_guess = random.randint(0, len(self.words[::])) #returns random number for random word in "words" list
            self.word_to_guess = self.words[word_to_guess]
            file.close()

        elif self.difficulty == "n":
            file = open("Words and Descs (Avg).txt", "r")
            self.words = []
            count = 1
            for line in file.readlines():
                count += 1
                if count % 2 == 0:
                    self.words.append(line.strip())
            word_to_guess = random.randint(0, len(self.words[::]))
            self.word_to_guess = self.words[word_to_guess]
            file.close()

        elif self.difficulty == "h":
            file = open("Words and Descs (Hard).txt", "r")
            self.words = []
            count = 1
            for line in file.readlines():
                count += 1
                if count % 2 == 0:
                    self.words.append(line.strip())
            word_to_guess = random.randint(0, len(self.words[::]))
            self.word_to_guess = self.words[word_to_guess]
            file.close()

        elif self.difficulty == "" or self.difficulty == "r": #if the input is accidentally (or purposefully) left blank, game defaults to random mode
            file = open("Words and Descs (Rndm).txt", "r")
            self.words = []
            count = 1
            for line in file.readlines():
                count += 1
                if count % 2 == 0:
                    self.words.append(line.strip())
            word_to_guess = random.randint(0, len(self.words[::]))
            self.word_to_guess = self.words[word_to_guess]
            file.close()

    def get_word(self): #bc we need to know what word it is
        return self.word_to_guess
    
    def set_new_word(self, new_difficulty): #why someone would use this, idk, we'll figure that out later ig. just resets the difficulty and sets a new word (not avoiding repeats oops)
        self.difficulty = new_difficulty
        if self.difficulty == "e":
             file = open("Words and Descs (Easy).txt", "r")
             words = []
             count = 1
             for line in file.readlines():
                count += 1
                if count % 2 == 0:
                    words.append(line.strip())
             word_to_guess = random.randint(0, len(words[::]))
             self.word_to_guess = words[word_to_guess]
             file.close()
        
        elif self.difficulty == "n":
            file = open("Words and Descs (Avg).txt", "r")
            words = []
            count = 1
            for line in file.readlines():
                count += 1
                if count % 2 == 0:
                    words.append(line.strip())
            word_to_guess = random.randint(0, len(words[::]))
            self.word_to_guess = words[word_to_guess]
            file.close()

        elif self.difficulty == "h":
            file = open("Words and Descs (Hard).txt", "r")
            words = []
            count = 1
            for line in file.readlines():
                count += 1
                if count % 2 == 0:
                    words.append(line.strip())
            word_to_guess = random.randint(0, len(words[::]))
            self.word_to_guess = words[word_to_guess]
            file.close()

        elif self.difficulty == "r" or self.difficulty == "":
            file = open("Words and Descs (Rndm).txt", "r")
            words = []
            count = 1
            for line in file.readlines():
                count += 1
                if count % 2 == 0:
                    words.append(line.strip())
            word_to_guess = random.randint(0, len(words[::]))
            self.word_to_guess = words[word_to_guess]
            file.close()

    def get_word_desc(self): #how am I gonna get the hint T-T EDIT: Figured out how to get the hint :)
        if self.difficulty == "e":
            file = open("Words and Descs (Easy).txt", "r")
            hint_list = []
            count = 0
            hint_index_num = self.words.index(self.word_to_guess)
            for line in file.readlines():
                 count += 1
                 if count % 2 == 0:
                    hint_list.append(line.strip())
            self.hint = hint_list[hint_index_num]
            file.close()
            return self.hint
        
        elif self.difficulty == "n":
            file = open("Words and Descs (Avg).txt", "r")
            hint_list = []
            count = 0
            hint_index_num = self.words.index(self.word_to_guess)
            for line in file.readlines():
                 count += 1
                 if count % 2 == 0:
                    hint_list.append(line.strip())
            self.hint = hint_list[hint_index_num]
            file.close()
            return self.hint
        
        elif self.difficulty == "h":
            file = open("Words and Descs (Hard).txt", "r")
            hint_list = []
            count = 0
            hint_index_num = self.words.index(self.word_to_guess)
            for line in file.readlines():
                 count += 1
                 if count % 2 == 0:
                    hint_list.append(line.strip())
            self.hint = hint_list[hint_index_num]
            file.close()
            return self.hint
        
        elif self.difficulty == "r" or self.difficulty == "":
            file = open("Words and Descs (Rndm).txt", "r")
            hint_list = []
            count = 0
            hint_index_num = self.words.index(self.word_to_guess)
            for line in file.readlines():
                 count += 1
                 if count % 2 == 0:
                    hint_list.append(line.strip())
            self.hint = hint_list[hint_index_num]
            file.close()
            return self.hint
    
    def __str__(self):
        return self.get_word()

class Strike: #was originally a bunch of functions, figured it would be easier to make a class
    def __init__(self, strike_count):
        self.strike_count = 0 + strike_count

    def strike(self):
        if self.strike_count == 1:
            return "_________\n|    |\n|    0\n|\n|\n|________\n"
        elif self.strike_count == 2:
            return "_________\n|    |\n|    0\n|   / \n|\n|________\n"
        elif self.strike_count == 3:
            return "_________\n|    |\n|    0\n|   / \ \n|\n|________\n"
        elif self.strike_count == 4:
            return "_________\n|    |\n|    0\n|   /|\ \n|\n|________\n"
        elif self.strike_count == 5:
            return "_________\n|    |\n|    0\n|   /|\ \n|   /\n|________\n"
        elif self.strike_count == 6:
            return "_________\n|    |\n|    0\n|   /|\ \n|   / \ \n|________\n"
        else:
            return "_________\n|    |\n|\n|\n|\n|________\n"
        
    def get_strike_count(self):
        return self.strike_count
    
    def __str__(self):
        return self.strike()

#actually starting something!
print("Welcome to Hangman!")
print("Select your difficulty: Easy (e), Normal (n), Hard (h), Random (r)") #normal = avg difficulty #if they don't type letters im screwed lmao
difficulty = input()
word = Hangman(difficulty)

print(Strike(0)) 

strike_count = 0 #how many times they get the letter wrong. 6 = game over rip
letter_guessed_list =[] #keeps track of what letters user guessses so no repeats
word_to_guess_list_og = [] #the og (the one everyone's compared to)
for letter in word.get_word():
    word_to_guess_list_og.append(letter)

word_to_guess_list_dash = [] #the one that's constantly comparing itself to the og
for letter in word.get_word():
    word_to_guess_list_dash.append("_")

word_to_guess_list_new = [] #list the user edits #the one always changing itself to be like the og
word_dash_str = "".join(word_to_guess_list_dash)
print(word_dash_str)

print(f"Guess a letter!\n(Type 'hint' for a hint or 'quit' to quit)") #starting the game before entering the loop
letter_guessed = input()
letter_guessed_list.append(letter_guessed)

if letter_guessed in word_to_guess_list_og:
    for letter in word_to_guess_list_og[::]:
        if letter_guessed == letter:
            word_to_guess_list_new.append(letter)
        elif letter_guessed in word_to_guess_list_og:
            word_to_guess_list_new.append("_")
            word_to_guess_list_dash = word_to_guess_list_new
    print(Strike(strike_count))

else:
    strike_count += 1
    if strike_count == 1:
        print(Strike(strike_count))
    word_to_guess_list_dash = word_to_guess_list_new

if letter_guessed == "hint":
        letter_guessed = ""
        print(word.get_word_desc(), "\n")
        if "hint" in letter_guessed_list:
            letter_guessed_list.remove("hint")

word_guess_str = "".join(word_to_guess_list_new)
print(f"Letters guessed:\n", ", ".join(letter_guessed_list), "\n")
print("".join(word_to_guess_list_new))


while word_to_guess_list_og != word_to_guess_list_dash:#idk if I still need this first while loop but I couldn't get the code to work properly w/out it :')
    while letter_guessed != "quit":
        while letter_guessed != "hint":
            print(f"Guess a letter!\n(Type 'hint' for a hint or 'quit' to quit)")
            letter_guessed = input()
            word_to_guess_list_new = []
            letter_guessed_list.append(letter_guessed)

            if letter_guessed in word_to_guess_list_og: #repeat or correct letter #wow branching central
                for letter in word_to_guess_list_og[::]:
                    if letter_guessed == letter:
                        word_to_guess_list_new.append(letter)
                    elif letter in letter_guessed_list:
                        word_to_guess_list_new.append(letter)
                    elif letter in word_to_guess_list_og:
                        word_to_guess_list_new.append("_")
                word_to_guess_list_dash = word_to_guess_list_new

            elif letter_guessed not in word_to_guess_list_og: #incorrect letter
                strike_count += 1
                for letter in word_to_guess_list_og:
                    word_to_guess_list_new.append("_")

            if 1 <= strike_count < 6: #strike count is here ig? i feel like it doesn't fit here, but the code runs fine so...
                    print(Strike(strike_count))
            elif strike_count == 6:
                    print(Strike(strike_count))
                    print(f"Letters guessed:\n", ", ".join(letter_guessed_list), "\n")
                    print("".join(word_to_guess_list_dash))
                    print("The word was: ", word)
                    print(f"Game Over!\nThanks for playing!")
                    exit()
            else:
                print(Strike(0))

            if letter_guessed == word.get_word(): #other people guess words when playing hangman, right?
                print(f"Letters guessed:\n", ", ".join(letter_guessed_list), "\n")
                print(word)
                print("You win! Congrats!\nRestart the program to play again!")
                exit()
            
            
            if word_to_guess_list_dash != word_to_guess_list_og:
                print(f"Letters guessed:\n", ", ".join(letter_guessed_list), "\n")
                print("".join(word_to_guess_list_dash))
            elif word_to_guess_list_dash == word_to_guess_list_og: #bc the outside most while loop doesn't work to end the game
                print(f"Letters guessed:\n", ", ".join(letter_guessed_list), "\n")
                print("".join(word_to_guess_list_dash))
                print("You win! Congrats!\nRestart the program to play again!")
                exit()
        
        if letter_guessed == "hint":
            letter_guessed = ""
            strike_count -= 1 #hints shouldn't count for strikes 
            print(word.get_word_desc(), "\n")
            if "hint" in letter_guessed_list: #idk i just dont think hint should be hanging out with the guessed letters
                letter_guessed_list.remove("hint")

    if letter_guessed == "quit":
        print("Thanks for playing!")
        exit()

if word_to_guess_list_og == word_to_guess_list_dash: #still don't know why this is here, but code still won't work w/out it
        print("You win! Congrats!\nRestart the program to play again!")