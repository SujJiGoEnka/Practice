from __future__ import absolute_import, division, print_function

import tensorflow as tf
from tensorflow import keras
import os
import numpy as np
import json
import re

checkpoint_path = "E:/Important Code/saved/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create checkpoint callback
# cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
#                                                  save_weights_only=True,
#                                                  verbose=1)

def convert_integers(mystr):
#     mystr = 'This was a very good movie but acting is too bad'.lower()
    wordList = re.sub("[^\w]", " ", mystr.lower()).split()
    print(wordList)
    with open('E:/Important Code/index.json', 'r') as f:
        nums = []
        array = json.load(f)
        for i in range(len(wordList)):
            value = array.get(wordList[i])
            if value == None:
                continue
            nums.insert(i, int(value) + 3) 
    return nums    

print(tf.__version__)

imdb = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)



# A dictionary mapping words to an integer index
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

# print(train_data[0])
# print(train_data[2])
#  
# print(decode_review(train_data[0]))
# print(decode_review(train_data[2]))
train_data = keras.preprocessing.sequence.pad_sequences(train_data,
                                                        value=word_index["<PAD>"],
                                                        padding='post',
                                                        maxlen=256)
 
test_data = keras.preprocessing.sequence.pad_sequences(test_data,
                                                       value=word_index["<PAD>"],
                                                       padding='post',
                                                       maxlen=256)

# print(len(train_data[0]), len(train_data[1]))
# print(train_data[0])

# input shape is the vocabulary count used for the movie reviews (10,000 words)
vocab_size = 18000

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


# model.predict(x, batch_size, verbose, steps, max_queue_size, workers, use_multiprocessing)
print("Starting model evaluation-->")
eval_result = model.evaluate(test_data, test_labels)
print(eval_result)
# print(results)
print("Starting model prediction-->")

# print(train_data[0])

# print(decode_review(train_data[1]))
text = "Overall, I can say now that the “Isle of Dogs” has probably become the first cartoon in my life that I truly love. I admit that I would not have watched it if Wes Anderson’s name was not on it, but I am glad I did. The “Isle of Dogs” is a fine example of taste, talent, and hard work put together. A great movie to watch on your own or with your family."
# feed_data = np.array([train_data[1]])
# feed_data = np.array([[14, 20, 9, 24, 15, 87, 179, 550, 5, 1499, 229, 151, 116, 9, 55, 52, 65, 186, 8, 30, 753]])
feed_data = np.array([convert_integers(text)])
# [[ 14  20 186   8  30 357]]
print(feed_data)
pred_result = model.predict(feed_data)
# print("Model prediction = ", pred_result)

# print("saving checkpoint")
# saver = tf.train.Saver()
# init_op = tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init_op)
#     save_path = saver.save(sess, "E:/Important Code/saved/model.ckpt")

model.load_weights(checkpoint_path)
loss,acc = model.evaluate(x_val, y_val)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))
pred_result = model.predict(feed_data)
print("Model prediction = ", pred_result)
print("End")

    


