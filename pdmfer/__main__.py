import sys
import os
import argparse

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pdmfer.core.processor import PDFProcessor
from pdmfer.cli.interface import main_cli


def main():
    main_cli()


if __name__ == "__main__":
    main()