import argparse
from PIL import Image
import random
import os

def crop_and_resize(image_path, coords, output_path, resolution=(512, 512)):
    """
    Crop and resize an image.

    :param image_path: Path of the source image
    :param coords: A tuple that contains the coordinates (left, upper, right, lower) of the area to be cropped
    :param output_path: Path to save the cropped image
    :param resolution: Resolution of the cropped image
    """
    with Image.open(image_path) as img:
        cropped_img = img.crop(coords)
        resized_img = cropped_img.resize(resolution)
        resized_img.save(output_path)

# Set up command line argument parsing
parser = argparse.ArgumentParser(description='Crop and resize an image.')
parser.add_argument('image_path', type=str, help='Path of the source image')
parser.add_argument('--c', type=int, default=1, help='Number of crops to make')
parser.add_argument('--r', type=int, default=512, help='Resolution of the cropped images')
args = parser.parse_args()

# Path of the source image
image_path = args.image_path

with Image.open(image_path) as img:
    width, height = img.size

# Generate random coordinates for cropping
coords_list = []
for _ in range(args.c):
    left = random.randint(0, max(0, width - args.r))
    upper = random.randint(0, max(0, height - args.r))
    right = min(left + args.r, width)
    lower = min(upper + args.r, height)
    coords = (left, upper, right, lower)
    coords_list.append(coords)

# Get image name without extension
base_name = os.path.basename(image_path)
image_name = os.path.splitext(base_name)[0]

# Loop through the list of coordinates and save each cropped image
for i, coords in enumerate(coords_list):
    output_path = f'{image_name}{i+1}.jpg'
    crop_and_resize(image_path, coords, output_path, resolution=(args.r, args.r))

