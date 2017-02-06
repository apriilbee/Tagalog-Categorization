import re
import sys
import csv
import enchant
from nltk.corpus import stopwords


infix = ['um', 'in'] ##list of infix
prefix = ['makapang','nakapang','nakapan','makapan','nakapam','makapam','nakapag','makapag','nagpati','magpati','nagpaka','magpaka',
    'magpapa','nagpapa','nagkaka','magkaka','ipakipa','ikapang','naipag','mangag','nangag','kasing','ipang','pinag','papag','mapag', 'kapag',
    'napag','ipaki','magka','magsi','nagka','magma','nagma','magpa','nagpa','maipa','naipa','kasim','pagpa','paka','paki','pang','ipag',
    'mang','nang','maka','naka','mapa','napa','ika','pag','isa','ipa','mai','nai','mag','nag','man','nan','mam','nam','ma','na','ka','pa']
suffix = ['han', 'hin', 'an','in'] #suffixes
vowel = ['a','e','i','o','u']

def strip_infix(word):
    for inf in infix:
        if (inf in word):
            start_pos = re.search(inf, word).start()
            end_pos = re.search(inf, word).end()

            #checks the position of infix; removes infix only if in the middle, start position, or word length > 3
            if (start_pos >= 0 and end_pos < len(word) and len(word) > 4):
                #if word ! in dictionary
                word = re.sub(inf,'',word,1)

    return word

###

def strip_suffix(word):
    for suf in suffix:
        if (suf in word):
            if(word.endswith(suf) and len(word) > 4):
                word = re.sub(suf+'$','',word,1)

    return word

###

def strip_prefix(word):
    for pre in prefix:
        if (pre in word):
            if(word.startswith(pre) and len(word) > 5):
                word = re.sub(pre,'',word,1)

        if word.startswith("-"):
            word = word[1:]

        # checks reduplication of vowel prefixes
        for char in vowel:
            if(word.startswith(char) and len(word) > 1):
                if(word[0] == word[1]):
                    word = word[1:]

        word = check_reduplication(word)

    return word

###
def check_reduplication(word):
    for i in range(1,3):
        if word[:i] == word[i:i+i]:###python substring;
            word= word[i:]
            break
    return word

###

def stem(document):
    eng = enchant.Dict("en_US")
    words = []
    for word in document.split():
        if eng.check(word):
            words.append(word)
        else:
            words.append(check_reduplication(strip_prefix(strip_suffix(strip_infix(word.strip()).strip().strip()))))

    doc = ' '.join(word for word in words)
    return doc


if __name__ == "__main__":
    # wordfile = open(sys.argv[1])
    # for word in wordfile.readlines():
    #     print word,check_reduplication(strip_prefix(strip_suffix(strip_infix(word.strip()).strip().strip()))),"\n"
    articles = []

    with open('../data/no_stopwords.csv') as readfile, open('../data/stemmed_.csv','w') as writefile:
        reader = csv.DictReader(readfile)

        fieldnames = ['title', 'category','content']
        writer = csv.DictWriter(writefile, fieldnames=fieldnames)

        for row in reader:
            articles.append(row)

        writer.writeheader()
        ctr = 0
        for a in articles:
            ar = a['content'].lower()
            writer.writerow({'title':a['title'], 'category':a['category'],'content':stem(ar)})
            print ctr
            ctr += 1
