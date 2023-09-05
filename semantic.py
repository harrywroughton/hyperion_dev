# The similarities between cat, monkey and banana were interesting because the more similarity between the words meant 
# the higher the number in the output. For example, it makes sense that banana and cat had a result of 0.223... because there
# is little correlation there, however with banana and monkey the result is 0.404 as much data will find a correlation between this 
# animal and a common food they eat. The same goes with monkey and cat as they are both animals, thus a higher result of 0.592.

import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("toaster")
word2 = nlp("oven")
word3 = nlp("flower")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# en_core_web_sm - the results seem to be far more limited: 'The model you're using has no word vectors loaded, so 
# the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity 
# judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`'
# However, there is still an output result of 0.4414942215905248 for flower with oven, and 0.3908074154318359 for flower with toaster.
# Predictably, the highest number 0.5623945214106559 for toaster with oven makes sense as they are both kitchen appliances. 

# en_core_web_md - the results are improved (assumably due to access to multi-data), giving the below results. All make sense as word1 and word2
# are similar in that they are both kitchen appliances, whereas word3 doesn't have any similarity with that.
# 0.6744098933740568
# 0.1710032771169544
# 0.2802130696324511