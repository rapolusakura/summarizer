import spacy
from collections import Counter, defaultdict
from operator import itemgetter

nlp = spacy.load('en')

def summarize_text(text, lengthOfSummary):
# Process `text` with Spacy NLP Parser
    doc = nlp(text)

    #creates a keyList of top 10 keywords, parses documents into list of sentences
    keywords = Counter()
    for chunk in doc.noun_chunks:
        if nlp.vocab[chunk.lemma_].prob < - 8: # probablity value -8 is arbitrarily selected threshold
            keywords[chunk.lemma_] += 1
    keyList = keywords.most_common(10)
    sentences = [s for s in doc.sents]
    for sentence in sentences:
        print(sentence)
    sentenceList = [] #a 2D array containing the index of each sentence and its score

    #assigining points to each sentence
    for i in range(0,len(sentences)):
        actualSentence = sentences[i].lemma_ #breaks up current sentence in sentences into basic word forms
        sentPoint = 0 #always reset the points when looping through the sentences
        for k in range(0,len(actualSentence)): #this for loop loops through each word in actualSentence
            currentWord = str(actualSentence[k].encode('utf-8')) #assigning currentWord to first word in actualSentence
            for j in range(1,len(keyList)): #starting at one bc the first element in keyList is not a useful keyword, loops through list of keywords
                if currentWord in str(keyList[j][0]): #checking if basic word from sentence is a substring of the keyword
                    sentPoint+= keyList[j][1] #adds points to the sentence equal to the frequency of the keyword
        eachSent = [i, sentPoint] #array containing the index of the currentSentence and its points
        sentenceList.append(eachSent) #add eachSent to the sentenceList

    #sorting the sentences by point value and putting them in a list, sorting those by sentence index and adding it to a string
    sortedSentByPoints = sorted(sentenceList, key=itemgetter(1), reverse=True)
    justSentList = []
    for x in range(0,int(lengthOfSummary)):
        justSentList.append(sortedSentByPoints[x])
    justSentList = sorted(justSentList, key=itemgetter(0), reverse=False)
    summary = ""
    for index in range(0,len(justSentList)):
        summary+=str(sentences[justSentList[index][0]]) + " "

    return summary


def get_character_adjectives(doc, character_lemma):
    adjectives = []
    for ent in processed_text.ents:
        if ent.lemma_ == character_lemma:
            for token in ent.subtree:
                if token.pos_ == 'ADJ': # Replace with if token.dep_ == 'amod':
                    adjectives.append(token.lemma_)
    for ent in processed_text.ents:
        if ent.lemma_ == character_lemma:
            if ent.root.dep_ == 'nsubj':
                for child in ent.root.head.children:
                    if child.dep_ == 'acomp':
                        adjectives.append(child.lemma_)
    return adjectives


def common(text):
    processed_text = nlp(text)
    doc_2 = nlp(text)
    characters = Counter()
    other = Counter()

    for ent in doc_2.ents:
        if ent.label_ == "PERSON":
            if nlp.vocab[ent.lemma_].prob < - 8: # probablity value -8 is arbitrarily selected threshold
                characters[ent.lemma_] += 1
        elif ent.label_ == "NORP" or ent.label_ == "ORG" or ent.label_ == "GPE":
            if nlp.vocab[ent.lemma_].prob < - 8: # probablity value -8 is arbitrarily selected threshold
                other[ent.lemma_] += 1
    others = other.most_common(5)
    chars = characters.most_common(3)
    return others

def commonppl(text):
    processed_text = nlp(text)
    doc_2 = nlp(text)
    characters = Counter()
    other = Counter()

    for ent in doc_2.ents:
        if ent.label_ == "PERSON":
            if nlp.vocab[ent.lemma_].prob < - 8: # probablity value -8 is arbitrarily selected threshold
                characters[ent.lemma_] += 1
        elif ent.label_ == "NORP" or ent.label_ == "ORG" or ent.label_ == "GPE":
            if nlp.vocab[ent.lemma_].prob < - 8: # probablity value -8 is arbitrarily selected threshold
                other[ent.lemma_] += 1
    others = other.most_common(5)
    chars = characters.most_common(3)
    return chars
    allchars = []
    allothers = []
    for char in chars:
        allchars.append(char[0])
    for entity in others:
        allothers.append(entity[0])
    print allothers
    print allchars

    # for char in chars:
    #     prettyList = []
    #     person = char[0]
    #     charList = get_character_adjectives(processed_text, person)
    #     if(charList != []):
    #         for x in range(len(charList)):
    #             if(charList[x]!="-PRON-" and charList[x] not in prettyList):
    #                 prettyList.append(charList[x])
    #         print char[0] + ": ",#how to not do a println?
    #         for elem in prettyList:
    #             print(elem),
    #         print
