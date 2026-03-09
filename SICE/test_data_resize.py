import cv2
import glob
import numpy as np
import random
from PIL import Image
from pathlib import Path


inter_method = {
    'cv2': {
        'NEAREST': cv2.INTER_NEAREST,
        'LINEAR': cv2.INTER_LINEAR,
        'CUBIC': cv2.INTER_CUBIC,
        'AREA': cv2.INTER_AREA,
        'LANCZOS4': cv2.INTER_LANCZOS4
    },
    'Image': {
        'NEAREST': Image.NEAREST,
        'LINEAR': Image.BILINEAR,
        'CUBIC': Image.BICUBIC,
        'ANTIALIAS': Image.ANTIALIAS
    }
}

def resize_long(im, long_size=224, method='cv2', interp=cv2.INTER_LINEAR):
    if method == 'cv2':
        value = max(im.shape[0], im.shape[1])
        scale = float(long_size) / float(value)
        resized_width = int(round(im.shape[1] * scale))
        resized_height = int(round(im.shape[0] * scale))

        im = cv2.resize(im, (resized_width, resized_height), interpolation=interp)
        return im
    elif method == 'Image':
        if isinstance(im, np.ndarray):
            im = Image.fromarray(im)
        value = max(im.size[0], im.size[1])
        scale = float(long_size) / float(value)
        resized_width = int(round(im.size[0] * scale))
        resized_height = int(round(im.size[1] * scale))

        im = im.resize((resized_width, resized_height), interp)
        return np.asarray(im)


class ResizeByLong:

    def __init__(self, long_size, method='cv2', interp='LINEAR'):
        self.long_size = long_size
        self.method = method
        if self.method not in ['cv2', 'Image']:
            raise ValueError("`method` should be one of 'cv2' and 'Image'")
        self.interp_dict = inter_method[self.method]
        self.interp = interp
        if not (self.interp == "RANDOM" or self.interp in self.interp_dict):
            raise ValueError("`interp` should be one of {}".format(self.interp_dict.keys()))

    def __call__(self, im, label=None):
        """
        Args:
            im (np.ndarray): The Image data.
            label (np.ndarray, optional): The label data. Default: None.

        Returns:
            (tuple). When label is None, it returns (im, ), otherwise it returns (im, label).
        """
        if self.interp == "RANDOM":
            interp = random.choice(list(self.interp_dict.keys()))
        else:
            interp = self.interp

        im = resize_long(
            im, self.long_size, method=self.method, interp=self.interp_dict[interp])

        if label is None:
            return (im,)
        else:
            label = resize_long(
                label, self.long_size, method=self.method, interp=self.interp_dict[interp])
            return im, label

# for file in Path('../all_test_small/label/').glob('*'):
#     label = str(file)
#     # lowlight_image = cv2.cvtColor(cv2.imread(lowlight), cv2.COLOR_BGR2RGB)
#
#     #
#     # lowlight_imager, label_imager = ResizeByLong(long_size=768, method='Image', interp='ANTIALIAS')\
#     #     (im=lowlight_image, label=label_image)
#     #
#     # lowlight_imager = cv2.cvtColor(lowlight_imager, cv2.COLOR_RGB2BGR)
#     # label_imager = cv2.cvtColor(label_imager, cv2.COLOR_RGB2BGR)
#     # cv2.imwrite(lowlight.replace('all_test_small', 'all_test_s'), lowlight_imager)
#     if label.split('.')[-1] == 'png':
#         print(label)
#         label_image = cv2.imread(label)
#         cv2.imwrite(label.replace('all_test_small', 'all_test_s').replace('png', 'jpg'), label_image)
#     # exit()
# for file in Path('../final_test/DICM/').glob('*'):
#     lowlight = str(file)
#     label = str(file).replace('lowlight', 'label')
#     print(lowlight)
#     print(label)
#     lowlight_image = cv2.cvtColor(cv2.imread(lowlight), cv2.COLOR_BGR2RGB)
#     label_image = cv2.cvtColor(cv2.imread(label), cv2.COLOR_BGR2RGB)
#     lowlight_imager, label_imager = ResizeByLong(long_size=768, method='Image', interp='ANTIALIAS')\
#         (im=lowlight_image, label=label_image)
#
#     lowlight_imager = cv2.cvtColor(lowlight_imager, cv2.COLOR_RGB2BGR)
#     label_imager = cv2.cvtColor(label_imager, cv2.COLOR_RGB2BGR)
#     cv2.imwrite(lowlight.replace('all_test_small', 'all_test_s'), lowlight_imager)
#     cv2.imwrite(label.replace('all_test_small', 'all_test_s'), label_imager)
#     # exit()
for file in Path('../final_test/other/').glob('*'):
    lowlight = str(file)
    lowlight_image = cv2.cvtColor(cv2.imread(lowlight), cv2.COLOR_BGR2RGB)
    if max(lowlight_image.shape) > 768:
        print(lowlight)
        lowlight_imager,  = ResizeByLong(long_size=768, method='Image', interp='ANTIALIAS')\
            (im=lowlight_image, )

        lowlight_imager = cv2.cvtColor(lowlight_imager, cv2.COLOR_RGB2BGR)
        cv2.imwrite(lowlight, lowlight_imager)
