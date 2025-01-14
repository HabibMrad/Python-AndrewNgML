import numpy as np
import matplotlib.pyplot as plt
import checker as op
import ex4helper as helper
import math
import matplotlib.image as mpimg
from numpy import linalg as LA


def main():
    checkNNGradients(0)


def checkNNGradients(lambdaVal):
    #   CHECKNNGRADIENTS(lambda) Creates a small neural network to check the
    #   backpropagation gradients, it will output the analytical gradients
    #   produced by your backprop code and the numerical gradients (computed
    #   using computeNumericalGradient). These two gradient computations should
    #   result in very similar values.
    #

    inputLayerSize = 3
    hiddenLayerSize = 5
    numLabels = 3
    m = 5

    # We generate some 'random' test data
    theta1 = debugInitializeWeights(hiddenLayerSize, inputLayerSize)
    theta2 = debugInitializeWeights(numLabels, hiddenLayerSize)

    # Reusing debugInitializeWeights to generate X
    X = debugInitializeWeights(m, inputLayerSize - 1)
    y = np.remainder(np.arange(m), numLabels) + 1

    # unroll parameters
    nnParams = np.append(theta1.flatten(), theta2.flatten())

    # calculate gradient with backprop
    grad = helper.BackPropagation(
        nnParams,
        inputLayerSize,
        hiddenLayerSize,
        numLabels,
        X,
        y,
        lambdaVal)

    # calculate difference between backprop and numerical gradient
    diff = op.check_grad(
        costMask,
        backPropMask,
        nnParams,
        inputLayerSize,
        hiddenLayerSize,
        numLabels,
        X,
        y,
        lambdaVal,
        epsilon=.0001)

    numGrad = op.approx_fprime(
        nnParams,
        costMask,
        .001,
        inputLayerSize,
        hiddenLayerSize,
        numLabels,
        X,
        y,
        lambdaVal)

    # Visually examine the two gradient computations.
    # The two columns you get should be very similar.
    print('\nComparing Gradients: (numGrad, grad, absolute difference)')

    for i in range(numGrad.shape[0]):
        print("{}: {:.9f}, {:.9f} {:.9f}".format(
            i+1,
            numGrad[i],
            grad[i],
            abs(numGrad[i] - grad[i])))

    print('The above left two columns you get should be very similar.')
    print('(Left-Your Numerical Gradient, Right-Analytical Gradient)')

    # Evaluate the norm of the difference between two solutions.
    # If you have a correct implementation
    # and you used EPSILON = 0.0001
    # in computeNumericalGradient,
    # then diff below should be less than 1e-9

    print('If your backpropagation implementation is correct, then ')
    print('the relative difference will be small (less than 1e-9).')
    print('Relative Difference: {}'.format(diff))


def debugInitializeWeights(fanOut, fanIn):
    # Initialize W using "sin", this ensures that  vW is always of the same
    # values and will be useful for debugging
    # numel ~ number of elements. equivalent to size, w.size
    # size, equivalent of shape, w.shape

    W = np.arange(fanOut*(fanIn+1))
    W = W.reshape(fanOut, fanIn+1)
    W = np.sin(W)/10
    return W


def backPropMask(nnParams, *args):
    return helper.BackPropagation(nnParams, *args)


def costMask(nnParams, *args):
    return helper.nnCostFunction(nnParams, *args)

if __name__ == '__main__':
    main()
