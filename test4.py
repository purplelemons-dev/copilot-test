
# Will generate a word that rhymes with user input and has the same number of syllables


import sys
import random


def get_rhymes(word):
    # Get a list of words that rhyme with the user input
    words = []
    # Get the last two letters of the user input
    last_two = word[-2:]
    # Get a list of words that end with the last two letters of the user input
    for line in open("/usr/share/dict/words"):
        if line.strip()[-2:] == last_two:
            words.append(line.strip())
    # Return the list of words that rhyme with the user input
    return words


def count_syllables(word):
    # Get the number of vowels in the word
    vowels = "aeiouy"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    # Return the number of vowels in the word
    return count


def macthing_syllables(word, rhymes):
    matches=[]
    for rhyme in rhymes:
        if count_syllables(word) == count_syllables(rhyme):
            matches.append(rhyme)
    return matches


def main():
    # Get user input
    word = input("Enter a word: ")
    # Get a list of words that rhyme with the user input
    words = get_rhymes(word)
    # If there are no words that rhyme with the user input
    if not words:
        # Print an error message
        print("No words found")
        # Exit the program
        sys.exit(1)
    # Get a list of words that rhyme with the user input and have the same number of syllables
    matches = macthing_syllables(word, words)
    # Print a random matching word
    print(random.choice(matches))


# Loop forever
while True:
    main()
