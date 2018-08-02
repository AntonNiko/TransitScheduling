import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from theano import *
import theano.tensor as T


class Schedule_nn():
    input_data = []
    output_data = []

    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(32, input_shape=(700,4)))
        self.model.add(Activation("relu"))
        self.model.add(Dense(10))
        self.model.add(Activation("softmax"))

        self.model.compile(loss="categorical_crossentropy",
                           optimizer="adam",
                           metrics=["accuracy"])

    def trainNetwork(self):
        self.model.fit(self.input_data,
                       self.output_data,
                       batch_size=32,
                       nb_epoch=10,
                       verbose=1)

    def evaluateNetwork(self):
        self.model.evaluate(self.input_data,
                            self.output_data,
                            verbose=0)
                       
        
