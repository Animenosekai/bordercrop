import bordercrop
from PIL.Image import Image

def test_borders():
    assert bordercrop.borders("tests/image1.png", 5, 2000, 20) == (0, 68, 2246, 1331)
    assert bordercrop.borders("tests/image2.png") == (189, 0, 2060, 1398)
    assert bordercrop.borders("tests/image3.jpg") == (0, 273, 868, 762)