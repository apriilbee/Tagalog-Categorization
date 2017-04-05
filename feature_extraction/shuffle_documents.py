import random

with open('../data/experiment3/stemmed_.csv') as f:
    data = f.readlines()

header, rest = data[0], data[1:]
random.shuffle(rest)

with open('../data/experiment3/shuffled.csv', 'w') as out:
    out.write(''.join([header]+rest))
