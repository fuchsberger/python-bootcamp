from decipher import *
from support import *

actual = makeLetterDict()
verbose = False

def checkOfTo(x, y):
    if known('o',actual): return
    # Try words x:of and y:to?
    if x[0] == y[1] and x[0] != x[1] and x[0] != y[0] and x[1] != y[0] and x[1] != y[1] and y[0] != y[1]:
        if verbose: print("\t'of' and 'to' match",x,"and",y,".")
        if verbose: print("Learned:",x[0],"='o' ",x[1], "='f' ",y[0],"='t'.")
        actual['o'] = x[0]
        actual['f'] = x[1]
        actual['t'] = y[0]

def checkTheE(the,es):
    # e vs the vs t
    # es is a sequence of e options
    if not known('t',actual): return
    if known('e',actual): return
    t = actual['t']

    for e in es:
        if t == the[0] and e == the[2] and the[1] != t and the[1] != e:
            if verbose: print("\t'e' and 'the' and 't' match",e,"and",the,"and",t,".")
            if verbose: print("Learned:",e,"='e' ",the[1],"='h'.")
            actual['e'] = e
            actual['h'] = the[1]
            return

def checkAndAI(w_and, a, i):
    if known('t',actual):
        t = actual['t']
        if w_and[0] == t: return

    # a vs and
    if w_and[0] == a and w_and[1] != a and w_and[1] != i and w_and[2] != a and w_and[2] != i and w_and[1] != w_and[2]:
        if verbose: print("\t'and' and 'a' match",w_and,"and",a,".")
        if verbose: print("Learned:",a,"='a' ",w_and[1],"='n' ",w_and[2],"='d' ",i,"='i'.")
        actual['a'] = a
        actual['n'] = w_and[1]
        actual['d'] = w_and[2]
        actual['i'] = i

def checkThat(that):
    if not known('tha', actual): return
    if known('that',actual): return

    # that: t and h and a should be known
    if that == encrypt('that',actual):
        if verbose: print("'that' matched up with",that,". Nothing new learned tho.")

def checkWith(w_with):
    if not known('th',actual): return
    if known('with',actual): return

    # with: t and h should be known
    if known('i',actual) and w_with[1:] == encrypt('ith',actual):
        print("\t'with' matched up with",w_with,".")
        print("Learned:",w_with[0],"='w'.")
        actual['w'] = w_with[0]

    elif not known('i',actual) and w_with[2:] == encrypt('th',actual):
        print("\t'with' matched up with",w_with,".")
        print("Learned:",w_with[0],"='w' ",w_with[1],"='i'.")
        actual['w'] = w_with[0]
        actual['i'] = w_with[1]

def checkHave(w_have):
    if not known('ae',actual): return
    if known('have',actual): return

    if w_have[1] == actual['a'] and w_have[3] == actual['e']:
        print("\t'have' matched up with",w_have,".")
        print("Learned:",w_have[0],"='h'  ",w_have[2],"='v'.")
        actual['h'] = w_have[0]
        actual['v'] = w_have[2]

def checkFrom(w_from):
    if not known('fro',actual): return
    if known('from',actual): return

    if w_fro[0:3] == encrypt('fro',actual):
        print("\t'from' matched up with",w_from,".")
        print("Learned:",w_from[3],"='m'.")
        actual['m'] = w_have[3]

def checkThis(w_this):
    if not known('thi',actual): return
    if known('this',actual): return

    if w_this[0:3] == encrypt('thi',actual):
        print("\t'this' matched up with",w_this,".")
        print("Learned:",w_this[3],"='s'.")
        actual['s'] = w_this[3]

def checkWhich(w_which):
    # _hi_h can only be which. i checked
    if not known('hi',actual): return
    if known('which',actual): return

    if w_which[1:3] == encrypt('hi',actual) and w_which[4] == actual['h']:
        print("\t'which' matched up with",w_which,".")
        print("Learned:",w_which[3],"='c'  ",w_which[0],"='w'.")
        actual['c'] = w_which[3]
        actual['w'] = w_which[0]

def checkTheir(w_their):
    if not known('thei',actual): return
    if known('their',actual): return

    if w_their[0:4] == encrypt('thei',actual):
        print("\t'their' matched up with",w_their,".")
        print("Learned:",w_their[4],"='r'.")
        actual['r'] = w_their[4]

