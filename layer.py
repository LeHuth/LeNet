inputs = [1, 2, 3, 2.5]
weigths = [ [0.2, 0.8, -0.5, 1],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

layer_outputs = []#output of the layer

for neuron_weights, neuron_bias in zip(weigths, biases): #iterating over weights and biases

    neuron_output = 0 # setting each neuron_output to 0

    for n_input, weight in zip(inputs, neuron_weights):# iterating over input and corresponding weight
        neuron_output += n_input*weight#calculating output for each neuron

    neuron_output += neuron_bias #adding the bias

    layer_outputs.append(neuron_output) #push result into output array

print(layer_outputs)
