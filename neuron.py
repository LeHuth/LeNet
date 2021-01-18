#inputs
inputs = [1.0, 2.0, 3.0, 2.5]

#weights and biases are the values that change during the training phase
weights = [0.2, 0.8, -0.5, 1.0]

#only one bias per neuron
bias = 2.0

#neuron sums each input * weigth and adds the bias
output =   (inputs[0]*weights[0]+       #  1.0  * 0.2
            inputs[1]*weights[1]+       #+ 2.0  * 0.8
            inputs[2]*weights[2]+       #+ 3.0  * -0.5
            inputs[3]*weights[3]+bias)  #+ 2.5  * 1.0 + 2.0



print(output)
