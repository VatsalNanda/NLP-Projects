from textblob import TextBlob

sent = TextBlob("Hello, my name is Vatsal Nanda and I am a Machine Learning Enthusiast. ")
for np in sent.noun_phrases:
 print (np)
