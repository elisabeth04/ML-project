import wikipedia
import tensorflow as tf
import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
from nltk.tokenize import word_tokenize
import os
#nltk.download('punkt')
queries = ["natural language processing", "neural networks", "machine learning"]
#download punkt
wikipedia.set_rate_limiting(0.01) #set limit so the all powerful webmaster doesn't block us
 #get a random page content
for query in queries:
    result = wikipedia.search(query) 
    for i in range(len(result)):

        page = wikipedia.page(result[i])
        content = page.content.lower()
        title = page.title.replace(" ","_")
        print(f"title: {title}")
        if title not in os.listdir("../../data/"):
            with open(f"../../data/{title}.txt", "w") as infile:
                infile.write(content)
                infile.close()
