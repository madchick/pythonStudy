import cv2
import numpy as np

net = cv2.dnn.readNetFromTorch('instance_norm/mosaic.t7')
img = cv2.imread('0202.jpg')


# preprocessing
h, w, c = img.shape
print(img.shape)

img = cv2.resize(img, dsize=(500, int(h / w * 500)))
print(img.shape)

# img = img[162:523, 185:428]

cv2.imshow('img', img)
# cv2.waitKey(0)

MEAN_VALUE = [103.939, 116.779, 123.680]
blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)
print(blob.shape)



# 추론하기 (Inference)
net.setInput(blob)
output = net.forward()



# postprocessing
output = output.squeeze().transpose((1, 2, 0))
output += MEAN_VALUE

output = np.clip(output, 0, 255)
output = output.astype('uint8')

cv2.imshow('output', output)
cv2.waitKey(0)



