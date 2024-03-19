import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from keras.utils.np_utils import to_categorical
from keras.layers import Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2
import os

## tf versão 2.0.0
##keras versão 2.3.1
 
### Parâmetros
path = "data"
batch_size_val=50
steps_per_epoch_val=1000
epochs_val=20
imageDimesions = (32,32,3)


## Importar Imagens
count = 0
images = []
classNo = []
pastas = os.listdir(path)
print("Total de Classes:",len(pastas))
noOfClasses=len(pastas)

for pt in range (0,len(pastas)):
    arquivos = os.listdir(path+"/"+str(count))
    for arq in arquivos:
        curImg = cv2.imread(path+"/"+str(count)+"/"+arq)
        images.append(curImg)
        classNo.append(count)

    count +=1

images = np.array(images)
classNo = np.array(classNo)
 
## Separando Imagens
X_train, X_test, y_train, y_test = train_test_split(images, classNo, test_size=0.2)
X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=0.2)

## Funções do pré-processamento das Imagens
def grayscale(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img
def equalize(img):
    img =cv2.equalizeHist(img)
    return img
def preprocessing(img):
    img = grayscale(img)     # Converter em Gray
    img = equalize(img)      # Padronizar a Luminosidade das imagens
    img = img/255            # normalizar valores para 0 e 1 em vez de 0 e 255
    return img

## Pré-processar imagens
X_train=np.array(list(map(preprocessing,X_train)))
X_validation=np.array(list(map(preprocessing,X_validation)))
X_test=np.array(list(map(preprocessing,X_test)))
 
## Regularizar Arrays
X_train=X_train.reshape(X_train.shape[0],X_train.shape[1],X_train.shape[2],1)
X_validation=X_validation.reshape(X_validation.shape[0],X_validation.shape[1],X_validation.shape[2],1)
X_test=X_test.reshape(X_test.shape[0],X_test.shape[1],X_test.shape[2],1)

## Aumentando Imagens com ImageDataGenerator
dataGen= ImageDataGenerator(width_shift_range=0.1,   # alterar posição width da imagem
                            height_shift_range=0.1,  # alterar posição hight da imagem
                            zoom_range=0.2,  # colocar zoom
                            shear_range=0.1,  # mudar ângulo
                            rotation_range=10)  # rotacionar imagem
dataGen.fit(X_train)
batches= dataGen.flow(X_train,y_train,batch_size=20)
X_batch,y_batch = next(batches)

y_train = to_categorical(y_train,noOfClasses)
y_validation = to_categorical(y_validation,noOfClasses)
y_test = to_categorical(y_test,noOfClasses)

## Criar Modelo
def myModel():
    model= Sequential()
    model.add(Conv2D(32,kernel_size=(5,5),input_shape=(imageDimesions[0],imageDimesions[1],1),activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Conv2D(64,kernel_size=(3,3),activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(128,activation='relu'))
    model.add(Dense(noOfClasses,activation='softmax'))

    # COMPILE MODEL
    model.compile(Adam(lr=0.001),loss='categorical_crossentropy',metrics=['accuracy'])
    return model

## Treinamento
model = myModel()
print(model.summary())

history=model.fit_generator(dataGen.flow(X_train,y_train,batch_size=batch_size_val),steps_per_epoch=steps_per_epoch_val,epochs=epochs_val,validation_data=(X_validation,y_validation),shuffle=1)

## Mostrar histórico de treinamento
plt.figure(1)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['training','validation'])
plt.title('loss')
plt.xlabel('epoch')
plt.figure(2)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.legend(['training','validation'])
plt.title('Acurracy')
plt.xlabel('epoch')
plt.show()
score =model.evaluate(X_test,y_test,verbose=0)
print('Test Score:',score[0])
print('Test Accuracy:',score[1])

## Salvar modelo
model.save('modelo.h5')
print('Modelo Salvo!')