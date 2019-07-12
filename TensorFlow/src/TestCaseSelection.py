print("START-->")

# MLP for the IMDB problem
import numpy
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# ************** Prapare input data************************

word_index = imdb.get_word_index()
 
# The first indices are reserved
word_index = {k:(v+3) for k,v in word_index.items()} 
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3
 
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()]) 
 
def decode_review(textList):
    decoded_List=[]
    for text in textList:
        decoded_text= ' '.join([reverse_word_index.get(i, '?') for i in text])
        decoded_List.append(decoded_text) 
    
#     return ' '.join([reverse_word_index.get(i, '?') for i in text])
    return decoded_List


# load the dataset but only keep the top n words, zero the rest
top_words = 10000
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=top_words)
x_train_str = decode_review(x_train)
x_test_str = decode_review(x_test)

#Data conversion from string to integer
print("Data conversion starts-->")
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
vectorizer.fit(x_train_str+x_test_str)



x_train = vectorizer.transform(x_train_str).toarray()
x_test  = vectorizer.transform(x_test_str).toarray()
print("Data conversion ends-->")
print("Number of training examples-->",len(x_train))
print("Number of testing examples-->",len(x_test))
print(x_train[0])


from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier.fit(x_train, y_train)
score = classifier.score(x_test, y_test)

print("Accuracy:", score)
x_predict = vectorizer.transform([
#                                     "This movie is good",
#                                   "Story is very dull",
#                                   "the 1 point from me",
#                                   "The 8 points from me",
#                                   "Acting is good but overall dull movie",
                                  "Acting is bad but overall nice movie",
                                  "story is useless",
                                  "want my money back"
                                  ]).toarray()
result=classifier.predict(x_predict)
print("Prediction-->",result)
print("End-->")