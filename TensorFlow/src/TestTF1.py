# coding=utf8
from __future__ import absolute_import, division, print_function

import csv
import tensorflow as tf
from tensorflow import keras
import os
import numpy as np
import json
import re

checkpoint_path = "E:/Important Code/saved/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
review = []
vocab_size = 88000

###########CODE USED TO SAVE TENSORFLOW MODEL#############
# Create checkpoint callback
cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)


def convert_integers(mystr):
    wordList = re.sub("[^\w]", " ", mystr.lower()).split()
#     print(wordList)
    with open('E:/Important Code/index.json', 'r') as f:
        nums = []
        array = json.load(f)
        for i in range(len(wordList)):
            value = array.get(wordList[i])
            if value == None or value > vocab_size:
                continue
            nums.insert(i, int(value) + 3) 
    return nums    


def read_csv(file_obj):   
    reader = csv.DictReader(file_obj, delimiter=',')
    count = 0
    for line in reader:
        review.insert(count, [line["review"]])
        count = +1

#----------------------------------------------------------------------

if __name__ == "__main__":
    with open('E:/Important Code/IMDB/imdb.csv') as f_obj:
        read_csv(f_obj)        
                
print("TensorFlow Version", tf.__version__)

imdb = keras.datasets.imdb
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)



word_index = imdb.get_word_index()
# The first indices are reserved
word_index = {k:(v + 3) for k, v in word_index.items()} 
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])


def decode_review(text):
    return ' '.join([reverse_word_index.get(i, '?') for i in text])

print("Pre-Processed Data: ",train_data[0])

print("Actual Text: ",decode_review(train_data[0]))

# Code used for padding
train_data = keras.preprocessing.sequence.pad_sequences(train_data,
                                                        value=word_index["<PAD>"],
                                                        padding='post',
                                                        maxlen=256)
 
test_data = keras.preprocessing.sequence.pad_sequences(test_data,
                                                       value=word_index["<PAD>"],
                                                       padding='post',
                                                       maxlen=256)

# print(len(train_data[0]), len(train_data[1]))
print("After padding:")
print(train_data[0])

# input shape is the vocabulary count used for the movie reviews (10,000 words)
vocab_size = 18000

# Model
model = keras.Sequential()
model.add(keras.layers.Embedding(vocab_size, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation=tf.nn.relu))
model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))
model.summary()

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

x_val = train_data[:10000]
partial_x_train = train_data[10000:]

y_val = train_labels[:10000]
partial_y_train = train_labels[10000:]

print("Starting model training-->")
# history = model.fit(partial_x_train,
#                     partial_y_train,
#                     epochs=40,
#                     batch_size=512,
#                     validation_data=(x_val, y_val),
#                     verbose=1, callbacks=[cp_callback])
# use cp_callback variable to save checkpoint after every epochs

# model.predict(x, batch_size, verbose, steps, max_queue_size, workers, use_multiprocessing)
print("Starting model evaluation-->")
print("-------------------------------------------")
eval_result = model.evaluate(test_data, test_labels)
print(eval_result)
# print(results)
print("Starting model prediction-->")


# code for model restored
model.load_weights(checkpoint_path)
loss, acc = model.evaluate(x_val, y_val)
print("Restored model, accuracy: {:5.2f}%".format(100 * acc))

for x in review:
    text = str(x)[1:-1] 
    
    feed_data = np.array([convert_integers(text)])

    print(feed_data)
    pred_result = model.predict(feed_data)
    pred_result= "{:.6}".format(float(pred_result))
    print(text)
    pred_result = (float(pred_result))
    if pred_result <= 0.5 and pred_result >= 0:
        print(pred_result, end=": ")
        print("Review seems to be NEGATIVE")
    elif pred_result > 0.5 and pred_result <= 1:
        print(pred_result, end=": ")
        print("Review seems to be POSITIVE")
    else:
        print("Unable to predict") 
        print(pred_result, end=": ")   
    print("-------------------------------------------")

# pred_result=model.predict([[feed_data]])
# 
# print("Model prediction = ", pred_result)    
# print("Model prediction = ", pred_result)

# print("saving checkpoint")
# saver = tf.train.Saver()
# init_op = tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init_op)
#     save_path = saver.save(sess, "E:/Important Code/saved/model.ckpt")


# pred_result = model.predict(feed_data)
# print("Model prediction = ", pred_result)
# print("End")

    



