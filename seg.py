# #!/usr/bin/env python3
""" Main entry point to superpixel_annotation.py """

import argparse
import os

from superpixel_annotation.superpixel_annotation import launch


def _parse_args():
    """ Add the cli argparser arguments

    Returns
    -------
    :class:`argparse.Namespace`
        The parsed command line arguments
    """
    parser = argparse.ArgumentParser(prog="Superpixel Annotation Tool",
                                     description="A simple QT tool for semantic segmentation")
    parser.add_argument("-i", "--images",
                        type=str,
                        help="Optionally pass a folder name containing the images you wish to "
                             "annotate.")
    parser.add_argument("-l", "--labels",
                        type=str,
                        help="Optionally pass a folder name for saving the labels to. Can contain "
                             "existing images. This folder will be created if it does not "
                             "pre-exist.")
    return parser.parse_args()


def main():
    """ Parses cli arguments and launch segmentation tool """
    args = _parse_args()
    if args.labels is not None and not os.path.exists(args.labels):
        print(f"Creating label folder: '{args.labels}'")
        os.makedirs(args.labels)

    launch(args.images, args.labels)


if __name__ == "__main__":
    main()
