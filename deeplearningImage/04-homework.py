import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('models/shape_predictor_5_face_landmarks.dat')

cap = cv2.VideoCapture('04-02.mp4')

sticker_img = cv2.imread('04-pig.png', cv2.IMREAD_UNCHANGED)

while True:
    ret, img = cap.read()

    if ret == False:
        break

    dets = detector(img)

    for det in dets:
        shape = predictor(img, det)

        face_x1 = det.left()
        face_y1 = det.top()
        face_x2 = det.right()
        face_y2 = det.bottom()
        nose_x = shape.parts()[4].x
        nose_y = shape.parts()[4].y

        nose_x1 = nose_x - 50
        nose_x2 = nose_x + 50

        h, w, c = sticker_img.shape
        nose_w = nose_x2 - nose_x1
        nose_h = int(h / w * nose_w)

        nose_y1 = int(nose_y - nose_h / 2)
        nose_y2 = nose_y1 + nose_h

        try:
            overlay_img = sticker_img.copy()
            overlay_img = cv2.resize(overlay_img, dsize=(nose_w, nose_h))

            overlay_alpha = overlay_img[:, :, 3:4] / 255.0
            background_alpha = 1.0 - overlay_alpha

            img[nose_y1:nose_y2, nose_x1:nose_x2] = overlay_alpha * overlay_img[:, :, :3] + background_alpha * img[nose_y1:nose_y2, nose_x1:nose_x2]
        except:
            pass

    cv2.imshow('result', img)
    if cv2.waitKey(1) == ord('q'):
        break



