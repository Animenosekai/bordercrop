# `bordercrop`

> A black borders cropping module

***Crop the black borders from any image in a single line of code!***

[![PyPI version](https://badge.fury.io/py/bordercrop.svg)](https://pypi.org/project/bordercrop/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/bordercrop)](https://pypistats.org/packages/bordercrop)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bordercrop)](https://pypi.org/project/bordercrop/)
[![PyPI - Status](https://img.shields.io/pypi/status/bordercrop)](https://pypi.org/project/bordercrop/)
[![GitHub - License](https://img.shields.io/github/license/Animenosekai/bordercrop)](https://github.com/Animenosekai/bordercrop/blob/master/LICENSE)
[![GitHub top language](https://img.shields.io/github/languages/top/Animenosekai/bordercrop)](https://github.com/Animenosekai/bordercrop)
[![CodeQL Checks Badge](https://github.com/Animenosekai/bordercrop/workflows/CodeQL%20Python%20Analysis/badge.svg)](https://github.com/Animenosekai/bordercrop/actions?query=workflow%3ACodeQL)
[![Pytest](https://github.com/Animenosekai/bordercrop/actions/workflows/pytest.yml/badge.svg)](https://github.com/Animenosekai/bordercrop/actions/workflows/pytest.yml)
![Code Size](https://img.shields.io/github/languages/code-size/Animenosekai/bordercrop)
![Repo Size](https://img.shields.io/github/repo-size/Animenosekai/bordercrop)
![Issues](https://img.shields.io/github/issues/Animenosekai/bordercrop)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need Python 3 to use this module

```bash
# vermin output
Minimum required versions: 3.2
Incompatible versions:     2
```

According to Vermin (`--backport typing`), Python 3.2 is needed for the backport of typing but some may say that it is available for python versions higher than 3.0

Always check if your Python version works with `bordercrop` before using it in production

## Installing

### Option 1: From PyPI

```bash
pip install bordercrop
```

### Option 2: From Git

```bash
pip install https://github.com/Animenosekai/bordercrop
```

You can check if you successfully installed it by printing out its version:

```bash
$ python -c "import bordercrop; print(bordercrop.__version__)"
# output:
bordercrop v1.0.0
```

<!--If a CLI version is available-->

or just:

```bash
$ bordercrop --version
# output:
bordercrop v1.0.0
```

## Usage

You can use bordercrop in Python by importing it in your script:

```python
import bordercrop

cropped_image = bordercrop.crop("https://i.imgur.com/lhQe6Bq.jpg")
cropped_image.show() # show the cropped image
```

Leaving everything with the default values, you may get images with no crop or with no size (entirely cropped).

I recommend testing and tweaking the MINIMUM_THRESHOLD_HITTING and MINIMUM_ROWS values according to your picture (a big picture needs more minimum rows and more pixels to hit before counting a row as dark).

### CLI usage

You can use bordercrop in other apps by accessing it through the CLI version:

```bash
$ bordercrop --image "https://i.ytimg.com/vi/e_53PHZwQH4/hqdefault.jpg" --output "cropped.jpg"
output
```

### As a Python module

The given image can be a filepath (str, bytes or Path), an URL (which will be downloaded) or a PIL.Image.Image instance

#### crop()

Autocrops the black borders from the given image

Args:  
    `image`: the given image, it can be a filepath (str, bytes or Path), an URL (which will be downloaded), a BytesIO or a PIL.Image.Image instance  
    `THRESHOLD`: the black threshold (0 is black while 225 is white)  
    `MINIMUM_THRESHOLD_HITTING`: the number of pixels in a row which needs to hit the threshold to count the row as dark (ex: if 5 is given and there is only 4 black pixels in the row, the row won't be counted as black)  
    `MINIMUM_ROWS`: the minimum row requirement to count a border (ex: if set to 3, 3 rows need to consecutively be black to count it as a border)

Returns:  
    A `PIL.Image.Image` instance containing the cropped image

#### borders()

Gives back the bounding box of the image without the black borders

Args:  
    `image`: the given image, it can be a filepath (str, bytes or Path), an URL (which will be downloaded), a BytesIO or a PIL.Image.Image instance  
    `THRESHOLD`: the black threshold (0 is black while 225 is white)  
    `MINIMUM_THRESHOLD_HITTING`: the number of pixels in a row which needs to hit the threshold to count the row as dark (ex: if 5 is given and there is only 4 black pixels in the row, the row won't be counted as black)  
    `MINIMUM_ROWS`: the minimum row requirement to count a border (ex: if set to 3, 3 rows need to consecutively be black to count it as a border)  

Returns:  
    A tuple containing the coordinates (LEFT, TOP, RIGHT, BOTTOM)

#### get_image()

Gives back the given image as a PIL.Image.Image instance

Mostly used internally, it can be useful sometimes.

Args:  
    `image`: the given image, it can be a filepath (str, bytes or Path), an URL (which will be downloaded), a BytesIO or a PIL.Image.Image instance

Returns:  
    A PIL.Image.Image instance containing the given image

### Exceptions

All of the excpetions inherit from the `BordercropException`

A `WrongType` exception can be raised if the wrong type of image is given

## Deployment

This module is currently in development and might contain bugs.

Feel free to use it in production if you feel like it is suitable for your production even if you may encounter issues.

## Built With

- [Pillow](https://github.com/python-pillow/Pillow) - To manipulate images

## Authors

- **Anime no Sekai** - *Initial work* - [Animenosekai](https://github.com/Animenosekai)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details
