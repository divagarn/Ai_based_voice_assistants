import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3,640)
cam.set(4,480)

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#its an object detection apporach
face_id = input("enter an numerical id here: ")
#use integrated id for every new face

print("taking samples, look at camera.... ")
count = 0 #integrated samples face count

while True:
    ret, img = cam.read() #read the frames using the above created object
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count +=1

        cv2.imwrite("samples/face." + str(face_id) + '.' + str(count) + ".jpg", converted_image[y:y+h,x:x+w])
        #to capture and save images in folder

        cv2.imshow('image', img) # used to display an image in a window
    k = cv2.waitKey(100) & 0xff # wait for pressed key
    if k == 27: #press ESC to stop
        break
    elif count >= 10:
        break
print("Samples taken now closing the program... ")
cam.release()
cv2.destroyAllWindows()