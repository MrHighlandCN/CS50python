import sys
import PIL

from os.path import splitext
from PIL import Image


def main():
    IsValid()
    helper(sys.argv[1], sys.argv[2])


def IsValid():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif (".jpg" or ".jpeg" or ".png") not in (sys.argv[1] or sys.argv[2]):
        sys.exit("Invalid input")
    elif splitext(f"{sys.argv[1]}")[1] != splitext(f"{sys.argv[2]}")[1]:
        sys.exit("Input and output have different extensions")


def helper(a, b):
    shirt = Image.open("shirt.png")
    size = shirt.size
    try:
        input = Image.open(f"{a}")
        ResizeImage = PIL.ImageOps.fit(input, size)
        ResizeImage.paste(shirt, shirt)
        ResizeImage.save(f"{b}")
    except FileNotFoundError:
        sys.exit(f"Can not open {a} file")


if __name__ == "__main__":
    main()
