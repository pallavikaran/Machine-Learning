# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 19:53:11 2015

@author: ANISH
"""
from __future__ import division
import pandas as pd
import nltk
from nltk.corpus import wordnet as wn
#df = pd.read_excel("training_set_rel3 (1).xls")
df = pd.read_excel("MyTester.xlsx")
df.head()
c=0
c1=0
d=0
e=0
w=0
#prints the whole Excel file's data
#print(df)

me=[]
wo=0
fr=0
#word count
print("word count is")
for index in range(len(df)):
     c=0
     c1=0
     s=0
     p=df.essay[index]
     for i in range(len(p)):
         if p[i]==" ":
           c=c+1
         if p[i]==".":
           s=s+1
     print(c+1)
     wo=c+1
     fr=pow(wo,0.25)
     print("fourth root of number of words in the essay")
     print(fr)
     print(s)
     print("Number of words divided by Number of sentences")
     print((wo)/s)
     print("")
     df["Words"] = c
     df.head()
     me.append(c)
   

#sentence count
f=[]
print("sentence count is")
for index in range(len(df)):
    c=0
    d=0
    p=df.essay[index]
    for i in range(len(p)):
         c=c+1
         if p[i]==".":
           d=d+1
    print(d)
    f.append(d)
    print(c)
    print("number of characters by number of sentences")
    print(c/d)
    print("")
    df["sentences"] = d
    df.head()
    me.append(d)

    
"""#number of words greater than 6
print("number of words greater than 6 in the essay's")
for index in range(len(df)):
    e=0
    r=df.essay[index]
    for word in r.split():
        if len(word)>=6:
            e=e+1
    print(e)"""
    
#number of words greater than 6 divided by the number of word tokens
print("number of words greater than 6 in the essay divided by the number of words")
for index in range(len(df)):
    t=0
    e=0
    r=df.essay[index]
    for word in r.split():
        t=t+1
        if len(word)>=6:
            e=e+1
    print(t)
    print(e)    
    print(t/e)
    print("")
    
    
#number of words less than 4 divided by the number of word tokens
print("number of words less than 4 in the essay divided by the number of words")
for index in range(len(df)):
    t1=0
    q=0
    r=df.essay[index]
    for word in r.split():
        t1=t1+1
        if len(word)<=4:
            q=q+1
    print(t1)
    print(q)    
    print(t1/q)
    print("")       
"""   
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
#number of words   
"""p=df.essay[2]
for i in range(len(p)):
   if p[i]==" ":
       c=c+1
print(c+1)
"""
#lemma continue
from sets import Set
for index in range(len(df)):
    t2=0
    r=df.essay[index]    
    count_lemma_set_for_essay=[] 
    for words in r.split():
         t2=t2+1
         lemma_set=Set() 
         for word in words: 
             for synset in wn.synsets(word): 
                for lemma in synset.lemmas(): 
                     lemma_set.add(lemma) 
    #print(lemma_set)
    print(t2)
    print(len(lemma_set))
    print("Number of Lemmas divided by Number of word tokens")
    print(len(lemma_set)/t2)
    print("")
    count_lemma_set_for_essay.append(len(lemma_set))     
    #print(len(count_lemma_set_for_essay))
    
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
            
z=[]
po=0            
#Number of Non-initial Capital character words divided by number of sentences           
for index in range(len(df)):
    t=0
    l=0
    r=df.essay[index]
    for word in r.split():
        l=l+1
        y=word[0]
        if y.isupper():
            t=t+1
    print(t)
    print(l)
    po=l-t
    print("Number of Non-initial Capital character words")
    print(po)
    z.append(po)
    print("")
ncs=[]
print("Number of Non-initial Capital character words divided by number of sentences")
for index in range(len(df)):
    ncs.append(z[index]/f[index])
print("This is it")
print(ncs)
print("s")
print(f)
print("ncw")
print(z)
p1=0
nouns=0
downcased=0
print("Trying grammer for a text")
for index in range(len(df)):
     p=df.essay[index]
     p1=nltk.word_tokenize(p)
     p2=nltk.pos_tag(p1)
     #print(" ")
     #try:
     for word,pos in p2:
             #word = word.strip()
             #pos=pos.strip()
             if pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS':
                 nouns = word
                 downcased = [x.lower() for x in nouns]
     #except ValueError:
             #print('Ignoring: malformed line: "{}"'.format(word))
             #print('Ignoring: malformed line: "{}"'.format(pos))
     print(downcased)

