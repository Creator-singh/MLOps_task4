from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import Sequential
model=Sequential()
model.add(Convolution2D(filters=32,kernel_size=(3,3),activation='relu',input_shape=(64, 64, 3) ))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(filters=32,kernel_size=(3,3),activation='relu))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(units=120, activation='relu'))
model.summary()
model.add(Dense(units=1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
from keras_preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('C:Faces//',target_size=(64, 64),batch_size=32,class_mode='binary')
test_set = test_datagen.flow_from_directory('C:FTest//',target_size=(64, 64),batch_size=32,class_mode='binary')
model.fit(training_set,steps_per_epoch=8000,epochs=5,validation_data=test_set,validation_steps=800)
m=model.save('FR.h5')
from keras.preprocessing import image
from keras.models import load_model
import cv2
#cap = cv2.VideoCapture(0)

test_image = image.load_img('C://Users//Singh//Documents//MLOPS//FTest//dk//Image2.jpg',target_size=(64,64))
test_image = image.img_to_array(test_image)
import numpy as np
test_image = np.expand_dims(test_image, axis=0)
#result = model.predict(test_image)
result = model.predict_classes(test_image)
print(result[0][0])
if result[0][0] == 0.0:
    print('F1')
else:
    print('F2')
img = cv2.imread('C://Users//Singh//Documents//MLOPS//FTest//dk//Image2.jpg')
 
cv2.imshow('sdf',img)
 
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows()
