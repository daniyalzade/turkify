# This Python file uses the following encoding: utf-8

import argparse
import codecs
parser = argparse.ArgumentParser()


TURKISH_TO_LATIN = {
        u'ç':u'c',
        u'ı':u'i',
        u'ğ':u'g',
        u'ö':u'o',
        u'ü':u'u',
        u'ş':u's',
        u'â':u'a',
        }

LATIN_TO_TURKISH = dict([(v, k) for (k, v) in TURKISH_TO_LATIN.items()])

def _get_all_words(data_path):
    words = set()
    with codecs.open(data_path, "r", "utf-8") as data:
        for w in data.readlines():
            cur = w.split()[0]
            words.add(cur)
    return words

def _get_cur_words(path):
    words = set()
    with open(path) as data:
        for l in data.readlines():
            for w in l.split():
                words.add(w)
    return words

def _get_canonical(word):
    return word.lower()

#def _get_closest(canonical, all_words):
#    closest = ''
#    latin_to_turkish = dict([(v, k) for (k, v) in TURKISH_TO_LATIN_CHAR_MAP.items()])
#    for c in canonical:
#        if (closest + c) in all_words:
#            closest += 

    #return word.lower()

def _combinations(canonical):
    def _get_char_combs(c):
        c = unicode(c)
        if c in LATIN_TO_TURKISH:
            return [c, LATIN_TO_TURKISH[c]]
        return [c]
    if len(canonical) == 1:
        return _get_char_combs(canonical)
    cur = canonical[0]
    rest = canonical[1:]
    new_words = []
    for i in _get_char_combs(cur):
        words = _combinations(rest)
        for word in words:
            new_word = u"%s%s" % (i, word)
            #print i, word, new_word
            new_words.append(new_word)
    return new_words

parser.add_argument("-d", "--data",
        default='full.txt.tr',
        )
parser.add_argument("-f", "--file",
        default='test.txt',
        )

args = parser.parse_args()
all_words = _get_all_words(args.data)
#print len(all_words)
cur_words = _get_cur_words(args.file)
#combi

for cur_word in cur_words:
    combinations = _combinations(_get_canonical(cur_word))
    translated = cur_word
    for comb in combinations:
        if comb in all_words:
            translated = comb
    print u"%s -> %s" % (cur_word, translated)
