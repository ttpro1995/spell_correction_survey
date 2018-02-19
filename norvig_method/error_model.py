from norvig_method.language_model import P, known
from norvig_method.spell import edits1, edits2

def correction(word):
    return max(candidates(word), key=P)

def candidates(word):
    return known([word]) or known(edits1(word)) or known(edits2(word)) or [word]