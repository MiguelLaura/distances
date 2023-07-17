"""CLI Endpoint"""

from argparse import ArgumentParser, FileType
import csv
import sys

import numpy as np

from distances.__version__ import __version__
from distances.distance_computor.hausdorff import hausdorff
from distances.distance_computor.minimal import minimal


def main():
    """Main function"""

    parser = ArgumentParser(
        description="First CLI : CLI distance", prog="distance_computor"
    )

    parser.add_argument(
        "--version", action="version", version=f'{"distance_computor {__version__}"}'
    )
    parser.add_argument(
        "file_a",
        type=FileType("r"),
        help="First file with coordinates",
    )
    parser.add_argument(
        "file_b",
        type=FileType("r"),
        help="Second file with coordinates",
    )
    parser.add_argument(
        "--distance",
        default="minimal",
        choices=["hausdorff", "minimal"],
        help="Compute the minimum distance between 2 sets with Hausdorff",
        metavar="distance_type",
    )

    cli_args = parser.parse_args()

    coords_a = []
    coords_b = []

    reader_a = csv.reader(cli_args.file_a, delimiter=" ")
    for row in reader_a:
        if row:
            coords_a.append(row)

    reader_b = csv.reader(cli_args.file_b, delimiter=" ")
    for row in reader_b:
        if row:
            coords_b.append(row)

    coords_a = np.array(coords_a, dtype=float)
    coords_b = np.array(coords_b, dtype=float)

    if cli_args.distance == "minimal":
        print(minimal(coords_a, coords_b))
    elif cli_args.distance == "hausdorff":
        print(hausdorff(coords_a, coords_b))
    else:
        parser.print_help(file=sys.stderr)


if __name__ == "__main__":
    main()
