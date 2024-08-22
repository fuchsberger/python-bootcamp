from decipher import *

# Put all your code here

# You may (and should) run your tests using this shell command:
# python -m unittest

def makeLetterDict():
    # a --> 97
    # z --> 122
    # Get an empty dictionary
    d = {}
    # Loop thru the ascii values for the letters a thru z using ord and range
    for ascii in range(97, 123):
        # Add the pair (letter, 0) to the dictionary
        d[chr(ascii)] = 0

    # Return the dictionary
    return d


def countLetters(words):
    # Get a letters dictionary mapping alphabet letters to 0
    d = makeLetterDict()

    # Loop thru the strings in the list
    for word in words:
        # Loop thru the letters in a string
        for c in word:
            # ensure character is lower case if it is a letter
            c = c.lower()
            # Increment its (lower case) count in the dictionary by 1
            if (ord(c) > 96 and ord(c) < 123):
                d[c] += 1

    # Return the dictionary
    return d

def getMostPopularKey(d):
    # Set an integer value to None. We’ll put real values here when we learn some.
    max = None
    # Set a string value to None. We’ll fill this in later as well.
    letter = None

    # Loop thru the keys in the dictionary.
    for c, count in d.items():
        # If the two values are None,
        # give them the value of this key and its corresponding value.
        if max == None and letter == None:
            max = count
            letter = c

        # If this key’s value is higher than our collected value,
        # set the two variables to be this key and its value.
        if count > max:
            max = count
            letter = c

    # Return the collected string. It’s the key that matches the highest value.
    return letter


def getPopularityList(dic):
    # Make a copy of the dictionary using the copy() method. This is so we don’t harm the original dictionary.
    d = dic.copy()
    # Create an empty list.
    l = []
    # Loop thru numbers values ranging from 0 to dictionary size (not including the dict size).
    # We use the ranged loop because we will be editing the dictionary as we go.
    for i in range(len(d)):
        #   Get the most popular key from the dictionary copy
        k = getMostPopularKey(d)
        #   Add that key to your list
        l.append(k)
        #   Remove the key from your dictionary copy using del
        del d[k]

        # Each time it loops, it removes the most popular key and we’ll find the next most popular on the next loop
    # Return the list
    return l


def cleanText(text):
    # Make a string containing all things you want to remove (punctuation and numbers)
    unwanted = "!@#$%^&*()_+-={}|\\[]:\";<>,.?/\'0123456789"

    # Loop thru a range of the length of the text (because we will be editing the text)
    for i in range(len(text)):
        #   Get the current word in lower case form
        word = text[i]

        #   Loop thru the characters in the unwanted string
        for c in unwanted:
            # Remove each character from the word
            word = word.replace(c, "")

            # Replace the word in the text with this new, smaller, lowercase word
            word = word.lower()

            text[i] = word

    # Nothing to return


def getUniqueWords(text):
    # Get an empty list
    l = []
    # Loop thru the text
    for word in text:
        # If the word (in lower case) is not in our new list, put it there
        if not word in l:
            l.append(word)
    # Return the new list
    return l


def getWordFrequencies(text):
    # Get an empty dictionary
    d = {}
    # Loop thru the words in the text
    for word in text:
        # If a word is not already in the dictionary, put it there with a count of 1
        if word not in d:
            d[word] = 1
        # Otherwise increase its count by 1
        else:
            d[word] += 1
    # Return the dictionary
    return d


def getFreqByLen(dic, length):
    # Get an empty dictionary
    d = {}
    # Loop thru the keys in the dictionary
    for key in dic:
        # If the key has the desired length, add its key, value pair to the new dictionary

        if len(key) == length:
            d[key] = dic[key]

    # Return the new dictionary
    return d
