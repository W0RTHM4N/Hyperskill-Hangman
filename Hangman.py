import random
from string import ascii_lowercase

words = ('python', 'java', 'kotlin', 'javascript')
correct_word = random.choice(words)
letters = set(correct_word)
tried_letters = set()
hint = "-" * (len(correct_word))
tries = 8

print("H A N G M A N")

while True:
    action = input('Type "play" to play the game, "exit" to quit: ')
    
    if action == "exit": 
        break
    if action != "play":
        continue

    while tries > 0:
    
        print()
        print(hint)
        guess = input("Input a letter: ")
    
        if len(guess) != 1:
            print("You should input a single letter")
            continue
    
        if guess not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
            continue
            
        if guess in letters:
            letters.remove(guess)
            hint = correct_word
        
            for letter in letters:
                hint = hint.replace(letter, "-")
    
        elif guess in tried_letters:
            print("You already typed this letter")
        
        else:
            print("No such letter in the word")
            tries -= 1
    
        tried_letters.add(guess)
    
        if "-" not in hint:
            break

    if "-" in hint:
        print("You are hanged!")
    else:
        print("""You guessed the word!
        You survived!""")
