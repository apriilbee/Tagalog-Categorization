import csv

words = []

def add_to_dict(document):
    for word in document.split():
        if word not in words:
            words.append(word.strip())

def write_file():
    out = open("../data/bag_of_words.txt", 'w')
    for word in words:
        out.write("%s\n" % word)

if __name__ == "__main__":

    articles = []

    with open('../data/stemmed_.csv') as readfile:
        reader = csv.DictReader(readfile)

        fieldnames = ['title', 'category','content']

        for row in reader:
            articles.append(row)

        ctr = 0
        for a in articles:
            ar = a['content'].lower()
            add_to_dict(ar)
            print ctr
            ctr += 1

    write_file()
