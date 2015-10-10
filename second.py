# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 19:53:11 2015

@author: ANISH
"""
from __future__ import division
import pandas as pd
import nltk
from nltk.corpus import wordnet as wn
df = pd.read_excel("training_set_rel3 (1).xls")
df.head()
c=0
c1=0
d=0
e=0
w=0
#prints the whole Excel file's data
#print(df)

me=[]
#word count
"""print("word count is")
for index in range(len(df)):
     c=0
     c1=0
     p=df.essay[index]
     for i in range(len(p)):
         if p[i]==" ":
           c=c+1
     print(c+1)
     df["Words"] = c
     df.head()
     me.append(c)"""
   
   
#sentence count
"""print("sentence count is")
for index in range(len(df)):
    d=0
    p=df.essay[index]
    for i in range(len(p)):
         if p[i]==".":
           d=d+1
    print(d)
    df["sentences"] = d
    df.head()
    me.append(d)"""

    
"""#number of words greater than 6
print("number of words greater than 6 in the essay's")
for index in range(len(df)):
    e=0
    r=df.essay[index]
    for word in r.split():
        if len(word)>=6:
            e=e+1
    print(e)
   
#number of words less than 4
print("number of words less than 4 in the essay's")
for index in range(len(df)):
    w=0
    r=df.essay[index]
    for word in r.split():
        if len(word)<=4:
            w=w+1
    print(w)"""

#finding the Lemma's for each word in each essay

"""syn = wn.synsets('cookbook')[0]
lemmas = syn.lemmas()
print(len(lemmas))
print(lemmas[0].name)
print(lemmas[1].name)"""
"""for word in r.split():
    syn = wn.synsets(word)
    lemmas = syn.lemmas()"""
    
p=df.essay[0]
for i in range(len(p)):
   if p[i]==" ":
       c=c+1
print(c+1)
from sets import Set
#for index in range(len(df)):
r=df.essay[0]    
count_lemma_set_for_essay=[] 
for words in r.split(): 
         lemma_set=Set() 
         for word in words: 
             for synset in wn.synsets(word): 
                for lemma in synset.lemmas(): 
                     lemma_set.add(lemma) 
#print(lemma_set)
print(len(lemma_set))
count_lemma_set_for_essay.append(len(lemma_set))     
print(len(count_lemma_set_for_essay))   
    
#useless
# Print the information
"""for synset in wn.synsets:
        print "-" * 10
        print "Name:", synset.name
        print "Lexical Type:", synset.lexname
        print "Lemmas:", synset.lemma_names
        print "Definition:", synset.definition
        for example in synset.examples:
            print "Example:", example"""
            
#Number of Capital starting character words in each essay
for index in range(len(df)):
    t=0
    r=df.essay[index]
    for word in r.split():
        y=word[0]
        if y.isupper():
            t=t+1
    print(t)
