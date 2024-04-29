from wand.image import Image
from argparse import ArgumentParser
import random

parser = ArgumentParser("Stamp some Porter Robinson on an image")
parser.add_argument("input", type=str, metavar="input image", help="The image to stamp.")
parser.add_argument("output", type=str, metavar="output image", help="The stamped image.")
parser.add_argument("--number", "-n", type=int, metavar="number of stamps", default=5, help="The number of stamps to put on the image.")
parser.add_argument("--porter", "-p", type=str, metavar="porter image", default="porter.webp", help="The image to stamp. Default: porter.webp")
parser.add_argument("--scale", "-s", type=float, metavar="scale", default=1.0, help="The scale of the stamp. Default: 1.0")
parser.add_argument("--even", "-e", action="store_true", help="Make the distribution of stamps even.")

args = parser.parse_args()
input_image = args.input
output_image = args.output
number = args.number
porter_image = args.porter
scale = args.scale
even = args.even

porter = Image(filename=porter_image)
porter.resize(int(porter.width * scale), int(porter.height * scale))
porter_w, porter_h = porter.size

with Image(filename=input_image) as img:
    w, h = img.size
    if even:
        blocks = int(number ** 0.5)
        for i in range(blocks):
            for j in range(blocks):
                x = random.randint(i * w // blocks, (i + 1) * w // blocks - porter_w)
                y = random.randint(j * h // blocks, (j + 1) * h // blocks - porter_h)
                porter_rotated = porter.clone()
                porter_rotated.rotate(random.randint(-30, 30))
                img.composite(porter_rotated, left=x, top=y)
        for i in range(number - blocks ** 2):
            x = random.randint(0, w - porter_w)
            y = random.randint(0, h - porter_h)
            porter_rotated = porter.clone()
            porter_rotated.rotate(random.randint(-30, 30))
            img.composite(porter_rotated, left=x, top=y)
    else:
        for i in range(number):
            x = random.randint(0, w - porter_w)
            y = random.randint(0, h - porter_h)
            porter_rotated = porter.clone()
            porter_rotated.rotate(random.randint(-30, 30))
            img.composite(porter_rotated, left=x, top=y)
    img.save(filename=output_image)
