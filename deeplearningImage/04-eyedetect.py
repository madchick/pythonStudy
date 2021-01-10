import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('models/shape_predictor_5_face_landmarks.dat')

cap = cv2.VideoCapture('04-01.mp4')

sticker_img1 = cv2.imread('04-sticker01.png', cv2.IMREAD_UNCHANGED)
sticker_img2 = cv2.imread('04-glasses.png', cv2.IMREAD_UNCHANGED)

while True:
    ret, img = cap.read()

    if ret == False:
        break

    dets = detector(img)
    print("number of faces detected:", len(dets))

    for det in dets:
        print(det)
        shape = predictor(img, det)

        for i, point in enumerate(shape.parts()):
            # cv2.circle(img, center=(point.x, point.y), radius=2, color=(0, 0, 255), thickness=-1)
            # cv2.putText(img, text=str(i), org=(point.x, point.y), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=(255, 255, 255), thickness=2)

            glasses_x1 = shape.parts()[2].x - 20
            glasses_x2 = shape.parts()[0].x + 20

            h, w, c = sticker_img2.shape

            glasses_w = glasses_x2 - glasses_x1
            glasses_h = int(h / w * glasses_w)

            center_y = (shape.parts()[0].y + shape.parts()[2].y) / 2

            glasses_y1 = int(center_y - glasses_h / 2)
            glasses_y2 = glasses_y1 + glasses_h

        x1 = det.left()
        y1 = det.top()
        x2 = det.right()
        y2 = det.bottom()
        # cv2.rectangle(img, pt1=(x1,y1), pt2=(x2,y2), color=(255,0,0), thickness=2)

        try:
            x1 = det.left() - 40
            y1 = det.top() - 50
            x2 = det.right() + 40
            y2 = det.bottom() + 30

            overlay_img = sticker_img1.copy()
            overlay_img = cv2.resize(overlay_img, dsize=(x2 - x1, y2 - y1))

            overlay_alpha = overlay_img[:, :, 3:4] / 255.0
            background_alpha = 1.0 - overlay_alpha
            img[y1:y2, x1:x2] = overlay_alpha * overlay_img[:, :, :3] + background_alpha * img[y1:y2, x1:x2]

            overlay_img = sticker_img2.copy()
            overlay_img = cv2.resize(overlay_img, dsize=(glasses_w, glasses_h))

            overlay_alpha = overlay_img[:, :, 3:4] / 255.0
            background_alpha = 1.0 - overlay_alpha

            img[glasses_y1:glasses_y2, glasses_x1:glasses_x2] = overlay_alpha * overlay_img[:, :, :3] + background_alpha * img[glasses_y1:glasses_y2, glasses_x1:glasses_x2]
        except:
            pass

    cv2.imshow('result', img)
    if cv2.waitKey(1) == ord('q'):
        break



