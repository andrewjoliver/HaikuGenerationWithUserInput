# HaikuGenerationWithUserInput
This project generates Haikus using word frequency analysis from a large text of poetry. The generation of Haikus changes as the user "likes" or "dislikes" certain poems. 

The Haikus have a basic structure and novel adjectives/nouns are generated to produce novel Haikus. Initially, a list of nouns and adjectives (that are common in poetry) are specified. Word frequency analysis is used to see how many times these words occur in ~2500 lines of poetry that was compiled from the web. 

Nouns/Adjs are picked using this equation/idea. Let compositenum = random.randint(0,7) + nnum_frequentwords[y] where nnum_frequentwords[y} is the number of occurences of a randomly selected word (y). If compositenum > some threshold (~7) then this word is used in the poetry. This process is repeated for all nouns/adjectives.

If the user rates a Haiku as "good" the number of occurences of a randomly selected word (y) is increased by 1, which gives a higher likelihood that this word will be greater than the established threshold. This is applied indiscriminately to all words in the poem for some rudimental machine learning. 
