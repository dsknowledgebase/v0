# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:34:38 2020

@author: Siddhesh
"""

#Referred https://github.com/DLangerr/dcgan-mnist-tensorflow/blob/master/ops.py

#Importing required libraries
import tensorflow as tf

#Creating a function to initialize weights
def init_weights(shape):
    
    #Initializing random weights
    weights = tf.Variable(initial_value = tf.random.truncated_normal(shape = shape, stddev = 1e-1))
    
    #Returning the weights
    return weights

#Creating a function to initialize bias
def init_bias(shape):
    
    #Initializing bias
    bias = tf.Variable(initial_value = tf.zeros(shape = shape))
    
    #Returning the bias
    return bias

# shape of input = [batch, in_height, in_width, in_channels]
# shape of filter = [filter_height, filter_width, in_channels, out_channels]
    
#Creating a function to perform a 2D Convolution
def Conv2D(X, filters, strides, padding):
    
    #Performing a 2D Convolution
    return tf.nn.conv2d(input = X, filters = filters, strides = strides, padding = padding)

#Creating a function to calculate the cost
def cost_func(labels, logits):
    
    #Calculating the cost
    cost = tf.reduce_mean(input_tensor = tf.nn.sigmoid_cross_entropy_with_logits(labels = labels, logits = logits))
    
    #Returning the cost
    return cost