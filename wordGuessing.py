import random

def main():
    # Opening wordlist file supplied by the customer
    # TODO need to add filtering to our file reading
    file = open("wordlist", "r")
    allTheLinesIfTheFile = file.readlines()
    file.close()

    # selecting a word at random
    selectedWord = allTheLinesIfTheFile[random.randint(0, len(allTheLinesIfTheFile) - 1)].strip()
    # selectedWord = "process"
    attempts = 2
    truthTracker = False
    winningTracker = False

    scoreCorrect = 10
    scoreIncorrect = -15
    scoreCurrent = 0

    # Creating our mask, its gonna be as long as the selectedword is
    mask = []
    for char in selectedWord:
        mask.append(False)

    # Game loop, will not end until attemps are 0 or if they won the game
    while attempts != 0 and not winningTracker:
        # Printing attempts left
        print("You have {} attempts left".format(attempts))
        print(scoreCurrent)

        # Printing out an _ or a char based on the mask value
        for index, char in enumerate(selectedWord):
            # If true, then print the character
            if mask[index]:
                print(char, end=" ")
            else:
                print("_", end=" ")
        print()

        # guessing out character
        userInput = input("Guess a character > ")

        # Checking if they gave us bad input
        if len(userInput) > 1 or not userInput.isalpha():
            print("You gave bad input, bad, bad person")
            continue

        # Checking if they guess a char correctly
        for index, char in enumerate(selectedWord):
            if userInput == char:
                mask[index] = True
                truthTracker = True
                scoreCurrent = scoreCurrent + scoreCorrect

        # Our logic for seeing if the game has been won or not
        for item in mask:
            if not item:
                winningTracker = False
                break
            else:
                winningTracker = True

        # If they guessed incorrectly, deduct an attempt
        if not truthTracker:
            attempts = attempts - 1
            scoreCurrent += scoreIncorrect
            # scoreCorrect = scoreCorrect + scoreIncorrect

    # Printing if we won or not
    if winningTracker:
        print("You won!")
    else:
        print("You lost!")

    name = ""
    while not name.isalpha():
        print("Enter name to be saved on the highscore list")
        name = input("Enter > ")

        if not name.isalpha():
            print("You have me bad bad input")

    file = open("saved", "a")
    file.write("{},{}".format(name, scoreCurrent))
    file.close()


if __name__ == "__main__":
    main()