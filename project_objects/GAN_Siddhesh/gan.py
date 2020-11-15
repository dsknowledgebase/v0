# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 00:43:29 2020

@author: Siddhesh
"""

#Referred https://github.com/DLangerr/dcgan-mnist-tensorflow/blob/master/dcgan.py

#Importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
import helper_functions as hf
from neural_networks import Generator, Discriminator

#Creating a Deep Convolutional Generative Adversarial Network
class DCGAN:
    
    #Initializing the variables
    def __init__(self, img_shape, sample_folder_name, iterations = 40000, lr_gen = 0.0001, lr_dc = 0.0003,
                 z_shape = 100, batch_size = 64, beta1 = 0.5, sample_interval = 500):
        
        #Creating a sample folder to save the images
        if not os.path.exists(f"{sample_folder_name}/"):
            
            #Creating the sample folder to save the images
            os.makedirs(f"{sample_folder_name}/")
            
        #Unpacking the image
        self.rows, self.cols, self.channels = img_shape
        
        #Initializing parameters
        self.sample_folder_name = sample_folder_name
        self.iterations = iterations
        self.z_shape = z_shape
        self.batch_size = batch_size
        self.sample_interval = sample_interval
        self.generator = Generator()
        self.discriminator = Discriminator(img_shape)
        
        #Loading the data
        mnist = tf.keras.datasets.mnist
        (x_train, _), (x_test, _) = mnist.load_data()
        
        #Combining the train and test images as validation data is not required for GANS
        X = np.concatenate([x_train, x_test], axis = 0)
        
        #Normalizing the data and mapping it between -1 and 1
        self.X = ((X / 255.0) * 2) - 1
        
        #Creating placeholders for the input
        self.phX = tf.compat.v1.placeholder(dtype = tf.float32, shape = [None, self.rows, self.cols, self.channels])
        self.phZ = tf.compat.v1.placeholder(dtype = tf.float32, shape = [None, self.z_shape])
        
        #Disabling eager execution
        #tf.compat.v1.enable_eager_execution()
        
        #Generating images
        self.gen_out = self.generator.forward(self.phZ)
        
        #Predicting whether the image is fake or real
        dc_logits_fake = self.discriminator.forward(self.gen_out)
        dc_logits_real = self.discriminator.forward(self.phX)
        
        #Calculating total loss of the Discriminator(real_image = 1, fake_image = 0)
        dc_loss_fake = hf.cost_func(labels = tf.zeros_like(input = dc_logits_fake), logits = dc_logits_fake)
        dc_loss_real = hf.cost_func(labels = tf.ones_like(input = dc_logits_real), logits = dc_logits_real)
        self.dc_loss = tf.add(x = dc_loss_fake, y = dc_loss_real)
        
        #Calculating total loss of the Generator(fake_image = 1)
        self.gen_loss = hf.cost_func(labels = tf.ones_like(input = dc_logits_fake), logits = dc_logits_fake)
        
        #Retrieving all trainable variables
        train_var = tf.compat.v1.trainable_variables()
        
        #Differentiating between variables of the Generator and Discriminator
        gen_var = [var for var in train_var if "g" in var.name]
        dc_var = [var for var in train_var if "d" in var.name]
        
        #Creating the training variables for the Generator and Discriminator
        self.dc_train = tf.compat.v1.train.AdamOptimizer(learning_rate = lr_dc, beta1 = beta1).minimize(loss = self.dc_loss, var_list = dc_var)
        self.gen_train = tf.compat.v1.train.AdamOptimizer(learning_rate = lr_gen, beta1 = beta1).minimize(loss = self.gen_loss, var_list = gen_var)
        
    #Creating a function to train the GAN
    def train(self):
        
        #Initializing global variables
        init = tf.compat.v1.global_variables_initializer()
        
        #Creating a tensorflow session
        self.sess = tf.compat.v1.Session()
        
        #Initializing all variables
        self.sess.run(init)
        
        #Starting the training loop
        for i in range(0, self.iterations):
            
            #Creating a random batch for training
            idx = np.random.randint(low = 0, high = len(self.X), size = self.batch_size)
            
            #Creating data for training the Discriminator
            batch_X = self.X[idx]
            batch_Z = np.random.uniform(low = -1, high = 1, size = (self.batch_size, self.z_shape))
            
            #Reshaping the training batch
            batch_X = batch_X.reshape([-1, 28, 28, 1])
            
            #Training the Discriminator
            _, d_loss = self.sess.run([self.dc_train, self.dc_loss], feed_dict = {self.phX : batch_X, self.phZ : batch_Z})
            
            #Creating data for training the Generator
            batch_Z = np.random.uniform(low = -1, high = 1, size = (self.batch_size, self.z_shape))
            
            #Training the Generator
            _, g_loss = self.sess.run([self.gen_train, self.gen_loss], feed_dict = {self.phZ : batch_Z})
            
            #Displaying to the user
            print(f"Epoch : {i}, Discriminator Loss : {d_loss}, Generator Loss : {g_loss}")
            
            #Generating samples and displaying the loss
            if(i % self.sample_interval == 0):
                
                #Generating samples
                self.generate_samples(i)
                
                #Displaying to the user
                print("")
                print("Sample Generated!")
                print("")
                
    #Creating a function to generate samples
    def generate_samples(self, iteration):
        
        #Creating a 5 x 5 grid
        r, c  = 5, 5
        
        #Creating a latent space to store generated images
        z = np.random.uniform(low = -1, high = 1, size = (25, self.z_shape))
        
        #Generating 25 images and storing them in the latent space
        imgs = self.sess.run(self.gen_out, feed_dict = {self.phZ : z})
        
        #Rescaling the images between 0 and 1
        imgs = 0.5 * imgs + 0.5
        
        #Creating subplots
        fig, ax = plt.subplots(r, c)
        
        #Initializing count to 0
        count = 0
        
        #Iterating through the grid
        for i in range(0, c):
            for j in range(0, r):
                
                #Plotting the images in the grid without an axis
                ax[i,j].imshow(imgs[count, :, :, 0], cmap = "gray")
                ax[i,j].axis("off")
                
                #Incrementing the value of count
                count += 1
                
        #Saving the grid of images in the required folder
        fig.savefig(f"{self.sample_folder_name}/{iteration}.png")
        plt.close()
        
#Writing the main program
if __name__ == "__main__":
    
    #Disabling eager execution
    tf.compat.v1.disable_eager_execution()
    
    #Specifying the shape of the image
    img_shape = (28, 28, 1)
    
    #Creating an object of the Deep Convolutional Generative Adversarial Network
    dcgan = DCGAN(img_shape, "samples")
    
    #Training the Deep Convolutional Generative Adversarial Network
    dcgan.train()