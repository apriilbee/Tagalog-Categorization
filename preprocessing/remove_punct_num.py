# coding=utf-8

import csv
import string

def removePunctuationAndNumbers(article):
    #replace_punctuation = ''.join(e for e in article.strip() if (e.isalpha() or e == " " or e == "-"))
    #return replace_punctuation
    doc = ""
    for e in article.strip():
        if(e.isalpha() or e == " " or e == "-"):
            doc += e
        else:
            doc += " "

    return doc

if __name__ == "__main__":

    articles = []

    with open('../data/FINAL.csv') as readfile, open('../data/no_punctuation.csv','w') as writefile:
        reader = csv.DictReader(readfile)

        fieldnames = ['title', 'category','content']
        writer = csv.DictWriter(writefile, fieldnames=fieldnames)

        for row in reader:
            articles.append(row)

        writer.writeheader()
        for a in articles:
            ar = a['content']
            #ar = regex na mag remove sa 24-anyos, 24,
            writer.writerow({'title':a['title'], 'category':a['category'],'content':removePunctuationAndNumbers(ar)})
