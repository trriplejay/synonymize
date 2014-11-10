from bighugelabsAPI import BigHugeLabAPI
from secret_key import API_KEY

import sys
import random
"""
haikume.net:
step 1:
    "synonymize me" takes in a sentence and returns many equivalent sentences
    using synonyms.. user picks the one they like best.
step 2:
    use NLTK (www.nltk.org) to parse a user input sentence and count syllables.
    try to count syllables, call synonymize, only return results with same
    syllables.
step 3:
    only return results with specifically 17 syllables.  This will give a
    haiku based on syllable count, though the juxtaposition aspect will be
    missing...
step 4:
    allow the user to provide a "subject", look it up on wikipedia, and write
    a summarizing haiku
    user gives a phrase, statement, sentence, etc.  haikume attempts to convert


Official syllable rules:

The Written Method Rules
Count the number of vowels (A, E, I, O, U) in the word.
Add 1 every time the letter 'y' makes the sound of a vowel (A, E, I, O, U).
Subtract 1 for each silent vowel (like the silent 'e' at the end of a word).

Subtract 1 for each diphthong or triphthong in the word.
Diphthong: when 2 vowels make only 1 sound (aw, oy, oo)
Triphthong: when 3 vowels make only 1 sound (iou)

Add 1 if the word ends with "le" or "les".

The number you are left with is the number of syllables in your word.

"""



def is_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


def count_diphthong_triphthong(word):
    diphthongs = ['ai', 'ou', 'ei', 'ie', 'oa', 'oe', 'io', 'ea']


def vowelcount(word):
    """
    count vowels in a word and return the result
    """
    return sum(list(map(is_vowel, list(word.lower()))))


def process_json():
    """
    takes a word, look up synonymns via JSON request to bighugethesaurus
    via bighugelabsAPI.py
    """
    sample_json = {u'verb': {u'syn': [u'prove', u'try', u'try out', u'examine', u'essay', u'screen', u'quiz', u'ascertain', u'be', u'check', u'determine', u'evaluate', u'find out', u'judge', u'learn', u'pass judgment', u'score', u'see', u'submit', u'take', u'undergo', u'watch']}, u'noun': {u'syn': [u'trial', u'trial run', u'tryout', u'mental test', u'mental testing', u'psychometric test', u'examination', u'exam', u'run', u'attempt', u'communicating', u'communication', u'cover', u'covering', u'effort', u'endeavor', u'endeavour', u'experiment', u'experimentation', u'mental measurement', u'natural covering', u'try']}}

    # we want maybe 2-3 random samples from each available category
    # we don't care about conjunctions, articles, pronouns, etc.. their
    # synonyms wouldn't be interesting
    noun_syn = list()
    verb_syn = list()
    adj_syn = list()
    adv_syn = list()

    syn_dict = {
        'noun': noun_syn,
        'verb': verb_syn,
        'adj': adj_syn,
        'adv': adv_syn,
    }
    # drill down to the list of synonyms
    for word_type, value in sample_json.items():
        # first loop cuts it down to verb/noun separation
        print word_type
        if 'syn' in value:
            templist = list(value['syn'])
            random.shuffle(templist)
            if word_type == 'noun':
                noun_syn.extend(templist)

            elif word_type == 'verb':
                verb_syn.extend(templist.pop())

            elif word_type == 'adj':
                adj_syn.extend(templist.pop())

            elif word_type == 'adv':
                adv_syn.extend(templist.pop())



    return syn_dict



def pick_synonyms(word):
    sample_json={u'verb': {u'syn': [u'prove', u'try', u'try out', u'examine', u'essay', u'screen', u'quiz', u'ascertain', u'be', u'check', u'determine', u'evaluate', u'find out', u'judge', u'learn', u'pass judgment', u'score', u'see', u'submit', u'take', u'undergo', u'watch']}, u'noun': {u'syn': [u'trial', u'trial run', u'tryout', u'mental test', u'mental testing', u'psychometric test', u'examination', u'exam', u'run', u'attempt', u'communicating', u'communication', u'cover', u'covering', u'effort', u'endeavor', u'endeavour', u'experiment', u'experimentation', u'mental measurement', u'natural covering', u'try']}}



def syllablecount(sentence):
    """
    returns list of tuples with word, vowels
    """
    results = []
    for word in sentence.split(' '):
        results.append((word, vowelcount(word)))
    return results

if __name__ == '__main__':

    """
    to invoke, either specify an input file that contains sentences,
    one on each line, and the program will output synonymized results for
    each sentence, or execute the program with no input file and give input
    from command line
    """
    if len(sys.argv) > 1:


        try:
            thefile = open(sys.argv[1])
        except IOError:
            print("no file given")
            thefile = None
        if thefile is not None:
            pass
    else:
        user_input = 'a'
        #while user_input.lower() != 'q':
            #pass
            #user_input = input("enter a sentence to synonymize (q to quit)")


        syn_dict = process_json()
        #api_obj = BigHugeLabAPI(API_KEY, 'json')

        print process_json()
