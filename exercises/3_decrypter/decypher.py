def reverseCipher(c):
    cipher = {v: k for k, v in c.items()}
    return cipher

def known(letters, cipher):
    found = ""
    for let in letters:
        if cipher[let] != 0:
            found += let
    return len(found) == len(letters)

def knowns(cipher):
    x = []
    for let in cipher:
        if cipher[let] != 0:
            x.append(let)
    return x

def unknowns(cipher):
    x = []
    for let in cipher:
        if cipher[let] == 0:
            x.append(let)
    return x

def encrypt(word,cipher):
    x = ""
    for let in word:
        if cipher[let] != 0:
            x += cipher[let]
        else:
            x += "_"
    return x

def decrypt(text, cipher):
    # text is a list of words w punctuation and capitals.
    # cipher is a string that each letter should become mapped to.
    crypt = []
    for word in text:
        newword = ""
        for letter in word:
            if letter.isalpha():
                if letter.isupper():
                    newword += cipher[letter.lower()].upper()
                else:
                    newword += cipher[letter]
            else:
                newword += letter
        crypt.append(newword)
    return crypt

def writeText(filename, message):
    file = open("decrypted/"+filename,'w')
    for word in message:
        file.write(word)
    file.close()

def readTextLines(filename):
    file = open("encrypted/"+filename,'r')
    list = file.readlines()
    file.close()
    return list

def readText(filename):
    file = open("encrypted/"+filename,'r')
    string = file.read()
    list = string.split()
    file.close()
    return list

verb = False
changeMade = False

# https://www.thefreedictionary.com/words-containing-thei
def searchForIt(before,likelyLetter,after, words, cipher):
    # return boolean true if it made a change. false if not
    # edits the cipher
    global changeMade

    string = before + "_" + after
    likelyWord = before + likelyLetter + after
    if known(before+after, cipher) and not known(likelyLetter, cipher):
        if verb: print("Searching for candidate",string,"to match", likelyWord)
        encrypted_before = encrypt(before, cipher)
        encrypted_after = encrypt(after, cipher)
        suspects = []
        for key in words:
            if len(key) == len(string) and \
                (len(before)== 0 or key[:len(before)] == encrypted_before) and \
                (len(after) == 0 or key[len(before)+1:] == encrypted_after):
                suspects.append(key)

        # remove suspects that use a letter we already know
        keep = []
        for s in suspects:
            if len(before)>0: letter = s[len(before)]
            else: letter = s[0]
            found = False
            for v in list(cipher.values()):
                if v == letter: found = True
            if found:
                if verb: print("\tWe already know how to decrypt",letter,".")
            else: keep.append(s)
        suspects = keep

        if len(suspects) == 1:
            word = suspects[0]
            if verb: print("\tFound",word,"in the text. It's almost certainly '", likelyWord,"'.")
            if len(before)>0: letter = word[len(before)]
            else: letter = word[0]
            if verb: print(letter,"is decrypted as '",likelyLetter,"'.")
            cipher[likelyLetter] = letter
            changeMade = True

        elif len(suspects) == 0:
            if verb: print("\tNo candidates found")
        else:
            if verb: print("\tToo many candidates found:", suspects)


