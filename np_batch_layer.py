import numpy as np

inputs = [  [1.0, 2.0, 3.0, 2.5],
            [2.0, 5.0, -1.0, 2.0],
            [-1.5, 2.7, 3.3, -0.8]]

weights = [ [0.2, 0.8, -0.5, 1],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

weights_2= [[0.1, -0.14, 0.5],
            [-0.5, 0.12, -0.33],
            [-0.44, 0.73, -0.13]]

biases_2 = [-1, 2, -0.5]

layer_outputs = np.dot(inputs, np.array(weights).T) + biases

layer_2_outputs = np.dot(layer_outputs, np.array(weights_2).T) + biases_2
#             =[np.dot(weights[0], inputs), np.do(weights[1], inputs)]
print(layer_2_outputs)
