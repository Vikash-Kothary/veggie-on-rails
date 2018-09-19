#!/usr/bin/venv python3
"""
dectection.py - Identify features in an image
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

WINDOW_NAME = "dectection"


def main():
    img = cv.imread('images/rail_track.png', cv.IMREAD_UNCHANGED)
    output = detect_trackts(img)
    cv.imwrite('images/output.jpg', output)

    # plt.subplot(121), plt.imshow(img, cmap='gray')
    # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(output, cmap='gray')
    # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    # plt.show()


def detect_trackts(img):
    """
    See: https://docs.opencv.org/3.4.0/da/d22/tutorial_py_canny.html
    SkiImage: http://scikit-image.org/docs/dev/auto_examples/edges/plot_canny.html
    """

    blur = cv.GaussianBlur(img, (5, 5), 0)
    sobelx = cv.Sobel(blur, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(blur, cv.CV_64F, 0, 1, ksize=5)

    edges = cv.Canny(blur, 300, 200)

    kernel = np.ones((5, 5), np.uint8)
    opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel)

    return closing

if __name__ == '__main__':
    main()
