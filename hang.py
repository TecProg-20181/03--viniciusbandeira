"""This module implements a hangman game"""
import random
import string

WORDLIST_FILENAME = "palavras.txt"


def load_words(file_name):
    """Load all words of file and randomly select a word

        :param file_name: Name of text file
        :type file_name: str
        :returns: str without blanc spaces
        :rtype: str

        .. note::
            Depending on the size of the word list, this function may take a while to finish.
    """
    print "Loading word list from file..."

    in_file = open(file_name, 'r', 0)

    line = in_file.readline()

    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    """Verify if all letters_guessed is in secret_word

        :param secret_word: Word useed in hang game
        :param letters_guessed: Word submited by the player
        :type letters_guessed: str
        :type secret_word: str
        :returns: If all letters_guessed is in secret_word is True
        :rtype: bool
    """
    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
            return False

    return True


def get_available_letters():
    """Return a string of the available letters of ascII pattern

    :returns: The string 'abcdefghijklmnopqrstuvwxyz'
    :rtype: str
    """
    available = string.ascii_lowercase

    return available


def hangman(secret_word, guesses):
    """Iniciate a hangman game, the closes when user
    submit all letters of secret_word or miss the
    letter zeroing the value of gesses left

        :param secret_word: A word will be used in hang game
        :param guesses: Number of max wrong guesses
        :type secret_word: str
        :type guesses: int
        :returns: Do not return nothing

        .. todo::
            - Modulate this function
    """

    letters_guessed = []
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secret_word), ' letters long.'
    print '-------------'

    while is_word_guessed(secret_word, letters_guessed) is False \
            and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        available = get_available_letters()
        for letter in available:
            if letter in letters_guessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in letters_guessed:

            guessed = ''
            for letter in secret_word:
                if letter in letters_guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secret_word:
            letters_guessed.append(letter)

            guessed = ''
            for letter in secret_word:
                if letter in letters_guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            guesses -= 1
            letters_guessed.append(letter)

            guessed = ''
            for letter in secret_word:
                if letter in letters_guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ', guessed
        print '------------'

    else:
        if is_word_guessed(secret_word, letters_guessed) is True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ',\
            secret_word, '.'


def main():
    """Function wtih run this module"""
    secret_word = load_words(WORDLIST_FILENAME).lower()
    hangman(secret_word, 8)


if __name__ == '__main__':
    main()
