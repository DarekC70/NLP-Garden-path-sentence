# === Garden-path sentences ==============================================================
#1 The complex houses married and single soldiers and their families.
#2 Fat people eat accumulates.
#3 We painted the wall with cracks.
#4 Mary gave the child the dog bit a Band-Aid.
#5 The girl told the story cried.

import spacy #This statement should work if you have spaCy installed 
nlp = spacy.load('en_core_web_sm')

# Sentence 1 - Tokenisation
print('Tokenisation - sentence #1: The complex houses married and single soldiers and their families.')
sentence_1 = "The complex houses married and single soldiers and their families."

doc = nlp(sentence_1)
doc.text.split()
# After using split
print(doc.text.split())  
# Tokenising sentence - splitting a text into words, symbols
print([token.orth_ for token in doc])
# Tokenization without punctuation and white space
print([token.orth_ for token in doc if not token.is_punct | token.is_space]) 

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

# Identify stop words
for word in doc:
    if word.is_stop == True:
        print(word)

# Sentence 2 - Tokenisation
print('Tokenisation - sentence #2: Fat people eat accumulates.')
sentence_1 = "Fat people eat accumulates."

doc = nlp(sentence_1)
doc.text.split()
# After using split
print(doc.text.split())  
# Tokenising sentence - splitting a text into words, symbols
print([token.orth_ for token in doc])
# Tokenization without punctuation and white space
print([token.orth_ for token in doc if not token.is_punct | token.is_space]) 

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

# Identify stop words
for word in doc:
    if word.is_stop == True:
        print(word)

# Sentence 3 - Tokenisation
print('Tokenisation - sentence #3: We painted the wall with cracks.')
sentence_1 = "We painted the wall with cracks."

doc = nlp(sentence_1)
doc.text.split()
# After using split
print(doc.text.split())  
# Tokenising sentence - splitting a text into words, symbols
print([token.orth_ for token in doc])
# Tokenization without punctuation and white space
print([token.orth_ for token in doc if not token.is_punct | token.is_space]) 

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

# Identify stop words
for word in doc:
    if word.is_stop == True:
        print(word)

# Sentence 4 - Tokenisation
print('Tokenisation - sentence #4: Mary gave the child the dog bit a Band-Aid.')
sentence_1 = "Mary gave the child the dog bit a Band-Aid."

doc = nlp(sentence_1)
doc.text.split()
# After using split
print(doc.text.split())  
# Tokenising sentence - splitting a text into words, symbols
print([token.orth_ for token in doc])
# Tokenization without punctuation and white space
print([token.orth_ for token in doc if not token.is_punct | token.is_space]) 

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

# Identify stop words
for word in doc:
    if word.is_stop == True:
        print(word)

# Sentence 5 - Tokenisation
print('Tokenisation - sentence #5: The girl told the story cried.')
sentence_1 = "The girl told the story cried."

doc = nlp(sentence_1)
doc.text.split()
# After using split
print(doc.text.split())  
# Tokenising sentence - splitting a text into words, symbols
print([token.orth_ for token in doc])
# Tokenization without punctuation and white space
print([token.orth_ for token in doc if not token.is_punct | token.is_space]) 

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

# Identify stop words
for word in doc:
    if word.is_stop == True:
        print(word)

#================================== Comments ===============================================================
# In sentence #2 unusual entitie is  'Fat'.  SpaCY got nun 'Fat people' - the initial meaning 
# is combined as an adjective with the noun - fat people, but the last word 'accumulates' indicates 
# that is subject (noun) meaning - Fat, which is accumulated in the human organism.

# In sentence #1 unusual entitie is 'The complex houses married'. SpaCY got nun ''The complex houses married',
# but that not have sense because people can married, but hauses not! The valid entity is 'complex' (group of buildings),
# that offered acomodetion (houses) for married and single soldiers and their families.

# In these cases, spacy suggests more common solutions.