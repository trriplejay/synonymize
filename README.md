<h1>Synonymizer and HaikuMe</h1>

<h4>This project's ultimate goal is to allow a user to enter an english sentence, or subject, and have a valid haiku returned.</h4>

<h4>This will happen through several steps:</h4>
<ol>
  <li>be able to synonymize any given sentence.  
  Synonymization is defined as:
  <ol>
    <li>Splitting a sentence into words</li>
    <li>Picking out the interesting words (typically noun, verb, adv, adj types)</li>
    <li>Perform API call to look up synonyms for each word</li>
    <li>Replace the original words with synonyms, returning the new sentence to the user.</li>
    <li>Due to several complications of the english language, return many (10?) versions of the sentence</li>
    <li>Allow the user to pick the best one, or rank them, or up/downvote, etc...</li>
  </ol>
  </li>

  <li>Be able to count syllables of any given sentence.  This info can probably be obtained via a dictionary API, though the API that I'm currently using to get synonyms does not give pronunciation (which typically splits a word into its synonyms)
  </li>

  <li>Be able to write a valid haiku about a subject.  This adds the complication of being able to sumamrize a subject via wikipedia.  Methods to try:
  <ol>
    <li>1. find 3 most "unique" sentences, narrow them down to haiku length, they become the 3 haiku lines
    <ul>
      <li>a. one flaw is that a unique sentence could involve many names, dates, places, which may be harder to get synonym counts on...</li>
      <li>making them a haiku might involve synonymizing, which would also be difficult with names, places, numbers</li>
     </ul>
    </li>
    <li>Take the first sentence of each paragraph in the first wikipedia section, which is typically a summary</li>
  </li>
</ol>

... part 3 will be quite challenging...
