# Project: Decryption

One form of encryption is a letter scramble. Every letter is replaced by a different letter. Unlike a Caesar cipher, there is not a pattern to the replacement. In order to decrypt such files, we can use the expected frequency of letters and words.

- [English word frequency](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/1-10000)
- [English letter frequency](https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html)

The most common letter is `e`.

The most common words by length are `a`, `I`, `of`, `to`, `the`, `and`, `that`, `with`, `have`, `from`, `this`, `which`, and `their`.

Additionally, there are words where if a letter is missing, there could only be one possible letter that completes the word. For example: a_ove could only be above. The decrypter uses a loop to continually search for such situations
given words with one unknown letter.

We have written the decryption part for you but it's missing all of the helper functions that make it work. We stored the decryption key in a dictionary which maps actual letters to their encrypted counterparts. This means that the helper functions need the list, dictionary and loops concepts we covered today.

### makeLetterDict()

Make a dictionary mapping lower case alphabet letters to 0.

A `0` indicates we don’t know which encrypted letter the real letter matches.

Uses: dictionaries, `list()`, `ord()`, `chr()`, `range()`, `in`, and a `for` loop.

Returns: `{ 'a':0, 'b':0, ... 'z':0 }`

Pseudo Code:
```
Get an empty dictionary
Loop thru the ascii values for the letters a thru z using ord and range
  Add the pair (letter, 0) to the dictionary
**Return** the dictionary
```

When you succeed, it will run as follows in the console prompt:
```bash
> makeLetterDict()
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
```

### countLetters()
Count the alphabet letters in a list of strings and return a dictionary mapping lower case letters to their corresponding counts. Upper case letters in the list get counted too (as lower case letters so T counts with t). Punctuation gets ignored.

**Inputs**
- `text` A list of words and some punctuation <br>Example: `['Hi!', 'This', 'is', 'a', 'text.']`

**Returns** a dictionary from a thru z which has the counts of each letter in the text input. Ignore the characters that are not letters. Treat all letters as lowercase so the dictionary has a key for `a` but not for `A`.

Example: `{ 'a':1, 'b':0, ... 't':3, ... 'z':0 }`

Pseudo code:
```
Get a letters dictionary mapping alphabet letters to 0
Loop thru the strings in the list
  Loop thru the letters in a string
    If the letter is in the alphabet
      Increment its (lower case) count in the dictionary by 1
```

When you succeed, it will run as follows in the console prompt:
```bash
> countLetters(['Hi!', 'This', 'is', 'a', 'text.'])
{'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 1, 'f': 0, 'g': 0, 'h': 2, 'i': 3, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 2, 't': 3,
'u': 0, 'v': 0, 'w': 0, 'x': 1, 'y': 0, 'z': 0}
```

### getMostPopularKey()
Get the most popular key in the dictionary.
Uses: dictionaries, loops, selection (if), and comparison (< > <= etc).

**Inputs:**
- `dict` a dictionary of keys to integer values. The key with the largest integer is the most popular.<br>
Example: `{ 'a':1, 'b':5, 't':3, 'z':2 }`

**Returns** a character that is the most popular key
Example: `b`

Pseudo code:
```
Set an integer value to None. We’ll put real values here when we learn some.
Set a string value to None. We’ll fill this in later as well.

Loop thru the keys in the dictionary.
  If the two values are None,
  give them the value of this key and its corresponding value.

  If this key’s value is higher than our collected value,
  set the two variables to be this key and its value.

Return the collected string. It’s the key that matches the highest value.
```

When you succeed, it will run as follows in the console prompt:
```bash
> getMostPopularKey( { 'a':1, 'b':5, 't':3, 'z':2 } )
'b'
> getMostPopularKey(countLetters(['Hi!', 'This', 'is', 'a', 'text.']))
'I' or 't' (because both were 23%)
```

### getPopularityList()
Get the list of dictionary keys ordered from most popular to least popular

Uses: dictionaries, lists, loops, range(), list(), len(), and dictionary and list functions

**Inputs:**
- `dict` a dictionary of keys to integer values. The key with the largest integer is the most popular.<br>
Example: `{ 'a':1, 'b':5, 't':3, 'z':2 }`

**Returns** a list of keys ordered from most to least popular.
example: `['b', 't', 'z', 'a']`

Pseudo code:
```
Make a copy of the dictionary using the copy() method. This is so we don’t harm the original dictionary.
Create an empty list.
Loop thru numbers values ranging from 0 to dictionary size (not including the dict size).
We use the ranged loop because we will be editing the dictionary as we go.
  Get the most popular key from the dictionary copy
  Add that key to your list
  Remove the key from your dictionary copy using del
Each time it loops, it removes the most popular key and we’ll find the next most popular on the next loop
Return the list
```