def searchCommonWords(words, cipher, v=False):
    # words is a freqencies dictionary keyed by word OR a list of words
    # https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/1-10000
    # other common long letter words: would there could other about little
    # should great before these after first never shall where those himself
    # without through being might again think every people thought under found
    # place while young
    global verb, changeMade
    verb = v

    changeMade = True
    while changeMade and len(knowns(cipher)) < 26:
        if verb: print("Searching for a list of common words")
        changeMade = False
        searchForIt('septem','b','er', words, cipher) # september
        searchForIt('re','b','ellion', words, cipher) #
        searchForIt('mem','b','er', words, cipher) #
        searchForIt('mem','b','ers', words, cipher) #
        searchForIt('a','b','sence', words, cipher) #
        searchForIt('pu','b','lic', words, cipher) #
        searchForIt('pu','b','licly', words, cipher) #
        searchForIt('a','b','ove', words, cipher) #
        searchForIt('ala','b','ama', words, cipher) #
        searchForIt('a','b','stain', words, cipher) #
        searchForIt('la','b','or', words, cipher) #
        searchForIt('reasona','b','le', words, cipher) #
        searchForIt('reasona','b','ly', words, cipher) #
        searchForIt('suita','b','le', words, cipher) #
        searchForIt('suita','b','ly', words, cipher) #
        searchForIt('','b','efore', words, cipher) # _efore: before
        searchForIt('','b','ehind', words, cipher)  # _ehind: behind
        searchForIt('de','b','it', words, cipher)  # de_it: debit
        searchForIt('ameri','c','a', words, cipher) #
        searchForIt('ameri','c','an', words, cipher) #
        searchForIt('symboli','c','', words, cipher) #
        searchForIt('bea','c','on', words, cipher) #
        searchForIt('injusti','c','e', words, cipher) #
        searchForIt('injusti','c','es', words, cipher) #
        searchForIt('','c','aptivity', words, cipher) #
        searchForIt('','c','aptive', words, cipher) #
        searchForIt('','c','ountry', words, cipher) # _ountry: country
        searchForIt('','c','apital', words, cipher) # _apital: capital
        searchForIt('','d','ual', words, cipher)    # _ual: dual
        searchForIt('thei','r','', words, cipher)  # thei_: their thein
        searchForIt('','o','ther', words, cipher) # _ther: other ether ither but we already know e and i
        searchForIt('','g','reat', words, cipher)  # _reat: great treat but we already know t
        searchForIt('tho','s','e', words, cipher)  # tho_e: those thole
        searchForIt('thro','u','gh', words, cipher) # thro_gh: through
        searchForIt('a','g','ain', words, cipher)  # a_ain: amain again
        searchForIt('','j','ustice', words, cipher) # _ustice: justice
        searchForIt('','j','anuary', words, cipher) # _anuary: january manuary
        searchForIt('sub','j','ect', words, cipher) # sub_ect: subject subsect
        searchForIt('re','j','oice', words, cipher) # re_oice: rejoice revoice
        searchForIt('re','j','oicing', words, cipher) # re_oicing: rejoicing revoicing
        searchForIt('chec','k','', words, cipher)  # chec_: check
        searchForIt('bac','k','', words, cipher) # bac_: back bach
        searchForIt('usua','l','', words, cipher)  # usua_: usual
        searchForIt('ce','l','ebrate', words, cipher) # celebrate cerebate
        searchForIt('ce','l','ebration', words, cipher) # celebration cerebration
        searchForIt('symbo','l','ic', words, cipher) #
        searchForIt('bruta','l','', words, cipher)  #
        searchForIt('cou','l','d', words, cipher)  #
        searchForIt('shou','l','d', words, cipher)  #
        searchForIt('per','m','it', words, cipher)  # per_it: permit
        searchForIt('hu','m','an', words, cipher)  # hu_an: human
        searchForIt('enem','m','y', words, cipher)  # enem_: enemy
        searchForIt('freedo','m','', words, cipher)  # freedo_: freedom
        searchForIt('ene','m','ies', words, cipher)  # ene_ies: enemies
        searchForIt('lifeti','m','e', words, cipher)  # lifeti_e: lifetime
        searchForIt('proble','m','', words, cipher)  # proble_: problem
        searchForIt('welco','m','e', words, cipher)  # welco_e: welcome
        searchForIt('','m','oreover', words, cipher)  #
        searchForIt('de','m','onstration', words, cipher) # de_onstration: demonstration
        searchForIt('e','q','uality', words, cipher) # e_uality: equality
        searchForIt('e','q','ual', words, cipher) # e_ual: equal
        searchForIt('re','q','uest', words, cipher) # re_uest: request
        searchForIt('thing','s','', words, cipher)  # thing_: things
        searchForIt('','s','mile', words, cipher) # _mile: smile
        searchForIt('faer','y','', words, cipher)  # faer_: faery
        searchForIt('e','v','ery', words, cipher)  # e_ery: every emery
        searchForIt('tho','u','ght', words, cipher)# tho_ght: thought
        searchForIt('','u','nder', words, cipher)  # _nder: under ender
        searchForIt('fo','u','nd', words, cipher)  # fo_und: found
        searchForIt('','w','ith', words, cipher)   # _ith: with kith pith sith
        searchForIt('','w','hen', words, cipher) # _hen: when then but we already know t
        searchForIt('','w','ere', words, cipher) # _ere: were here mere pere sere fere cere dere but we already know h
        searchForIt('','b','een', words, cipher) # _een: been seen keen teen ween peen but we already know s t
        searchForIt('wo','u','ld', words, cipher) # wo_ld: would world woald but we already know r and a
        searchForIt('o','u','t', words, cipher)  # o_t: oot oat oft out opt
        searchForIt('u','s','ual', words, cipher) # u_ual: usual
        searchForIt('u','p','', words, cipher)   # u_: up us um uh ut un but we know h and t and n and s and nobody puts um in a speech
        searchForIt('yo','u','', words, cipher)    # yo_: you yon yow yob yom yod yok
        searchForIt('','w','hile', words, cipher) # _hile: while
        searchForIt('e','x','ile', words, cipher) # e_ile: exile edile
        searchForIt('lu','x','ury', words, cipher) # lu_ury: luxury
        searchForIt('e','x','pect', words, cipher)
        searchForIt('','y','ou', words, cipher)  # _ou: you fou sou
        searchForIt('realit','y','', words, cipher) # realit_: reality
        searchForIt('mechani','z','ed', words, cipher)  #
        searchForIt('mechani','z','er', words, cipher)  #
        searchForIt('mechani','z','es', words, cipher)  #
        searchForIt('citi','z','en', words, cipher) # citi_en: citizen
        searchForIt('citi','z','ens', words, cipher) # citi_ens: citizens
        searchForIt('citi','z','enship', words, cipher) # citi_enship: citizenship
