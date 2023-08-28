import sys
from PIL import Image

def resize_image(image_path, width):
    image = Image.open(image_path)
    wpercent = (width / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((width, hsize), Image.LANCZOS)
    image.save(image_path)

if __name__ == "__main__":
    resize_image(sys.argv[1], int(sys.argv[2]))