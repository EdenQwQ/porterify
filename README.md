# Porterify

![](./demo.png)

## Usage

Install `python`, `pip` and `ImageMagick`. Then install the dependencies by running `pip install -r requirements.txt`.

Check the usage by running `python porterify.py --help`.

```bash
usage: Stamp some Porter Robinson on an image [-h] [--number number of stamps] [--porter porter image] [--scale scale]
                                              [--even]
                                              input image output image

positional arguments:
  input image           The image to stamp.
  output image          The stamped image.

options:
  -h, --help            show this help message and exit
  --number number of stamps, -n number of stamps
                        The number of stamps to put on the image.
  --porter porter image, -p porter image
                        The image to stamp. Default: porter.webp
  --scale scale, -s scale
                        The scale of the stamp. Default: 1.0
  --even, -e            Make the distribution of stamps even.
```
