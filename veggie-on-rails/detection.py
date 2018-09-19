#!/usr/bin/venv python3
"""
dectection.py - Identify features in an image
"""

from utils import dir_files

import cv2
import numpy as np
import skimage
from skimage import io
from matplotlib import pyplot as plt

"""
TODO:
- [ ] Check only left - delete anything on the right

"""


# files = dir_files('images')

# for i in files:
#     img = cv2.imread('images/'+i)
#     get_green(img)


def main():
    files = dir_files('input')
    for i in files:
        img = cv2.imread('input/' + str(i))
        if img is None:
            raise ValueError('No image found')

        img = preprocess(img)

        tree_mask = filter_green(img)
        #tree_mask = col_slice(tree_mask)
        #track_mask = detect_tracks(img)
        #track_mask = row_slice(track_mask)
        #sliced = preprocess(sliced)
        #output = cv2.bitwise_not(track_mask, track_mask, mask=tree_mask)
        output = cv2.bitwise_and(img, img, mask=tree_mask)

        cv2.imwrite('results/' + str(i), output)

    # plt.subplot(121), plt.imshow(img, cmap='gray')
    # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(output, cmap='gray')
    # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    # plt.show()


def row_slice(img):
    """
    """
    print(img.shape)
    zeros = np.zeros_like(img)
    zeros[(img.shape[0] // 2):, :] = img[(img.shape[0] // 2):, :]
    print('og' + str(img.shape))
    # new_img = img[(img.shape[0] // 2):, :, :]
    print('ng' + str(zeros.shape))
    # cv2.imwrite('images/slice.jpg', zeros)
    return zeros


def col_slice(img):
    """
    """
    print(img.shape)
    zeros = np.zeros_like(img)
    zeros[:, :((img.shape[1] // 3) * 2)] = img[:, :((img.shape[1] // 3) * 2)]
    print('og' + str(img.shape))
    # new_img = img[(img.shape[0] // 2):, :, :]
    print('ng' + str(zeros.shape))
    # cv2.imwrite('images/slice.jpg', zeros)
    return zeros


def preprocess(img):
    """
    """
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=5)
    return blur


def detect_tracks(img):
    """
    See: https://docs.opencv.org/3.4.0/da/d22/tutorial_py_canny.html
    """

    edges = cv2.Canny(img, 400, 200)

    kernel = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # redImg = np.zeros(closing.shape, closing.dtype)
    # redImg[:, :, :] = (0, 0, 255)
    # redMask = cv2.bitwise_and(redImg, redImg, mask=closing)
    # cv2.addWeighted(redMask, 1, img, 1, 0, img)
    #cv2.imwrite('images/tracks.jpg', closing)
    return closing


def filter_green(img):
    '''
    Filters green out of image
    '''
    # plt.imshow(img)

    GREEN_MIN = np.array([5, 0, 0], np.uint8)
    GREEN_MAX = np.array([100, 255, 255], np.uint8)

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    frame_threshed = cv2.inRange(hsv_img, GREEN_MIN, GREEN_MAX)
    #cv2.imwrite('images/trees' + '.jpg', frame_threshed)

    kernel = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(frame_threshed, cv2.MORPH_CLOSE, kernel)

    # image = io.imread('images/temp' + '.jpg')
    # plt.imshow(image)
    return frame_threshed


if __name__ == '__main__':
    main()
