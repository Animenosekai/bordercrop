"""
bordercrop v1.0.0 (Stable)

© Anime no Sekai — 2021
"""

from bordercrop.exceptions import WrongType
from bordercrop.utils.validate import is_url, is_file
from bordercrop.utils.annotations import Tuple
from PIL import Image
from urllib.request import urlopen
from io import BytesIO

def get_image(image) -> Image.Image:
    """
    Gives back the given image as a PIL.Image.Image instance

    Args:
        image: the given image, it can be a filepath (str, bytes or Path), an URL (which will be downloaded), a BytesIO or a PIL.Image.Image instance
        
    Returns:
        A PIL.Image.Image instance containing the given image
    """
    if isinstance(image, Image.Image):
        return image.copy() # already a PIL Image instance
    elif is_file(image):
        return Image.open(image) # open the image
    elif is_url(image):
        return Image.open(BytesIO(urlopen(image).read())) # download the image
    elif isinstance(image, BytesIO):
        return Image.open(image)
    raise WrongType("{input_type} is not supported by bordercrop".format(input_type=type(image).__name__))

def borders(image, THRESHOLD: int = 5, MINIMUM_THRESHOLD_HITTING: int = 100, MINIMUM_ROWS: int = 100) -> Tuple:
    """
    Gives back the bounding box of the image without the black borders

    Args:
        image: the given image, it can be a filepath (str, bytes or Path), an URL (which will be downloaded), a BytesIO or a PIL.Image.Image instance
        THRESHOLD: the black threshold (0 is black while 225 is white)
        MINIMUM_THRESHOLD_HITTING: the number of pixels in a row which needs to hit the threshold to count the row as dark (ex: if 5 is given and there is only 4 black pixels in the row, the row won't be counted as black)
        MINIMUM_ROWS: the minimum row requirement to count a border (ex: if set to 3, 3 rows need to consecutively be black to count it as a border)

    Returns:
        A tuple containing the coordinates (LEFT, TOP, RIGHT, BOTTOM)
    """
    original_image = get_image(image)
    image = original_image.convert("L") # convert to grayscale
    width, height = image.size # get the size of the image
    data = list(image.getdata()) # get a list containing the different pixels
    # initializing variables
    horizontal = {}
    vertical = {}
    x, y = (0, 0)
    # getting the horizontal and the vertical rows
    for pixel in data:
        x += 1
        try:
            vertical[x].append(pixel)
        except Exception: # avoiding checking if vertical[x] is a list
            vertical[x] = [pixel]
        
        try:
            horizontal[y].append(pixel)
        except Exception:
            horizontal[y] = [pixel]

        if x == width: # if we are getting to the end of the horizontal row
            x = 0
            y += 1
    
    def find_border(data: dict, default: int = 0, _first_border_default: int = 0):
        has_been_dark = False # counting the number of border found
        row_count = 0 # the current number of dark row
        first_border = _first_border_default # the first black border found

        for coord, pixels in data.items(): # looping through the rows
            if [pixel <= THRESHOLD for pixel in pixels].count(True) >= MINIMUM_THRESHOLD_HITTING: # checking if the number of dark pixels is higher or equal to the defined threshold
                row_count += 1
                if row_count >= MINIMUM_ROWS: # we have a border thick enough
                    if has_been_dark: # this is the second border we found
                        return first_border, coord - MINIMUM_ROWS
            else:
                if row_count >= MINIMUM_ROWS: # if we exited the first border
                    has_been_dark = True
                    first_border = coord
                row_count = 0
        
        return first_border, default

    # the "_" prefixed one is the first border found in the opposite analysis

    _top_y, bottom_y = find_border(horizontal, height, 0) # getting the 
    _bottom_y, top_y = find_border({key: horizontal[key] for key in reversed(list(horizontal.keys()))}, 0, height) # reversing the rows order to go from the bottom to the top

    left_x, _right_x = find_border(vertical, width, 0)
    right_x, _left_x = find_border({key: vertical[key] for key in reversed(list(vertical.keys()))}, 0, width)

    BOTTOM = min([bottom_y, _bottom_y]) # getting the higher one
    TOP = max([top_y, _top_y]) # getting the lower one
    LEFT = max([left_x, _left_x])
    RIGHT = min([right_x, _right_x])


    """ debug
    print("Bottom Y:", BOTTOM, bottom_y, _bottom_y)
    print("Top Y:", TOP, top_y, _top_y)
    print("Left X:", LEFT, left_x, _left_x)
    print("Right X:", RIGHT, right_x, _right_x)
    print("Size", original_image.size)
    cropped = original_image.crop((LEFT, TOP, RIGHT, BOTTOM))
    print("Cropped Size", cropped.size)
    cropped.show()
    """

    return LEFT, TOP, RIGHT, BOTTOM

def crop(image, THRESHOLD: int = 5, MINIMUM_THRESHOLD_HITTING: int = 100, MINIMUM_ROWS: int = 100) -> Image.Image:
    """
    Autocrops the black borders from the given image

    Args:
        image: the given image, it can be a filepath (str, bytes or Path), an URL (which will be downloaded), a BytesIO or a PIL.Image.Image instance
        THRESHOLD: the black threshold (0 is black while 225 is white)
        MINIMUM_THRESHOLD_HITTING: the number of pixels in a row which needs to hit the threshold to count the row as dark (ex: if 5 is given and there is only 4 black pixels in the row, the row won't be counted as black)
        MINIMUM_ROWS: the minimum row requirement to count a border (ex: if set to 3, 3 rows need to consecutively be black to count it as a border)

    Returns:
        A PIL.Image.Image instance containing the cropped image
    """
    original_image = get_image(image)
    LEFT, TOP, RIGHT, BOTTOM = borders(original_image, THRESHOLD, MINIMUM_THRESHOLD_HITTING, MINIMUM_ROWS)
    return original_image.crop((LEFT, TOP, RIGHT, BOTTOM)) # crop it