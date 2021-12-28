# pip install Pillow
import os
from PIL import Image


def compress(file):
    filepath = os.path.join(os.getcwd(), file)
    picture = Image.open(filepath)
    picture.save('Compressed_' + file, 'JPEG', optimize=True, quality=60)
    return


def main():
    cwd = os.getcwd()
    formats = ('.png', '.jpg', '.jpeg')
    for file in os.listdir(cwd):
        if os.path.splitext(file)[1].lower() in formats:
            compress(file)


if __name__ == '__main__':
    main()
