import tensorflow as tf

sess = tf.Session()
new_saver = tf.train.import_meta_graph('E:/Important Code/saved/my-model.meta')
new_saver.restore(sess, tf.train.latest_checkpoint('E:/Important Code/saved/'))
all_vars = tf.get_collection('vars')
for v in all_vars:
    v_ = sess.run(v)
    print(v_, end="")