#this one is the last submitted and the accuracy improve due to the 
# number of outnode has been set equaltoone and the number of layer has been st toincreaseto 35and70 in second layer


# code is inspired but below tutorial :-
# http://bit.ly/2g2h2hw  # using the cnn from the keras library and pandas for file reading
import pandas as pd
import numpy as np
import keras.utils.np_utils as Kerasutlty
from keras.callbacks import EarlyStopping
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten

# this is the r code for taking input do according to this
args <- commandArgs(trailingOnly = TRUE)
trainingfile = args[0]
testingfile = args[1]
# #trainingfile  = "input/train.csv"
# #testingfile = "input/test.csv";
# inputtrain = read_csv(trainingfile)
# inputtest  = read_csv(testingfile)


# Read the train and test datasets
allTrain = pd.read_csv(trainingfile).values
test  = pd.read_csv(testingfile).values


#cmdinput = sys.argv[1:]
#trainingfile = cmdinput[0];
#testingfile = cmdinput[1];
#allTrain = pd.read_csv(trainingfile).values
#test = pd.read_csv(testingfile).values
RowinImg = 28
ColinImg = 28
StepSize = 160  # Number of images used in each optimization step
nb_epoch = 150  # Number of times the whole data is used to learn
#only fifttenran and then excited
XTrain = allTrain[:, 1:].reshape(allTrain.shape[0], RowinImg, ColinImg, 1)
XTrain = XTrain.astype('float32')
XTrain /= 255.0

YTrain = Kerasutlty.to_categorical(allTrain[:, 0],10) # change is here i am adding the number of neuron in output layer to be 10 
classNo = YTrain.shape[1]


def DefineModel():
    CNNPredictor = Sequential()
    # this will be the first layer
    CNNPredictor.add(Convolution2D(35, 5, 5, border_mode='valid', init='normal', input_shape=(RowinImg, ColinImg, 1)))
    CNNPredictor.add(Activation('relu'))
    CNNPredictor.add(MaxPooling2D(pool_size=(2, 2)))  # 2 = pool sixe nb_poal

    # this will be the second layer
    CNNPredictor.add(Convolution2D(70, 5, 5, border_mode='valid', init='normal'))
    CNNPredictor.add(Activation('relu'))
    CNNPredictor.add(MaxPooling2D(pool_size=(2, 2)))  # 2 = pool sixe nb_poal

    CNNPredictor.add(Flatten())
    CNNPredictor.add(Dense(1024, init='he_normal'))
    CNNPredictor.add(Activation('relu'))
    CNNPredictor.add(Dropout(0.5))
    CNNPredictor.add(Dense(classNo, init='he_normal'))
    CNNPredictor.add(Activation('softmax'))
    CNNPredictor.compile(loss='categorical_crossentropy', optimizer="adam", metrics=["accuracy"])
    return CNNPredictor


CNNPredictor = DefineModel();
early_stop = EarlyStopping(monitor='val_acc', patience=3, verbose=1, mode='max')

CNNPredictor.fit(XTrain, YTrain, batch_size=StepSize, nb_epoch=nb_epoch, show_accuracy=True, verbose=2,
                 validation_split=.1, callbacks=[early_stop])

Xtest = test.reshape(test.shape[0], RowinImg, ColinImg, 1)
Xtest = Xtest.astype('float32')
Xtest /= 255.0
YTest = CNNPredictor.predict_classes(Xtest, verbose=0)

np.savetxt('output.csv', np.c_[range(1, len(YTest) + 1), YTest], delimiter=',', header='ImageId,Label', comments='',
           fmt='%d')
