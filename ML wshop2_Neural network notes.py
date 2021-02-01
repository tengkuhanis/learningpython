'''

no matter how complex the neural network is,
the output will always obtained with a sigmoid function
Y = .......

4 things:
actual input
actual output
initially guess weight
initially guess bias

bias, w1,w2,w3...and so on are completely random (initially)

2 things needed:
-cost/loss function
-optimizer - ADAM (2015) -> a modified version of
                            gradient descent algorithm

error: |actual-predited|

Structure:
-haw many input layer, how many hidden layers
-infinite possiblities for how many neurons in a hidden layer
-more neurons, more precise the neural network can be


things you will always see in machine learning:
Mean Square Error (MSE)

finding minimum point in a graph is also one type of optimization
            - this is how the gradient descent algorithm works
'''