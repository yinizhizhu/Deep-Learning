import numpy as np
import matplotlib.pyplot as plt
#
# a = np.random.randn(2,3)
# print(a)
# print(a.shape)
#
#
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

import network

lee = network.Network([784, 100, 10])
lee.SGD(training_data, 10, 10, 3.0, test_data)