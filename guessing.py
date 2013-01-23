from random import randint

def guessNumber():
    random_number = str(randint(1,101))
    print random_number
    print "Welcome to guess-a-number! Type 'exit' to quit."
    gameOn = True
    counter = 1
    guess = raw_input("Enter a number between 1 and 100. >> ")
    while gameOn:
        if guess == "" or int(guess) < 1 or int(guess) > 101:
            guess = raw_input("Please enter a valid number between 1 and 100. >> ")
        elif guess == "exit":
            gameOn = False
        else:
            if guess == random_number:
                    if counter == 1:
                        print "You win! It only took %d guess! Outstanding!" % counter
                        gameOn = False
                    else:
                        print "You win! It took %d guesses!" % counter
                        gameOn = False
            elif guess > random_number:
                guess = raw_input("Too high, guess again! >> ")
                counter += 1
            else:
                guess = raw_input("Too low, guess again! >> ")        
                counter += 1
guessNumber()
