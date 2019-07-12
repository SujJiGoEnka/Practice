import tensorflow as tf
ITERATOR_BATCH_SIZE = 2
NR_EPOCHS = 3
train1_path = 'E:\Text Files\data.csv'

dataset = tf.contrib.data.CsvDataset(train1_path,
                                     [tf.float32],
                                     header=True, field_delim=' ')

dataset = dataset.batch(ITERATOR_BATCH_SIZE)

with tf.Session() as sess:

    for i in range (NR_EPOCHS):
        print('\nepoch: ', i)
        iterator = dataset.make_one_shot_iterator()
        next_element = iterator.get_next()
        while True:            
            try:
              data_and_target = sess.run([next_element])
            except tf.errors.OutOfRangeError:
              break
            print("\n\n", data_and_target)