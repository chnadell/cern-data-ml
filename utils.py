import numpy as np


def mad_norm(image):
    im_median = np.median(image)
    im_diff = image - im_median
    mad = np.median(np.abs(im_diff))
    img_out = im_diff / mad
    return img_out


im_test = mad_norm(np.array([[128, 52], [78, 200]]))
print(im_test)
