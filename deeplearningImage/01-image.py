import cv2

img = cv2.imread('0101.jpg')

print(img)
print(img.shape)

cv2.rectangle(img, pt1=(257,87), pt2=(379,337), color=(255,0,0), thickness=2)
cv2.circle(img, center=(320,220), radius=100, color=(0,0,255), thickness=3)
cv2.imshow('img',img)
cv2.waitKey(0)

cropped_img = img[89:348, 259:380] # Y축, X축 순으로 자른다
cv2.imshow('img',cropped_img)
cv2.waitKey(0)

resized_img = cv2.resize(img, (512,256))
cv2.imshow('img',resized_img)
cv2.waitKey(0)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('result', img_rgb)
cv2.waitKey(0)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('result', img_rgb)
cv2.waitKey(0)



overlay_img = cv2.imread('0102.png', cv2.IMREAD_UNCHANGED)
overlay_img = cv2.resize(overlay_img, dsize=(150,150))

overlay_alpha = overlay_img[:, :, 3:] / 255.0
background_alpha = 1.0 - overlay_alpha

x1 = 100
y1 = 100
x2 = x1 + 150
y2 = y1 + 150
img[y1:y2, x1:x2] = overlay_alpha * overlay_img[:, :, :3] + background_alpha * img[y1:y2, x1:x2]

cv2.imshow('result', img)
cv2.waitKey(0)



