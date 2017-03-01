import csv
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

corpus = []

#  print len(vectorizer.get_feature_names())
#  print vectorizer.vocabulary_.get('patay')
#  print vectorizer.transform(['Dalawa patay sa giyera']).toarray()
#  print train_data_features.shape

# Sum up the counts of each vocabulary word
# dist = np.sum(train_data_features.toarray(), axis=0)
# vocab = vectorizer.get_feature_names()
# for tag, count in zip(vocab, dist):
#      print count, tag

# DO NEXT: STORE ANG VALUES SA CSV
# IBUTANG NA ANG 1 0 1 0 NA LABEL, MAKE COLUMNS FOR LABEL
# PWEDE NA DAYON I-FEED SA MODEL I THINK HUHUHUHUHUHU

#tf-idf
def vectorize():
    vectorizer = TfidfVectorizer(min_df=1)
    X = vectorizer.fit_transform(corpus)
    train_data_features = X.toarray()

#count only
def vectorizer():
     vectorizer = CountVectorizer(min_df=1)
     X = vectorizer.fit_transform(corpus)
     analyze = vectorizer.build_analyzer()
     train_data_features = X.toarray()
     #print train_data_features.shape



if __name__ == "__main__":
    with open('data/stemmed_.csv') as readfile:
        reader = csv.DictReader(readfile)
        fieldnames = ['title', 'category','content']

        for row in reader:
            corpus.append(row['content'].lower())

    vectorizer()
