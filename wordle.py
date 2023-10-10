import random

# next steps: had a check to handle when a user inputs a word shorter or longer than 5 letters=

def game_instructions():
    print("""
Wordle is a game in which you need to guess a five letter hidden word. You will have 6 attempts.
After each attempt, the game will tell you which letters in your guess are correct or incorrect.

- 'X' indicates that the letter used is not in the hidden word.
- 'O' indicates that letter used is in the hidden word and at the correct position.
- '*' indicates that the letter used is in the hidden word but in the wrong position.
    """)


def get_words():
    # Load the file.
    with open('sgb-words.txt','r') as f:
        ## This includes \n at the end of each line:
        #words = f.readlines()

        # This drops the \n at the end of each line:
        words = f.read().splitlines()

    return words


def display_indications(guess):
    display = (guess[0] + ' ' + indications[0] + '\n' +
               guess[1] + ' ' + indications[1] + '\n' +
               guess[2] + ' ' + indications[2] + '\n' +
               guess[3] + ' ' + indications[3] + '\n' +
               guess[4] + ' ' + indications[4] + row)
    print(display)


def checkword(guess, hidden_word):
    for k in range(5):
        if guess == hidden_word:
            return True
        elif guess[k] == hidden_word[k]:
            indications[k] = 'O'
        elif guess[k] in hidden_word:
            indications[k] = '*'
        else:
            indications[k] = 'X'


def play_game():
    hidden_word = random.choice(words)
    for turn in range(1, 7):
        guess = input("Attempt {}: \n".format(turn))
        if checkword(guess, hidden_word):
            print("Correct! You win :D")
            break
        checkword(guess, hidden_word)
        display_indications(guess)
    else:
        print("You ran out of attempts... You lost!\n The hidden word was: ", hidden_word)


words = get_words()
row = '\n' + '-' * 5
indications = {0: ' ', 1: ' ', 2: ' ', 3: ' ', 4: ' '}

game_instructions()
play_game()
