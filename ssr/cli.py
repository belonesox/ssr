"""Console script for ssr."""
import argparse
import sys
from .ssr import SSR


def main():
    """Console script for ssr."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    # print("Arguments: " + str(args._))
    # print("Replace this message by putting your code into "
    #       "ssr.cli.main")
    ssr = SSR(args)
    ssr.process()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
