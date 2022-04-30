import scrapping.wiki_scrape as ws
import os
from nltk.tokenize import word_tokenize
def main():
    # word_tokenize("")
    query = input("Enter your domain of interest: \n")
    os.chdir("scrapping")
    # print(os.listdir())
    ws.wiki_scrape([query])

if (__name__ == "__main__"):
    main()