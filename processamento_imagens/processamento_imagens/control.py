#importando bibliotecas 
import tensorflow as tf
import keras
import numpy as np
from keras.preprocessing import image
from keras.applications import vgg16
import matplotlib.pyplot as plt
from pathlib import Path
import os

def read_img(path):
     img = keras.utils.load_img(path, target_size=(224,224))
     image_array = tf.keras.utils.img_to_array(img)
     return image_array

def train_model(image_array):
    x_train = np.expand_dims(image_array, axis=0)
    #Parametrizando dados
    x_train = vgg16.preprocess_input(x_train)
    return x_train

def predict_model(x_train , path : None):
    model = vgg16.VGG16(weights="imagenet")
    prediction = model.predict(x_train)
    pred = vgg16.decode_predictions(prediction)
    data = plt.imread(path)
    plt.imshow(data)
    plt.show()
    print(pred)