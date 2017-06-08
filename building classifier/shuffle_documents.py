import random

# with open('../data/no_stopwords.csv') as f:
#     data = f.readlines()

with open('../data/experiment1/stemmed_.csv') as f:
    data = f.readlines()

header, rest = data[0], data[1:]
random.shuffle(rest)

with open('../data/experiment1/shuffled_updated.csv', 'w') as out:
    out.write(''.join([header]+rest))
