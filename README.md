***Synonymizer and HaikuMe

This project's goal is to allow a user to enter an english sentence, or subject, and have a valid haiku returned.

This will happen through several step:
1. be able to synonymize any given sentence.  
  Synonymization is defined as:
    1. Splitting a sentence into words
    2. Picking out the interesting words (typically noun, verb, adv, adj types)
    3. Perform API call to look up synonyms for each word
    4. Replace the original words with synonyms, returning the new sentence to the user.
    5. Due to several complications of the english language, return many (10?) versions of the sentence
    6. Allow the user to pick the best one, or rank them, or up/downvote, etc...

2. Be able to count syllables of any given sentence.  This info can probably be obtained via a dictionary API, though the API that I'm currently using to get synonyms does not give pronunciation (which typically splits a word into its synonyms)

3. Be able to write a valid haiku about a subject.  This adds the complication of being able to sumamrize a subject via wikipedia.  Methods to try:
  1. find 3 most "unique" sentences, narrow them down to haiku length, they become the 3 haiku lines
     a. one flaw is that a unique sentence could involve many names, dates, places, which may be harder to get synonym counts on...
     b. making them a haiku might involve synonymizing, which would also be difficult with names, places, numbers
  2. Take the first sentence of each paragraph in the first wikipedia section, which is typically a summary

... part 3 will be quite challenging...
