import cv2

img = cv2.imread("abstract.jpg", 1)


print(type(img))
#print(img)

resized_image = cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))
#cv2.imshow("Abstract", resized_image)
cv2.imwrite("Abstract_resized.jpg", resized_image)
#cv2.waitKey(0)
cv2.destroyAllWindows()