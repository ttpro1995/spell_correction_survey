from collections import Counter
import re
import os

def words(text):
    """
    Read from text file
    :param text:
    :return:
    """
    return re.findall(r'\w+', text.lower())


bigfile = "big.txt"
if not os.path.isfile(bigfile):
    bigfile = "norvig_method/big.txt"

WORDS = Counter(words(open(bigfile).read()))
KNOWN_WORDS = set(words(open(bigfile).read()))

def P(word, N=sum(WORDS.values())):
    return WORDS[word] / N

def known(input_words):
    """
    check if a word is know
    :param word: one word token only
    :return: true if known
    """
    # try :
    return set(w for w in input_words if w in WORDS)
    # except:
    #     print("error ", word)