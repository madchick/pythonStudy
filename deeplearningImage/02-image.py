import cv2
import numpy as np

net1 = cv2.dnn.readNetFromTorch('instance_norm/mosaic.t7')
net2 = cv2.dnn.readNetFromTorch('instance_norm/the_scream.t7')
img = cv2.imread('02-03.jpg')


# preprocessing
h, w, c = img.shape
print(img.shape)

img = cv2.resize(img, dsize=(500, int(h / w * 500)))
print(img.shape)

# img = img[162:523, 185:428]

cv2.imshow('img', img)

MEAN_VALUE = [103.939, 116.779, 123.680]
blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)
print(blob.shape)



# 추론하기 (Inference)
net1.setInput(blob)
output1 = net1.forward()

net2.setInput(blob)
output2 = net2.forward()



# postprocessing
output1 = output1.squeeze().transpose((1, 2, 0))
output1 += MEAN_VALUE
output1 = np.clip(output1, 0, 255)
output1 = output1.astype('uint8')

output2 = output2.squeeze().transpose((1, 2, 0))
output2 += MEAN_VALUE
output2 = np.clip(output2, 0, 255)
output2 = output2.astype('uint8')

output1_half = output1[:, 0:250]
output2_half = output2[:, 250:500]

new_output = np.concatenate([output1_half,output2_half], axis=1)

cv2.imshow('output1', output1)
cv2.imshow('output2', output2)
cv2.imshow('output1_half', output1_half)
cv2.imshow('output2_half', output2_half)
cv2.imshow('new_output', new_output)
cv2.waitKey(0)



