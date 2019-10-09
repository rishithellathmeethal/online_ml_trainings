import math as math
import numpy as np
import matplotlib.pyplot as plt

#Machine learning libraries
from keras.models import Sequential
from keras.layers import LSTM,Dense

t =  np.arange(2000)
x = np.sin(0.01*t)
#print(t,x)
#plt.plot(t,x)
#plt.show()

# Create function to preprocess the data into 7 look back slices

def processData(dataX,dataY, lb):
    X,Y = [],[]
    for i in range(len(dataX)-lb-1):
        X.append(dataX[i:(i+lb)])
        Y.append(dataY[(i+lb)])
    return np.array(X),np.array(Y)

X,y = processData(t,x,7)

X_train,X_test = X[:int(X.shape[0]*0.80)],X[int(X.shape[0]*0.80):]
y_train,y_test = y[:int(y.shape[0]*0.80)],y[int(y.shape[0]*0.80):]
print(X_train.shape[0])
print(X_test.shape[0])
print(y_train.shape[0])
print(y_test.shape[0])

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#Build the model
model = Sequential()
model.add(LSTM(256,input_shape=(7,1)))
model.add(Dense(1))
model.compile(optimizer='adam',loss='mse')
#Reshape data for (Sample,Timestep,Features) 
X_train = X_train.reshape((X_train.shape[0],X_train.shape[1],1))
X_test = X_test.reshape((X_test.shape[0],X_test.shape[1],1))

#Fit model with history to check for overfitting
history = model.fit(X_train,y_train,epochs=300,validation_data=(X_test,y_test),shuffle=False)


plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])