def decipherIt(filename):
    print("======================================")
    print("Deciphering",filename)
    text = readText(filename) # [Hello., How, are, you?]
    cleanText(text)         # [hello, how, are, you]

    ###############################################################
    # Check out the letter frequencies
    uniqueWords = getUniqueWords(text)
    letterCounts = countLetters(uniqueWords)
    letterlist = getPopularityList(letterCounts)

    print("One of these is 'e':", letterlist[0:2])
    maybe_e = (letterlist[0], letterlist[1])

    # Check out the word frequencies
    wordFreqs = getWordFrequencies(text) # {i:3, have:1, etc}

    ###############################################################
    print()
    maybe_i = 0
    maybe_a = 0
    ones = getFreqByLen(wordFreqs,1)
    print("ones:",ones)
    oneslist = getPopularityList(ones)
    if (len(oneslist) == 2):
        print("There are two 1-letter words (as expected).")
        print("These are likely 'i' and 'a':",oneslist)
        maybe_i = oneslist[0]
        maybe_a = oneslist[1]
    else:
        print("ISSUE: There are",len(ones),"1-letter words:",ones)

    ###############################################################
    print()
    twos = getFreqByLen(wordFreqs,2)
    twoslist = getPopularityList(twos)
    # most frequent 2-letter words: of to in
    print("This is probably 'of', 'to', and 'in':", twoslist[0:3])

    checkOfTo(twoslist[0],twoslist[1])
    checkOfTo(twoslist[1],twoslist[0])
    checkOfTo(twoslist[0],twoslist[2])
    checkOfTo(twoslist[2],twoslist[0])
    checkOfTo(twoslist[1],twoslist[2])
    checkOfTo(twoslist[2],twoslist[1])

    if not known('oft', actual): print("ISSUE: Failed to discover o, f, and t from most frequent 2-letter words.")

    ###############################################################
    print()
    # https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/1-10000
    #pop = getPopularityList(wordFreqs)
    threes = getFreqByLen(wordFreqs,3)
    threeslist = getPopularityList(threes)
    print("These are probably 'the' and 'and':", threeslist[0:5])

    checkTheE(threeslist[0],maybe_e)
    checkTheE(threeslist[1],maybe_e)
    checkTheE(threeslist[2],maybe_e)

    if not known('e',actual): print("ISSUE: Failed to discover e and h from the most frequent 3-letter words.")

    for i in list(range(5)):
        checkAndAI(threeslist[i],maybe_a, maybe_i)
        checkAndAI(threeslist[i],maybe_i, maybe_a)

    if not known('i',actual): print("ISSUE: Failed to discover i, a, n and d from the most frequent 3-letter words.")

    ###############################################################
    print()
    fours = getFreqByLen(wordFreqs,4)
    fourslist = getPopularityList(fours)
    print("These are probably 'that' 'with' 'have' 'from' 'this':", fourslist[0:5])

    for i in list(range(5)):
        checkThat(fourslist[i])

    for i in list(range(5)):
        checkWith(fourslist[i])

    for i in list(range(5)):
        checkHave(fourslist[i])

    for i in list(range(5)):
        checkFrom(fourslist[i])

    for i in list(range(5)):
        checkThis(fourslist[i])

    if not known('w',actual): print("ISSUE: Failed to discover w from the most frequent 4-letter words.")
    if not known('v',actual): print("ISSUE: Failed to discover v from the most frequent 4-letter words.")
    if not known('m',actual): print("ISSUE: Failed to discover m from the most frequent 4-letter words.")
    if not known('s',actual): print("ISSUE: Failed to discover s from the most frequent 4-letter words.")

    ###############################################################
    print()
    fives = getFreqByLen(wordFreqs,5)
    fiveslist = getPopularityList(fives)
    print("These are probably 'which' and 'their':", fiveslist[0:5])

    for i in list(range(5)):
        checkWhich(fiveslist[i])
    for i in list(range(5)):
        checkTheir(fiveslist[i])

    if not known('c',actual): print("ISSUE: Failed to discover c from the most frequent 5-letter words.")

    if not known('r',actual): print("ISSUE: Failed to discover r from the most frequent 5-letter words.")

    searchCommonWords(wordFreqs, actual)

    if len(knowns(actual)) == 25:
        # figure out which one is missing and put it in
        fromLetter = unknowns(actual)[0]
        string = 'qwertyuiopasdfghjklzxcvbnm'
        for key in actual:
            string = string.replace(actual[key],'')
        if len(string)!= 1: print("issue: not mapped to", string)
        toLetter = string
        actual[fromLetter] = toLetter

    if len(knowns(actual)) == 26:
        cipher = reverseCipher(actual)
        original = readTextLines(filename)
        message = decrypt(original, cipher)
        print("Message decrypted")
        writeText("decrypted_"+filename, message)
    else:
        print("knowns:",knowns(actual))
        print("unknowns:",unknowns(actual))
        print("needs more words")
    print("======================================")

actual = makeLetterDict()
decipherIt("encrypted1.txt")
actual = makeLetterDict()
decipherIt("encrypted2.txt")
actual = makeLetterDict()
decipherIt("encrypted3.txt")

