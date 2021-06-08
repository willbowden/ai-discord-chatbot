import os
import importlib
from util import wbjson
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
import numpy as np
from .use import embed

async def train_ai():
    data = wbjson.ReadToRaw("dataset.json")
    trainingData = []

    for intent in data.keys():
        for msg in data[intent]["patterns"]:
            trainingData.append({"type": intent, "message": msg})

    sentences = list(map(lambda i: i["message"].lower(), trainingData))
    xTrain = embed(sentences)
    yList = list(map(lambda x: [1 if x["type"] == "greeting" else 0, 1 if x["type"] =="goodbye" else 0, 1 if x["type"] == "insult" else 0, 1 if x["type"] == "compliment" else 0], trainingData))
    yTrain = tf.constant(yList)

    model = Sequential()
    model.add(Dense(128, input_shape=(len(xTrain[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(yTrain[0]), activation='softmax'))

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    model.fit(np.array(xTrain), np.array(yTrain), epochs=200, batch_size=5, verbose=1)
    model.save("david2_model")
    return model