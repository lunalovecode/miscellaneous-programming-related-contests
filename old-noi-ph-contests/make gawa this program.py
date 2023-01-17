t = int(input())
sentences = [input() for x in range(t)]
possible_subjects = ["I", "You", "He", "She", "We", "They"]
make_tenses = ["will make", "make", "makes", "made"]
punctuation = [".", "!"]
vowels = "aeiou"
def divide(word, before_vowel):
    syllables = []
    first_vowel = ""
    for i in word:
        if i in vowels:
            first_vowel = word[word.index(i)]
            if before_vowel:
                syllables = [word[0:word.index(i)], word[word.index(i)::]]
                break
            else:
                syllables = [word[0:word.index(i) + 1], word[word.index(i) + 1::]]
                break
    return [syllables, first_vowel]

# How do I find an element in a list that matches another list and return it?

def translate(sentence):
    words = sentence.split()
    subj = words[0]
    make = ""
    verb = words[2]
    noun = words[-1]
    # punc = noun[-1]
    pandiwa = []
    simuno = ""
    if "will make" in sentence:
        make = "will make"
        verb = words[3]
    elif "make" in sentence:
        make = "make"
    elif "makes" in sentence:
        make = "makes"
    else:
        make = "made"
        
    if subj == "I":
        simuno = "ko"
    elif subj == "You":
        simuno = "mo"
    elif subj == "He" or subj == "She":
        simuno = "niya"
    elif subj == "We":
        simuno = "natin"
    else:
        simuno = "nila"
    # Divide the verb into syllables
    # made:
    # make/makes:
    # - 
    if make == "will make":
        # Repeat the first syllable of the verb.
        pandiwa.append(divide(verb, True)[0][0].upper())
        pandiwa.append(divide(verb, True)[1])
        pandiwa.append(divide(verb, False)[0][0])
        pandiwa.append(divide(verb, False)[0][1])
        # Reverse the verb
        temp = list(reversed("".join(pandiwa)))
        for j in range(len(temp)):
             # If the last vowel of the verb is o, replace it with u.
            if temp[j] in vowels and temp[j] == "o":
                temp[j] = "u"
                pandiwa = list("".join(reversed(temp)))
                break
        if temp[0] in vowels:
            # If the last letter is a vowel, add hin at the end.
            pandiwa.append("hin")
        else:
            # Otherwise, add in at the end.
            pandiwa.append("in")
    elif make == "make" or make == "makes":
        # Repeat the first syllable then add the string in before the first vowel.
        pandiwa.append(divide(verb, True)[0][0].upper())
        pandiwa.append("in")
        pandiwa.append(divide(verb, False)[1])
        pandiwa.append(divide(verb, False)[0][0])
        pandiwa.append(divide(verb, False)[0][1])
    else:
        # Add the string in before the first vowel.
        pandiwa.append(divide(verb, True)[0][0].upper())
        pandiwa.append("in")
        pandiwa.append(divide(verb, False)[1])
        pandiwa.append(divide(verb, False)[0][1])
    return f"{''.join(pandiwa)} {simuno} ang {noun}"

for k in range(t):
    print(translate(sentences[k]))