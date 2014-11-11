from bighugelabsAPI import BigHugeLabAPI
from secret_key import API_KEY

import sys
from random import shuffle, randint
from string import punctuation

"""
haikume.net:
step 1:
    "synonymize me" takes in a sentence and returns many equivalent sentences
    using synonyms.. user can pick the one they like best.
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


class synonymizer(object):
    """
    takes in a sentence
    """
    def __init__(self, sentence):

        self.sentence = sentence
        self.api_instance = BigHugeLabAPI(API_KEY, 'json')

        # nested dict.  first tier is words we are swapping
        # second tier keys are noun, verb, adv, adj
        # values in second tier are the synonyms
        self.syn_dict = dict()
        self.words_to_syn = list()
        self.sent_iter = None

        # kick off the processing
        self.analyze_sentence()

    @property
    def sentence(self):
        return self._sentence

    # any time a user changes the initial sentence, it should re-trigger
    # the analysis and reset the other inner attributes
    @sentence.setter
    def sentence(self, value):
        if type(value) != str:
            raise TypeError("please provide a string as input.")
        else:
            self._sentence = value
            self.words_to_syn = list()
            self.syn_dict = dict()
            self.sent_iter = None
            self.analyze_sentence()

    def analyze_sentence(self):

        temp = self.sentence.strip().split(' ')

        # remove punctuation
        #temp = self.sentence.translate(None, string.punctuation)

        for word in temp:
            word = word.translate(None, punctuation)
            # ignore contractions
            if "'" in word or "-" in word:
                pass
            # ignore nubmers or words containing numbers
            elif not word.isalpha():
                pass
            elif len(word) < 4:
                pass
            else:
                if word not in self.words_to_syn:
                    self.words_to_syn.append(word)

    def get_synonyms(self):
        if self.syn_dict:
            raise ValueError("we already got the synonyms, call get_new_sentence")
        else:
            for word in self.words_to_syn:
                # process_json returns a list of synonyms for the word
                # get_word in the API returns the json result
                result = self.process_json(self.api_instance.get_word(word))

                self.syn_dict[word] = result
                #if word == 'test':
                #    self.syn_dict[word] = self.process_json()

    def get_new_sentence(self):
        # should return the next value in an iterator.
        # builds a new sentence based on the original
        # could be TONS of combinations, depending on the length of the
        # sentence, so generator is the best way to go, rather than
        # calculating every permutation at once
        if self.syn_dict is None:
            self.get_synonyms()
        if self.sent_iter is None:
            self.sent_iter = self.get_next_sent()
        return next(self.sent_iter)

    def get_next_sent(self):
        # each choice is going to be random for the sake of
        # simplicity and more variety from the user's point of view
        # assume at this point that we have a
        while True:
            newsent = self.sentence
            start = 0
            end = len(newsent)

            for word, syn_list in self.syn_dict.items():
                while newsent.count(word) > 0:
                    # in case the same word occurs more than once in the
                    # sentence, replace them each with a random synonym
                    index = randint(0, len(syn_list)-1)
                    wordstart = newsent.index(word,)
                    wordend = wordstart + len(word)
                    newsent = newsent[start:wordstart] + syn_list[index] + newsent[wordend:end]

            yield newsent


    def process_json(self, input_json=None):
        """
        takes a word, look up synonymns via JSON request to bighugethesaurus
        via bighugelabsAPI.py
        """
        if input_json is None:
            # for testing
            input_json = {u'verb': {u'syn': [u'prove', u'try', u'try out', u'examine', u'essay', u'screen', u'quiz', u'ascertain', u'be', u'check', u'determine', u'evaluate', u'find out', u'judge', u'learn', u'pass judgment', u'score', u'see', u'submit', u'take', u'undergo', u'watch']}, u'noun': {u'syn': [u'trial', u'trial run', u'tryout', u'mental test', u'mental testing', u'psychometric test', u'examination', u'exam', u'run', u'attempt', u'communicating', u'communication', u'cover', u'covering', u'effort', u'endeavor', u'endeavour', u'experiment', u'experimentation', u'mental measurement', u'natural covering', u'try']}}

        synonyms = []

        # drill down to the list of synonyms
        for word_type, value in input_json.items():
            # first loop cuts it down to verb/noun separation
            if 'syn' in value:
                synonyms.extend(value['syn'])

        # give them a shuffle, just for fun

        shuffle(synonyms)

        return synonyms


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

        #syn_dict = process_json()

        the_obj = synonymizer("Hello, world! I am a sentence")
        print the_obj.words_to_syn
        the_obj.get_synonyms()
        print the_obj.syn_dict.keys()
        print the_obj.get_new_sentence()
        #api_obj = BigHugeLabAPI(API_KEY, 'json')

        #for key, value in syn_dict.items():
         #   if len(value) > 0:
          #      print value
