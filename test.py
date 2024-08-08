import os
import numpy as np
import cv2
import random
dogfd='C:/Users/thispc/Downloads/archive1/training_set/training_set/dogs'
catfd='C:/Users/thispc/Downloads/archive1/training_set/training_set/cats'
x=400
select_dog=random.sample(os.listdir(dogfd),x)
select_cat=random.sample(os.listdir(catfd),x)
imgv=[]
nhan=[]
for filename in select_dog:
   img_path=os.path.join(dogfd,filename)
   img=cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
   nimg=cv2.resize(img,(300,400))
   flattened_vector = nimg.flatten()
   imgv.append(flattened_vector)
   nhan.append(1)
for filename in select_cat:
   img_path=os.path.join(catfd,filename)
   img=cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
   nimg=cv2.resize(img,(300,400))
   flattened_vector = nimg.flatten()
   imgv.append(flattened_vector)
   nhan.append(0)   
x_train=np.vstack(imgv)
y_train=np.array(nhan)
import tensorflow as tf
from tf_keras import Sequential
from tf_keras.layers import Dense 

model=Sequential([ 
    Dense(units=300,activation='sigmoid'),
    Dense(units=100,activation='sigmoid'),
    Dense(units=1,activation='sigmoid')  
])
from tf_keras.losses import BinaryCrossentropy
model.compile(loss=BinaryCrossentropy(from_logits=True),optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=20)

test=[]
y=[]
dogtest='C:/Users/thispc/Downloads/archive1/test_set/test_set/dogs'
select_test=random.sample(os.listdir(dogtest),200)
for filename in select_test:
   img_path=os.path.join(dogtest,filename)
   img=cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
   nimg=cv2.resize(img,(300,400))
   flattened_vector = nimg.flatten()
   test.append(flattened_vector)
   y.append(1)
   
   
x_test=np.vstack(test)   
y_test=np.array(y)
ans=model.predict(x_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(ans,y_test))
 