import bordercrop
from PIL import Image

def test_image_retrieving():
    print("[test] --> Testing Retrieving from the internet")

    # should return a PIL.Image.Image instance
    assert isinstance(bordercrop.get_image("https://i.imgur.com/lhQe6Bq.jpg"), Image.Image)
    
    # should return a WrongType exception
    try:
        bordercrop.get_image("aaa")
    except Exception as e:
        assert isinstance(e, bordercrop.exceptions.WrongType)
        assert isinstance(e, bordercrop.exceptions.BordercropException)

    assert bordercrop.get_image("tests/image1.png").size == (2246, 1398)
    image = Image.open("tests/image1.png")
    assert bordercrop.get_image(image).size == (2246, 1398)