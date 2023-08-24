from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import webbrowser
capture = cv2.VideoCapture(0)
result = True
while(result):
    _, frame = capture.read()
    cv2.imwrite("live.jpg",frame)
    result =False
    if (cv2.waitKey(1) &0xFF == ord("q")):
        capture.release()
        v2.destroyAllWindows()



img = cv2.imread('live.jpg')

plt.imshow(img[:,:,::-1])
plt.show()

result = DeepFace.analyze(img,actions='emotion')



result = result[0]['dominant_emotion']
print(result)


    