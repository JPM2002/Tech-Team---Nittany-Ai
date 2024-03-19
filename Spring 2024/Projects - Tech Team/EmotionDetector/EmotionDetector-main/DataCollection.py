import cv2
import cv2 as cv
cam = cv.VideoCapture(0)
cam.set(3, 5)
cam.set(4, 5)


images = 0
while images != 150:
    ret, frame = cam.read(0)
    cv.imshow('frame', frame)
    cv.imwrite(f'HappyImages/IMAGE_{images}.png', frame)
    if cv2.waitKey(20) == ord('q'):
        break
    images += 1

print('HappyImages=' + str(images))
cam.release()
cv.destroyAllWindows()


