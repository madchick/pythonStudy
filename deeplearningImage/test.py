import cv2
import numpy as np
from skimage import io              # Only needed for web reading images


def process(img_url):

    # Web read image
    img = cv2.cvtColor(io.imread(img_url), cv2.COLOR_RGB2BGR)
    img_c = img.copy()

    # Inverse binary threshold grayscale version of image
    # Assumption: plain white background
    img_thr = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 248, 255, cv2.THRESH_BINARY_INV)[1]

    # Find external contour
    # Assumption: only one object/contour
    cnts = cv2.findContours(img_thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    # Find rotated rectangle of the minimum area
    rect = cv2.minAreaRect(cnts[0])
    rect_pts = np.int0(cv2.boxPoints(rect))

    # Calculate centroid
    cent = np.int0((rect_pts[0] + rect_pts[2]) / 2)

    # Calculate tangent of rotation angle
    alpha = rect[2]
    if np.abs(alpha) > 45:
        alpha += 90
    tan_alpha = np.tan(np.deg2rad(alpha))

    # Calculate first edge point
    x0 = np.int32(cent[0] - cent[1] / tan_alpha)
    if x0 < 0:
        x0 = 0
        y0 = np.int32(-cent[0] * tan_alpha + cent[1])
    else:
        y0 = 0

    # Calculate second edge point
    x1 = np.int32(cent[0] + (img.shape[0] - cent[1]) / tan_alpha)
    if x1 > img.shape[1]:
        x1 = img.shape[1]
        y1 = np.int32((x1 - cent[0]) * tan_alpha + cent[1])
    else:
        y1 = img.shape[0]

    # Generate mask for cutting
    # Assumption: Image is sufficient large
    mask = np.zeros_like(img_thr)
    mask = cv2.line(mask, (x0, y0), (x1, y1), 255, 1)
    cv2.floodFill(mask, None, (cent[0] - 5, cent[1] - 5), 255)

    # Split image
    mask3 = np.repeat(np.expand_dims(mask, 2), 3, 2)
    img1 = ~mask3 + cv2.bitwise_and(img_c, img_c, mask=mask)
    img2 = mask3 + cv2.bitwise_and(img_c, img_c, mask=255-mask)

    # Debug output
    img = cv2.line(img, (x0, y0), (x1, y1), (0, 0, 255), 2)
    img = cv2.drawContours(img, [rect_pts], -1, (128, 128, 128), 2)
    img = cv2.circle(img, tuple(cent), 5, (255, 0, 0), 4)

    cv2.imshow('img', img)
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.waitKey(0)


img_urls = [
    'https://i.stack.imgur.com/suzjF.png',
    'https://i.stack.imgur.com/Rl2WN.png'
]

for i in img_urls:
    process(i)

cv2.destroyAllWindows()



