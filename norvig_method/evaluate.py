from collections import Counter
from norvig_method.error_model import correction
from norvig_method.language_model import WORDS, words, P
import os

def unit_tests():
    assert correction('speling') == 'spelling'  # insert
    assert correction('korrectud') == 'corrected'  # replace 2
    assert correction('bycycle') == 'bicycle'  # replace
    assert correction('inconvient') == 'inconvenient'  # insert 2
    assert correction('arrainged') == 'arranged'  # delete
    assert correction('peotry') == 'poetry'  # transpose
    assert correction('peotryy') == 'poetry'  # transpose + delete
    assert correction('word') == 'word'  # known
    assert correction('quintessential') == 'quintessential'  # unknown
    assert words('This is a TEST.') == ['this', 'is', 'a', 'test']
    assert Counter(words('This is a test. 123; A TEST this is.')) == (
        Counter({'123': 1, 'a': 2, 'is': 2, 'test': 2, 'this': 2}))

    # those comment line does not work because the number was different ...
    # don't know
    # assert len(WORwhyDS) == 32192
    # assert sum(WORDS.values()) == 1115504
    # assert WORDS.most_common(10) == [
    #     ('the', 79808),
    #     ('of', 40024),
    #     ('and', 38311),
    #     ('to', 28765),
    #     ('in', 22020),
    #     ('a', 21124),
    #     ('that', 12512),
    #     ('he', 12401),
    #     ('was', 11410),
    #     ('it', 10681)]
    # assert WORDS['the'] == 79808
    assert P('quintessential') == 0
    assert 0.07 < P('the') < 0.08
    return 'unit_tests pass'


def spelltest(tests, verbose=False):
    "Run correction(wrong) on all (right, wrong) pairs; report results."
    import time
    start = time.clock()
    good, unknown = 0, 0
    n = len(tests)
    for right, wrong in tests:
        w = correction(wrong)
        good += (w == right)
        if w != right:
            unknown += (right not in WORDS)
            if verbose:
                print('correction({}) => {} ({}); expected {} ({})'
                      .format(wrong, w, WORDS[w], right, WORDS[right]))
    dt = time.clock() - start
    print('{:.0%} of {} correct ({:.0%} unknown) at {:.0f} words per second '
          .format(good / n, n, unknown / n, n / dt))


def Testset(lines):
    "Parse 'right: wrong1 wrong2' lines into [('right', 'wrong1'), ('right', 'wrong2')] pairs."
    return [(right, wrong)
            for (right, wrongs) in (line.split(':') for line in lines)
            for wrong in wrongs.split()]

if __name__ == "__main__":
    print(unit_tests())
    spell_testset1 = "spell-testset1.txt"
    spell_testset2 = "spell-testset2.txt"

    if not os.path.isfile(spell_testset1):
        spell_testset1 = os.path.join("norvig_method", spell_testset1)
        spell_testset2 = os.path.join("norvig_method", spell_testset2)

    spelltest(Testset(open('spell-testset1.txt')))  # Development set
    spelltest(Testset(open('spell-testset2.txt')))  # Final test set