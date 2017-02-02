import csv
import string

def removePunctuation(article):
    replace_punctuation = string.maketrans("!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~", ' '*(len(string.punctuation)-1))
    return article.translate(replace_punctuation)

if __name__ == "__main__":

    articles = []

    with open('../data/FINAL.csv') as readfile, open('../data/stripped_punctuations.csv','w') as writefile:
        reader = csv.DictReader(readfile)

        fieldnames = ['title', 'category','content']
        writer = csv.DictWriter(writefile, fieldnames=fieldnames)

        for row in reader:
            articles.append(row)

        writer.writeheader()
        for a in articles:
            ar = a['content']
            #ar = regex na mag remove sa 24-anyos, 24,
            writer.writerow({'title':a['title'], 'category':a['category'],'content':removePunctuation(ar)})
