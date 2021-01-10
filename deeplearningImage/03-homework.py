# 1. 마스크 착용여부 출력 (동영상)
# 2. 마스크 판단 confidencd 숫자 출력

import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

facenet = cv2.dnn.readNet('models/deploy.prototxt', 'models/res10_300x300_ssd_iter_140000.caffemodel')
model = load_model('models/mask_detector.model')

def detectMask(video):
    cap = cv2.VideoCapture(video)

    while True:
        ret, img = cap.read()

        if ret == False:
            break

        h, w, c = img.shape
        # 이미지 전처리하기
        blob = cv2.dnn.blobFromImage(img, size=(300, 300), mean=(104., 177., 123.))

        # 얼굴 영역 탐지 모델로 추론하기
        facenet.setInput(blob)
        dets = facenet.forward()

        # 각 얼굴에 대해서 반복문 돌기
        for i in range(dets.shape[2]):
            confidence = dets[0, 0, i, 2]

            if confidence < 0.5:
                continue

            # 사각형 꼭지점 찾기
            x1 = int(dets[0, 0, i, 3] * w)
            y1 = int(dets[0, 0, i, 4] * h)
            x2 = int(dets[0, 0, i, 5] * w)
            y2 = int(dets[0, 0, i, 6] * h)

            face = img[y1:y2, x1:x2]

            face_input = cv2.resize(face, dsize=(224, 224))
            face_input = cv2.cvtColor(face_input, cv2.COLOR_BGR2RGB)
            face_input = preprocess_input(face_input)
            face_input = np.expand_dims(face_input, axis=0)

            mask, nomask = model.predict(face_input).squeeze()     

            if mask > nomask:
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)

            # 사각형 그리기
            cv2.rectangle(img, pt1=(x1, y1), pt2=(x2, y2), thickness=2, color=color)
            cv2.putText(img, text='%.2f'%mask, org=(x1, y1), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=color)

        cv2.imshow('result', img)
        if cv2.waitKey(1) == ord('q'):
            break



detectMask('0301.mp4')
detectMask('0302.mp4')
detectMask('0303.mp4')
detectMask('0304.mp4')



