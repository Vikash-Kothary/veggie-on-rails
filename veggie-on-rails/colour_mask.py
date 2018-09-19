import skimage
from skimage import io
from matplotlib import pyplot as plt
import cv2
import numpy as np

from os import listdir
from os.path import isfile, join

# TODO:
# Check only left - delete anything on the right
#


def get_green(img):
    '''
    Get green out of image
    '''
    # plt.imshow(img)

    GREEN_MIN = np.array([40, 40, 40], np.uint8)
    GREEN_MAX = np.array([70, 255, 255], np.uint8)

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    frame_threshed = cv2.inRange(hsv_img, GREEN_MIN, GREEN_MAX)
    cv2.imwrite('images/temp'+'.jpg', frame_threshed)

    image = io.imread('images/temp'+'.jpg')
    plt.imshow(image)


def dir_files(path):
    '''
    Lists files in a directory, ignoring hidden files
    '''

    return [f for f in listdir(path) if isfile(join(path, f)) and not f.startswith('.')]

# files = dir_files('images')

# for i in files:
#     img = cv2.imread('images/'+i)
#     get_green(img)
