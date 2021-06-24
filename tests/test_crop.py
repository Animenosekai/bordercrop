import bordercrop
from PIL.Image import Image

def test_crop():
    assert isinstance(bordercrop.crop("tests/image1.png"), Image)
    assert bordercrop.crop("tests/image1.png", 5, 2000, 20).size == (2246, 1263)
    assert bordercrop.crop("tests/image2.png").size == (1871, 1398)
    assert bordercrop.crop("tests/image3.jpg").size == (868, 489)
