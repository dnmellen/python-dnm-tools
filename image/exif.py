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


GExiv2
``````````````````````````

    sudo apt-get install libexiv2-dev libgexiv2-2 gir1.2-gexiv2-0.4
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
        with open(image_path, 'rb') as f:
            image = Image.open(f)
            image.rotate(degrees)
            image.save()
