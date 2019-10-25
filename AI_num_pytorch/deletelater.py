import tensorflow as tf

x1 = tf.Variable(2.0)
x2 = tf.Variable(3.0)
x = tf.stack([x1,x2],0)

y1 = 5*x1+2*x2*x2
y2 = x1*x1+ 10*x2
y = tf.stack([y1,y2],0)

grad = tf.gradients(y, x)
print(x)
print(y)

err 

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    grad_value = sess.run(grad)
    print(grad_value)