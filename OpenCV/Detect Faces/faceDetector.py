import cv2


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("vasnme.jpg")

resized_image = cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))
gray_img = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray_img,
                                     scaleFactor=1.05, minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(resized_image, (x,y), (x+w, y+h), (0,255,0), 3)

print(type(faces))
print(faces)

cv2.imshow("Gray", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
