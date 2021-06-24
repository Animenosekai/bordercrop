"""
File containing the CLI version of bordercrop
"""

import argparse
import bordercrop

def main():
    parser = argparse.ArgumentParser(prog='bordercrop', description='A black borders cropping module')
    
    parser.add_argument('--version', '-v', action='version', version=bordercrop.__version__)
    
    # required
    parser.add_argument('image', type=str, help='The image to crop')
    parser.add_argument('--output', '-o', action='store', type=str, required=True, help='The path to save the cropped image')
    # optional
    parser.add_argument('--threshold', '-t', action='store', type=int, required=False, default=5, help='The black threshold (0 is black while 225 is white)')
    parser.add_argument('--minimum-threshold-hitting', '-mth', action='store', type=int, required=False, default=100, help="The number of pixels in a row which needs to hit the threshold to count the row as dark (ex: if 5 is given and there is only 4 black pixels in the row, the row won't be counted as black)")
    parser.add_argument('--minimum-rows', '-mr', action='store', type=int, required=False, default=100, help='The minimum row requirement to count a border (ex: if set to 3, 3 rows need to consecutively be black to count it as a border)')
    
    args = parser.parse_args()

    cropped_image = bordercrop.crop(args.image, THRESHOLD=args.threshold, MINIMUM_THRESHOLD_HITTING=args.minimum_threshold_hitting, MINIMUM_ROWS=args.minimum_rows)
    cropped_image.save(args.output)