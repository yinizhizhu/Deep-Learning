import random, time
import numpy as np
import matplotlib.pyplot as plt

#####for the np.random.randn#####
# a = np.random.randn(2,3)
# print(a)
# print(a.shape)
#
#####for the random.shuffle#####
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a)
# random.shuffle(a)
# print(a)
# random.shuffle(a)
# print(a)
# print(a[1:1+3])

#####xrange(head, tail, gap)#####
# for k in xrange(0, 10, 3):
#     print k

# a = [3, 1, 2, 4, 6, 1]
# maxindex = 0
# i = 0
# for tmp in a:
#     if tmp > a[maxindex]:
#         maxindex = i
#     i += 1
# print(maxindex)
#
#####for the np.argmax#####
# a = np.array([3, 1, 2, 4, 6, 1])
# print(np.argmax(a))
#
# a = np.array([[1, 5, 5, 2],
#               [9, 6, 2, 8],
#               [3, 7, 9, 1]])
# print(np.argmax(a, axis=0)) #axis - a[0][j]
# print(np.argmax(a, axis=1)) #axis - a[j][0]

#####for the np.dot#####
# # 2-D array: 2 x 3
# one = np.array([[1, 2, 3], [4, 5, 6]])
# # 2-D array: 3 x 2
# two = np.array([[1, 2], [3, 4], [5, 6]])
#
# res = np.dot(one, two)
# print('two_multi_res: %s' %(res))
#
# # 1-D array:
# one = np.array([1, 2, 3])
# two = np.array([4, 5, 6])
# res = np.dot(one, two)
# print('one_result_res: %s' %(res))

import mnist_loader

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

#####for the feedforward, sigmod#####
# sizes = [784, 100, 10]
# biases = [np.random.randn(y, 1) for y in sizes[1:]]
# weights = [np.random.randn(y, x)
#                 for x, y in zip(sizes[:-1], sizes[1:])]
#
# pic = training_data[0][0];
# im = np.reshape(pic, (28, 28))
# plt.figure()
# plt.imshow(im, cmap='gray')
# plt.show()
# score = training_data[0][1];
# print(score)
#
# def feedforward(a):
#     """Return the output of the network if ``a`` is input."""
#     for w, b in zip(weights, biases):
#         a = sigmoid(np.dot(w, a) + b)
#         # print(len(a))
#         # print(a)
#     return a
#
# def sigmoid(z):
#     """The sigmoid function."""
#     return 1.0/(1.0+np.exp(-z))
# ans = feedforward(pic)
#
# print(len(ans))
# print(ans)
#
# print(len(ans))
# print(ans-score)

# def evaluate1(test_data):
#     test_results = [(np.argmax(feedforward(x)), y)
#                     for (x, y) in test_data]
#     return sum(int(x == y) for (x, y) in test_results)
#
# def evaluate2(test_data):
#     counter = 0
#     for (x, y) in test_data:
#         if np.argmax(feedforward(x)) == y:
#             counter += 1
#     return counter
#
# s = time.time()
# for i in xrange(10):
#     evaluate1(test_data)
# print "The running time is {0}" .format(time.time()-s)
# s = time.time()
# for i in xrange(10):
#     evaluate2(test_data)
# print "The running time is {0}" .format(time.time()-s)

import network

f = open('result.txt', 'w')
print >> f, 'The Network with [{0}, {1}]\n'.format(784, 10)
lee1 = network.Network([784, 10])
lee1.SGD(f, training_data, 30, 10, 1.2, test_data)

print >> f, 'The Network with [{0}, {1}, {2}]\n'.format(784, 30, 10)
lee2 = network.Network([784, 30, 10])
lee2.SGD(f, training_data, 30, 10, 1.2, test_data)
f.close()