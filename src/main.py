import mnist_loader

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

# print(training_data[1])
#
# i = raw_input("Start?")

import network

net = network.Network([784, 100, 10])
net.SGD(training_data, 30, 10, 3.0, test_data)
