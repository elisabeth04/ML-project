import wikipedia
import tensorflow as tf
import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
from nltk.tokenize import word_tokenize
import os
import warnings
#nltk.download('punkt')
warnings.catch_warnings()
warnings.simplefilter("ignore")
queries = [ "computer science", "networks", "mathematics", "algorithms", "number theory", "graph theory" ]
#download punkt
wikipedia.set_rate_limiting(0.01) #set limit so the all powerful webmaster doesn't block us
 #get a random page content
for query in queries:
    result = wikipedia.search(query) 
    print(f"query: {query}, result: {result}")
    for i in range(len(result)):
        try:
            page = wikipedia.page(result[i])
            content = page.content.lower()
            title = page.title.replace(" ","_")
            if title not in os.listdir("../../data/"):
                with open(f"../../data/{title}.txt", "w") as infile:
                    infile.write(content)
                    infile.close()
        except wikipedia.exceptions.DisambiguationError as e:
            pass
        

        
