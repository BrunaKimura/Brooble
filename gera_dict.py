import cv2
import os, sys
import numpy as np
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input
from keras.applications.resnet50 import preprocess_input, decode_predictions
import itertools
import pickle

model = ResNet50(weights='imagenet')

def mnetv2_input_from_image(img):
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    return preprocess_input(x)

def return_id(caminho):
    img = image.load_img(caminho, target_size=(224, 224))
    x = mnetv2_input_from_image(img)
    preds = model.predict(x)
    sort = np.argsort(preds)
    inv_sort = np.flip(sort, 1)
    maiorid = inv_sort[0][:5]
    maior5 = decode_predictions(preds, top=5)[0]
    return maiorid, maior5

dic_id = {}
files = sorted(os.listdir("imagens"))
for i in files:
    img_path = i
    caminho = "imagens/"+img_path
    id5, predict = return_id(caminho)
    for e in range(len(id5)):
        if id5[e] in dic_id:
            dic_id[id5[e]].append([predict[e][2], caminho])
        else:
            dic_id[id5[e]] = [[predict[e][2], caminho]]  

pickle.dump(dic_id, open( "dict.p", "wb" ) )