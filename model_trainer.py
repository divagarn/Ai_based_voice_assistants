import cv2
import numpy as np
from PIL import Image #pillow package
import os

path = 'samples' #patj from ssamples present alreaady

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def Images_And_Lables(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        gray_img = Image.open(imagePath).convert('L') #convert it to grayscale
        img_arr = np.array(gray_img, 'uint8') #creating an array

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_arr)

        for (x,y,w,h) in faces:
            faceSamples.append(img_arr[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print("Training faces , it will take a few seconds. wait ...... ")
faces,ids = Images_And_Lables(path)
recognizer.train(faces, np.array(ids))

recognizer.write('trainer/train.yml') # save the models as trainer.yml

print("model trained, Now we can recogonize your face .")