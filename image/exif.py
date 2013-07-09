# coding: utf-8

__author__ = 'dnmellen'

'''
==========================
Image utilities
==========================

--------------------------
Requirements
--------------------------

PIL
``````````````````````````

    pip install Pillow

'''

from PIL import Image
from gi.repository import GExiv2


def remove_rotation(image_path):
    '''
    Fix a picture taken from an Apple device

    :param image: Image path
    '''

    # Get Metadata
    exif = GExiv2.Metadata(image_path)

    # Get current orientation
    orientation = exif.get_orientation()
    degrees = None
    if orientation == GExiv2.Orientation.ROT_90:
        degrees = 90
    elif orientation == GExiv2.Orientation.ROT_180:
        degrees = 180
    elif orientation == GExiv2.Orientation.ROT_270:
        degrees = 270

    if degrees is not None:
        # Remove orientation tag
        exif.set_orientation(GExiv2.Orientation.NORMAL)
        exif.save_file()

        # Rotate image
        image = Image.open(image_path)
        rotated_image = image.rotate(360 - degrees)
        rotated_image.save()
