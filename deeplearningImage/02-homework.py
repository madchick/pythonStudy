import cv2
import numpy as np

net1 = cv2.dnn.readNetFromTorch('instance_norm/mosaic.t7')
net2 = cv2.dnn.readNetFromTorch('instance_norm/the_scream.t7')
net3 = cv2.dnn.readNetFromTorch('eccv16/starry_night.t7')
net4 = cv2.dnn.readNetFromTorch('eccv16/composition_vii.t7')

img = cv2.imread('0204.jpg')



# preprocessing
h, w, c = img.shape
img = cv2.resize(img, dsize=(500, int(h / w * 500)))
cropped_img = img[57:143, 188:318]

MEAN_VALUE = [103.939, 116.779, 123.680]
blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)
cropped_blob = cv2.dnn.blobFromImage(cropped_img, mean=MEAN_VALUE)



# 추론하기 (Inference)
net1.setInput(cropped_blob)
cropped_output = net1.forward()
net2.setInput(blob)
output1 = net2.forward()
net3.setInput(blob)
output2 = net3.forward()
net4.setInput(blob)
output3 = net4.forward()



# postprocessing
cropped_output = cropped_output.squeeze().transpose((1, 2, 0))
cropped_output += MEAN_VALUE
cropped_output = np.clip(cropped_output, 0, 255)
cropped_output = cropped_output.astype('uint8')

output1 = output1.squeeze().transpose((1, 2, 0))
output1 += MEAN_VALUE
output1 = np.clip(output1, 0, 255)
output1 = output1.astype('uint8')

output2 = output2.squeeze().transpose((1, 2, 0))
output2 += MEAN_VALUE
output2 = np.clip(output2, 0, 255)
output2 = output2.astype('uint8')

output3 = output3.squeeze().transpose((1, 2, 0))
output3 += MEAN_VALUE
output3 = np.clip(output3, 0, 255)
output3 = output3.astype('uint8')

output1_half = output1[0:100, :]
output2_half = output2[100:200, :]
output3_half = output3[200:281, :]
new_output = np.concatenate([output1_half,output2_half,output3_half], axis=0)



img[57:143, 188:318] = cropped_output[0:86,0:130]
new_output[57:143, 188:318] = cropped_output[0:86,0:130]
cv2.imshow('img', img)
cv2.imshow('new_output', new_output)
cv2.waitKey(0)

# 1번
# - 액자 부분만 crop 해서 추론하기 (480,145), (812,367)
# - 바뀐 이미지를 다시 액자 안에 집어넣기

# 2번
# - 가운데가 아닌 곳에서 나눠보기
# - 2개가 아니라 3개, 4개로 나눠보기



import cv2
cap = cv2.VideoCapture('0102.mp4')

while True:
    ret, img = cap.read()

    if ret == False:
        break
    
    h, w, c = img.shape
    img = cv2.resize(img, dsize=(500, int(h / w * 500)))
    
    MEAN_VALUE = [103.939, 116.779, 123.680]
    blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)

    net2.setInput(blob)
    output = net2.forward()

    output = output.squeeze().transpose((1, 2, 0))
    output += MEAN_VALUE
    output = np.clip(output, 0, 255)
    output = output.astype('uint8')
    
    cv2.imshow('video', output)
    if cv2.waitKey(1) == ord('q'):
        break

# 3번
# - 동영상에 적용해보기



