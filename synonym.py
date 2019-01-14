import nltk 
from nltk.corpus import wordnet 
synonyms = [] 
antonyms = [] 
  
for syn in wordnet.synsets("good"): 
    for l in syn.lemmas(): 
        synonyms.append(l.name()) 
        #if l.antonyms(): 
            #antonyms.append(l.antonyms()[0].name()) 
  
print(set(synonyms)) 

w1 = wordnet.synset('good.n.01') # v here denotes the tag verb 
w2 = wordnet.synset('lie.n.01') 
print(w1.wup_similarity(w2))  
