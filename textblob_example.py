from textblob import TextBlob

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

blob = TextBlob(text)
blob.tags

blob.noun_phrases

#print sentiment polarity

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)

#translate to Spanish

blob.translate(to="es")

#dislpay sentiment tuple

blob.sentiment

#display list of sentences

blob.sentences

#display words

blob.words

#display noun phrases

blob.noun_phrases
