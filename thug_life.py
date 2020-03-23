import cv2

cap = cv2.VideoCapture(0)

classifier = cv2.CascadeClassifier("haarcascade_eye.xml")
glasses = cv2.imread("try.png", cv2.IMREAD_UNCHANGED)
print(glasses.shape)
while True:

    retval, image = cap.read()
    if retval:

        eyes = classifier.detectMultiScale(image)
        eyes = sorted(eyes, key=lambda eye: eye[2]*eye[3], reverse=True)

        if len(eyes) >= 2:

            x1, y1, w1, h1 = eyes[0]
            x2, y2, w2, h2 = eyes[1]
            if (x1 > x2):
                x1, x2 = x2, x1
                y1, y2 = y2, y1
                w1, w2 = w2, w1
                h1, h2 = h2, h1
            h = min(h1,h2)
            w = x2 + w2 - x1 + 40
            x1 -= 20
            glasses = cv2.resize(glasses, (w,h))
            cv2.imshow("Glasses", glasses)
            cut = image[y1:y1 + h, x1:x1+w]
            for row in range(h):
                for col in range(w):
                    if glasses[row, col, 3] > 100:
                        cut[row, col] = glasses[row, col, :3]

            cv2.imshow("thug_life", image)
    key = cv2.waitKey(10)

    if key == ord("q"):
        break
    if key == ord("c"):
        cv2.imwrite("classroom.png", image)


cap.release()
cv2.destroyAllWindows()