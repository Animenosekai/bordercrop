"""
File containing the different exceptions which can be raised in bordercrop
"""

class BordercropException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class WrongType(BordercropException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)