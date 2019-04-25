'''
Utility functions to save overlay information on images.
'''

import os
import numpy as np

from skimage import io, img_as_ubyte
from skimage.color import label2rgb

def save_overlay_image(path, image, reg_props, reg_labels):
    '''
    Generates and saves an image overlaying a green / red shade corresponding to the label passed

    Parameters
    ----------
    path: string
        Path to the save directory
    image: np.array
        Original image to use as background for the overlay
    regProps(N): list(regionProperties)
        List of regionProperties corresponding to the regions to label
    regLabels(N): list(int)
        List of binary labels (0 or 1) corresponding to the regionProperties
    '''

    labeled_binary = np.zeros_like(image)

    for (i, region) in enumerate(reg_props):
        np.put(labeled_binary, np.ravel_multi_index(region.coords.T, labeled_binary.shape), reg_labels[i] + 1)

    overlay_label = label2rgb(labeled_binary, image, colors=['red', 'green'], alpha=0.2, bg_label=0)

    if not os.path.exists(os.path.dirname(path)):
        os.mkdir(os.path.dirname(path))

    io.imsave(path, img_as_ubyte(overlay_label))
    