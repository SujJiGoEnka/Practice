# coding=utf8
import tensorflow as tf
import numpy as np

ITERATOR_BATCH_SIZE = 3
NR_EPOCHS = 2

train1_path = 'C:/Users/suraj.goenka/Downloads/imdb_master.csv/sample.csv'

dataset = tf.contrib.data.CsvDataset(train1_path,
                                     [tf.string, tf.string],
                                     header=True)

dataset = dataset.map(lambda *x: tf.convert_to_tensor(x))
dataset = dataset.batch(ITERATOR_BATCH_SIZE)

with tf.Session() as sess:
    for i in range (NR_EPOCHS):
        print('\nepoch: ', i)
        iterator = dataset.make_one_shot_iterator()
        next_element = iterator.get_next()
        while True:            
            try:
                data_and_target = sess.run(next_element)
            except tf.errors.OutOfRangeError:
                break
            print("\n\n", data_and_target)