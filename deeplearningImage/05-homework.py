# 1. 다른 그레이스케일 이미지로 시도
# 2. 영상에 시도해보기
# 3. 직사각형 마스크를 씌워 직사각형 부분만 컬러로 만들기
# 4. 이미지에 해상도 향상 & 색 복원 둘 다 적용해보기

# https://www.pexels.com/ko-kr/search/grayscale/
# https://www.pexels.com/ko-kr/search/videos/grayscale/



import cv2
import numpy as np

proto = 'models/colorization_deploy_v2.prototxt'
weights = 'models/colorization_release_v2.caffemodel'

net = cv2.dnn.readNetFromCaffe(proto, weights)
pts_in_hull = np.load('models/pts_in_hull.npy')
pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1).astype(np.float32)
net.getLayer(net.getLayerId('class8_ab')).blobs = [pts_in_hull]
net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full((1, 313), 2.606, np.float32)]

img = cv2.imread('05-03.jpg')

h, w, c = img.shape
img_input = img.copy()
img_input = img_input.astype('float32') / 255.
img_lab = cv2.cvtColor(img_input, cv2.COLOR_BGR2Lab)
img_l = img_lab[:, :, 0:1]

blob = cv2.dnn.blobFromImage(img_l, size=(224, 224), mean=[50, 50, 50])
net.setInput(blob)
output = net.forward()

output = output.squeeze().transpose((1, 2, 0))
output_resized = cv2.resize(output, (w, h))
output_lab = np.concatenate([img_l, output_resized], axis=2)

output_bgr = cv2.cvtColor(output_lab, cv2.COLOR_Lab2BGR)
output_bgr = output_bgr * 255
output_bgr = np.clip(output_bgr, 0, 255)
output_bgr = output_bgr.astype('uint8')

cv2.imshow('img', img_input)
cv2.imshow('result', output_bgr)
cv2.waitKey(0)







import cv2
import numpy as np

cap = cv2.VideoCapture('05-01.mp4')

while True:
    ret, img = cap.read()

    if ret == False:
        break

    img = cv2.resize(img, dsize=(640,360))

    h, w, c = img.shape
    img_input = img.copy()
    img_input = img_input.astype('float32') / 255.
    img_lab = cv2.cvtColor(img_input, cv2.COLOR_BGR2Lab)
    img_l = img_lab[:, :, 0:1]

    blob = cv2.dnn.blobFromImage(img_l, size=(224, 224), mean=[50, 50, 50])
    net.setInput(blob)
    output = net.forward()

    output = output.squeeze().transpose((1, 2, 0))
    output_resized = cv2.resize(output, (w, h))
    output_lab = np.concatenate([img_l, output_resized], axis=2)

    output_bgr = cv2.cvtColor(output_lab, cv2.COLOR_Lab2BGR)
    output_bgr = output_bgr * 255
    output_bgr = np.clip(output_bgr, 0, 255)
    output_bgr = output_bgr.astype('uint8')    

    cv2.imshow('result', output_bgr)
    if cv2.waitKey(1) == ord('q'):
        break







import cv2
import numpy as np

proto = 'models/colorization_deploy_v2.prototxt'
weights = 'models/colorization_release_v2.caffemodel'

net = cv2.dnn.readNetFromCaffe(proto, weights)
pts_in_hull = np.load('models/pts_in_hull.npy')
pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1).astype(np.float32)
net.getLayer(net.getLayerId('class8_ab')).blobs = [pts_in_hull]
net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full((1, 313), 2.606, np.float32)]

img = cv2.imread('05-03.jpg')

h, w, c = img.shape
img_input = img.copy()
img_input = img_input.astype('float32') / 255.
img_lab = cv2.cvtColor(img_input, cv2.COLOR_BGR2Lab)
img_l = img_lab[:, :, 0:1]

blob = cv2.dnn.blobFromImage(img_l, size=(224, 224), mean=[50, 50, 50])
net.setInput(blob)
output = net.forward()

output = output.squeeze().transpose((1, 2, 0))
output_resized = cv2.resize(output, (w, h))
output_lab = np.concatenate([img_l, output_resized], axis=2)

output_bgr = cv2.cvtColor(output_lab, cv2.COLOR_Lab2BGR)
output_bgr = output_bgr * 255
output_bgr = np.clip(output_bgr, 0, 255)
output_bgr = output_bgr.astype('uint8')

mask = np.zeros_like(img, dtype='uint8')
mask = cv2.rectangle(mask, pt1=(221, 96), pt2=(400, 361), color=(1, 1, 1), thickness=-1)
color = output_bgr * mask
gray = img * (1 - mask)
output2 = color + gray

cv2.imshow('img', img_input)
cv2.imshow('result', output_bgr)
cv2.imshow('result2', output2)
cv2.waitKey(0)







import cv2
import numpy as np

proto = 'models/colorization_deploy_v2.prototxt'
weights = 'models/colorization_release_v2.caffemodel'

net = cv2.dnn.readNetFromCaffe(proto, weights)
pts_in_hull = np.load('models/pts_in_hull.npy')
pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1).astype(np.float32)
net.getLayer(net.getLayerId('class8_ab')).blobs = [pts_in_hull]
net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full((1, 313), 2.606, np.float32)]

img = cv2.imread('05-04.jpg')

h, w, c = img.shape
img_input = img.copy()
img_input = img_input.astype('float32') / 255.
img_lab = cv2.cvtColor(img_input, cv2.COLOR_BGR2Lab)
img_l = img_lab[:, :, 0:1]

blob = cv2.dnn.blobFromImage(img_l, size=(224, 224), mean=[50, 50, 50])
net.setInput(blob)
output = net.forward()

output = output.squeeze().transpose((1, 2, 0))
output_resized = cv2.resize(output, (w, h))
output_lab = np.concatenate([img_l, output_resized], axis=2)

output_bgr = cv2.cvtColor(output_lab, cv2.COLOR_Lab2BGR)
output_bgr = output_bgr * 255
output_bgr = np.clip(output_bgr, 0, 255)
output_bgr = output_bgr.astype('uint8')

sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel('models/EDSR_x3.pb')
sr.setModel('edsr', 3)
result = sr.upsample(output_bgr)

resized_img = cv2.resize(output_bgr, dsize=None, fx=3, fy=3)

cv2.imshow('img', img_input)
cv2.imshow('color', output_bgr)
cv2.imshow('highres', result)
cv2.imshow('resized', resized_img)
cv2.waitKey(0)



