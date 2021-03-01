import numpy as np

#inputs
inputs = [1.0, 2.0, 3.0, 2.5]

#weigths and biases are the values that change during the training phase
weights = [0.2, 0.8, -0.5, 1.0]

#only one bias per neuron
bias = 2.0

#neuron sums each input * weigth and adds the bias
output =   np.dot(weights, inputs) + bias
print(output)
