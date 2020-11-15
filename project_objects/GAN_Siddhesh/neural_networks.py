# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:02:15 2020

@author: Siddhesh
"""

#Referred 
#https://github.com/DLangerr/dcgan-mnist-tensorflow/blob/master/discriminator.py
#https://github.com/DLangerr/dcgan-mnist-tensorflow/blob/master/generator.py

#Importing required libraries
import tensorflow as tf
import helper_functions as hf

#Creating the Discriminator Class
class Discriminator:
    
    #Initializing the variables
    def __init__(self, img_shape):
        
        #Retrieving the width, height and color channels of the image
        self.img_rows, self.img_cols, self.channels = img_shape
        
        #Defining the layer sizes
        layer_sizes = [64, 64, 128, 256]
        
        #Creating a variable scope for the Discriminator
        with tf.compat.v1.variable_scope('d'):
            
            #Displaying to the user
            print("Initializing the weights of the Discriminator")
            
            #Initializing the weights and bias
            self.W1 = hf.init_weights(shape = [5, 5, self.channels, layer_sizes[0]])
            self.b1 = hf.init_bias(shape = [layer_sizes[0]])
            self.W2 = hf.init_weights(shape = [3, 3, layer_sizes[0], layer_sizes[1]])
            self.b2 = hf.init_bias(shape = [layer_sizes[1]])
            self.W3 = hf.init_weights(shape = [3, 3, layer_sizes[1], layer_sizes[2]])
            self.b3 = hf.init_bias(shape = [layer_sizes[2]])
            self.W4 = hf.init_weights(shape = [2, 2, layer_sizes[2], layer_sizes[3]])
            self.b4 = hf.init_bias(shape = [layer_sizes[3]])
            self.W5 = hf.init_weights(shape = [7 * 7 * layer_sizes[3], 1])
            self.b5 = hf.init_bias(shape = [1])
                
    #Creating a function for forward passing
    def forward(self, X, momentum = 0.5):
        
        #No use of pooling layers. Using stride distance of 2 in order to reduce image size instead.
        #Throughout the layers, image size changes from 28x28x1 -> 14x14x64 -> 14x14x64 -> 7x7x128 -> 7x7x256
        
        #Reshaping the data
        X = tf.reshape(X, [-1, self.img_rows, self.img_cols, self.channels])
        
        #Creating the first conv block of the neural network
        #Performing a 2D convolution with stride[batch, width, height, channel] distance 2x2
        z = hf.Conv2D(X, self.W1, [1, 2, 2, 1], padding = "SAME")
        #Adding a bias
        z = tf.nn.bias_add(value = z, bias = self.b1)
        #Adding a leaky relu activation function
        z = tf.nn.leaky_relu(features = z)
        
        #Creating the second conv block of the neural network
        #Performing a 2D convolution with stride[batch, width, height, channel] distance 1x1
        z = hf.Conv2D(z, self.W2, [1, 1, 1, 1], padding = "SAME")
        #Adding a bias
        z = tf.nn.bias_add(value = z, bias = self.b2)
        #Adding a Batch Normalization layer
        z = tf.compat.v1.layers.batch_normalization(z, momentum = momentum)
        #Adding a leaky relu activation function
        z = tf.nn.leaky_relu(features = z)

        #Creating the third conv block of the neural network
        #Performing a 2D convolution with stride[batch, width, height, channel] distance 2x2
        z = hf.Conv2D(z, self.W3, [1, 2, 2, 1], padding = "SAME")
        #Adding a bias
        z = tf.nn.bias_add(value = z, bias = self.b3)
        #Adding a Batch Normalization layer
        z = tf.compat.v1.layers.batch_normalization(z, momentum = momentum)
        #Adding a leaky relu activation function
        z = tf.nn.leaky_relu(features = z)

        #Creating the fourth conv block of the neural network
        #Performing a 2D convolution with stride[batch, width, height, channel] distance 1x1
        z = hf.Conv2D(z, self.W4, [1, 1, 1, 1], padding = "SAME")
        #Adding a bias
        z = tf.nn.bias_add(value = z, bias = self.b4)
        #Adding a Batch Normalization layer
        z = tf.compat.v1.layers.batch_normalization(z, momentum = momentum)
        #Adding a leaky relu activation function
        z = tf.nn.leaky_relu(features = z)
        
        #Creating a Fully Conncected Layer
        #Flattening the image
        z = tf.reshape(tensor = z, shape = [-1, 7 * 7 * 256])
        #Defining the output
        logits = tf.matmul(a = z, b = self.W5)
        #Adding a bias
        logits = tf.nn.bias_add(value = logits, bias = self.b5)
        
        #Returning the output
        return logits
    
#Creating the Generator Class
class Generator:
    
    #Initializing the variables
    def __init__(self):
        
        #Defining the layer sizes
        self.layer_sizes = [512, 256, 128, 1]
        
        #Creating a variable scope for the Generator
        with tf.compat.v1.variable_scope('g'):
            
            #Displaying to the user
            print("Initializing the weights of the Generator")
            
            #Initializing the weights
            self.W1 = hf.init_weights(shape = [100, 7 * 7 * self.layer_sizes[0]])
            self.W2 = hf.init_weights(shape = [3, 3, self.layer_sizes[0], self.layer_sizes[1]])
            self.W3 = hf.init_weights(shape = [3, 3, self.layer_sizes[1], self.layer_sizes[2]])
            self.W4 = hf.init_weights(shape = [3, 3, self.layer_sizes[2], self.layer_sizes[3]])
            
    #Creating a function for forward passing
    def forward(self, X, momentum = 0.5):
        
        #Creating an Inverse Fully Conncected Layer
        #Defining the input
        z = tf.matmul(a = X, b = self.W1)
        #Adding a relu activation function
        z = tf.nn.relu(features = z)
        #Reshaping the data into a 4D tensor
        z = tf.reshape(tensor = z, shape = [-1, 7, 7, self.layer_sizes[0]])
        
        #Creating the first conv block of the neural network
        #Increasing the image size by upsampling
        z = tf.keras.layers.UpSampling2D(size = (2, 2))(z)
        #Performing a 2D convolution with stride[batch, width, height, channel] distance 1x1
        z = hf.Conv2D(X = z, filters = self.W2, strides = [1, 1, 1, 1], padding = "SAME")
        #Adding a Batch Normalization layer
        z = tf.compat.v1.layers.batch_normalization(z, momentum = momentum)
        #Adding a leaky relu activation function
        z = tf.nn.leaky_relu(features = z)
        
        #Creating the second conv block of the neural network
        #Increasing the image size by upsampling
        z = tf.keras.layers.UpSampling2D(size = (2, 2))(z)
        #Performing a 2D convolution with stride[batch, width, height, channel] distance 1x1
        z = hf.Conv2D(X = z, filters = self.W3, strides = [1, 1, 1, 1], padding = "SAME")
        #Adding a Batch Normalization layer
        z = tf.compat.v1.layers.batch_normalization(z, momentum = momentum)
        #Adding a leaky relu activation function
        z = tf.nn.leaky_relu(features = z)
        
        #Creating the output layer of the neural network
        z = hf.Conv2D(X = z, filters = self.W4, strides = [1, 1, 1, 1], padding = "SAME")
        #Adding a hyperbolic tangent activation function
        output = tf.nn.tanh(x = z)
        
        #Returning the output
        return output