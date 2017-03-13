import csv
from collections import defaultdict

import nltk
from nltk.corpus import stopwords

stopwords_tagalog = []

def list_stopwords():
    with open("stopwords.txt", "r") as f:
        for word in f:
            stopwords_tagalog.append(word.strip())

def remove_stopwords(document):
    document = ' '.join([word for word in document.split() if
        word.strip() not in stopwords_tagalog and word.strip() not in
        stopwords.words('english') and word.strip()!=' '])
    return document

if __name__ == "__main__":
    articles = []
    list_stopwords()

    with open('../data/no_punctuation.csv') as readfile, open('../data/delete.csv','w') as writefile:
        reader = csv.DictReader(readfile)

        fieldnames = ['title', 'category','content']
        writer = csv.DictWriter(writefile, fieldnames=fieldnames)

        for row in reader:
            articles.append(row)

        writer.writeheader()
        ctr = 0
        for a in articles:
            ar = a['content'].lower()
            writer.writerow({'title':a['title'], 'category':a['category'],'content':remove_stopwords(ar)})
            print ctr
            ctr += 1