When you succeed, it will run as follows in the console prompt:
```bash
> getPopularityList({ 'a':1, 'b':5, 't':3, 'z':2 })
['b', 't', 'z', 'a']
> getPopularityList(countLetters(['Hi!', 'This', 'is', 'a', 'text.']))
['i', 't', 'h', 's', 'a', 'e', 'x', 'b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'u', 'v', 'w', 'y', 'z']
```
`countLetters()` started us with a full alphabet so that is why the list includes unused letters.

### cleanText()
Remove the punctuation and numbers and make all the letters lower case in the given text.

Uses: dictionaries, loops, and math (+, -, *, /).

**Inputs:**
- `text` A list of words and some punctuation<br>
Example: `['Hi!', 'This', 'is', 'a', 'text.']`

**Returns** nothing

Changes the given text so it is all lower case and has no punctuation or numbers
example: `[‘hi’, ‘this’, ‘is’, ‘a’, ‘text’]`

Pseudo code:
```
Make a string containing all things you want to remove (punctuation and numbers)
Loop thru a range of the length of the text (because we will be editing the text)
  Get the current word in lower case form
  Loop thru the characters in the unwanted string
    Remove each character from the word
    Replace the word in the text with this new, smaller, lowercase word
Nothing to return
```

When you succeed, it will run as follows:
```bash
> text = [‘!@#$%^&*()_+-={}|\\[]:";<>,.?/\'0123456789’]
> cleanText(text)
> print(text)
[ ]
> text = ['Hi!', 'This', 'is', 'a', 'text.']
> cleanText(text)
> print(text)
['hi', 'this', 'is', 'a', 'text']
```

### getUniqueWords()
Remove the duplicate words from a text.

Uses: lists, loops, selection (if), not, in, and lower().

**Inputs:**
- `text` A list of words and some punctuation<br>
Example: `['hello', 'hello', 'hello', 'is', 'there', 'anybody', 'out', 'there', 'out', 'there']`

**Returns** a list of words with duplicates removed<br>
Example: `['hello', 'is', 'there', 'anybody', 'out']`

Pseudo Code:
```
Get an empty list
Loop thru the text
  If the word (in lower case) is not in our new list, put it there
Return the new list
```

When you succeed, it will run as follows in the console prompt:
```bash
> getUniqueWords(['hello', 'hello', 'hello', 'is', 'there', 'anybody', 'out', 'there', 'out', 'there'])
['hello', 'is', 'there', 'anybody', 'out', 'there']
```

### getWordFrequencies()
Remove the duplicate words from a text

Uses: lists, dictionaries, loops, and selection (if), in, lower().

**Inputs:**
- `text` A list of words. Assume it is lower case with no punctuation.<br>
Example: ['hello', 'hello', 'hello', 'is', 'there', 'hello', 'anybody', 'hello', 'out', 'there', 'out', 'there']

**Returns** a dictionary mapping each word in the text to its number of occurrences<br>
Example: `{ ‘hello’:5, ‘is’:1, ‘there’:3, ‘anybody’:1, ‘out’:2 }`

Pseudo code:
```
Get an empty dictionary
Loop thru the words in the text
  If a word is not already in the dictionary, put it there with a count of 1
  Otherwise increase its count by 1
Return the dictionary
```

When you succeed, it will run as follows in the console prompt:
```bash
> getWordFrequencies(['hello', 'hello', 'hello', 'is', 'there', 'hello', 'anybody', 'hello', 'out', 'there', 'out', 'there'])
{ 'hello': 5, 'is': 1, 'there': 3, 'anybody': 1, 'out': 2 }
```

### getFreqByLen()
Remove the duplicate words from a text

Uses: dictionaries and loops

Inputs:
- `dict` a dictionary mapping strings to numbers<br>
Example: `{ 'hello': 5, 'is': 1, 'there': 3, 'anybody': 1, 'out': 2 }`
- `length` an integer<br>
example: `3`

**Returns** a new dictionary with only the key,value pairs where the key was the given length
example: `{ 'out': 2 }`

Pseudo code:
```
Get an empty dictionary
Loop thru the keys in the dictionary
  If the key has the desired length, add its key,value pair to the new dictionary
Return the new dictionary
```

When you succeed, it will run as follows in the console prompt:
```bash
> getFreqByLen(['hello', 'hello', 'hello', 'is', 'there', 'hello', 'anybody', 'hello', 'out', 'there', 'out', 'there'], 1)
{}

> getFreqByLen(['hello', 'hello', 'hello', 'is', 'there', 'hello', 'anybody', 'hello', 'out', 'there', 'out', 'there'], 2)
{ 'is': 1 }

> getFreqByLen(['hello', 'hello', 'hello', 'is', 'there', 'hello', 'anybody', 'hello', 'out', 'there', 'out', 'there'], 5)
{'hello': 5, 'there': 3}
```
