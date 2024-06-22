import hashlib
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import numpy as np

def generate_fingerprinting(data):
    if not isinstance(data, bytes):
        data = data.encode('utf-8')
    hash_obj = hashlib.sha256()
    hash_obj.update(data)
    fingerprinting = hash_obj.hexdigest()
    return fingerprinting

def add_text_watermark(image, text, position, save_path, color=(0,0,0,255)):
    image = Image.open(image).convert('RGBA')
    txt = Image.new('RGBA', image.size, color=(255,255,255,0))
    # font = ImageFont.truetype(font_size)
    # font = ImageFont.truetype(font, font_size)
    d = ImageDraw.Draw(txt)
    d.text(position, text, fill=color)
    # d.text(position, text, fill=color, font=font)

    watermarked = Image.alpha_composite(image, txt)
    watermarked = watermarked.convert('RGB')
    watermarked.show()
    watermarked.save(save_path)

def encode_message(img_path, message):
    img = Image.open(img_path)
    encoded_img = img.copy()
    width, height = img.size
    index = 0
    message += "}" # A special character indicating the end of the message
    binary_message = ''.join([format(ord(char), '08b') for char in message])
    data_len = len(binary_message)
    for row in range(height):
        for col in range(width):
            if index < data_len:
                pixel = list(img.getpixel((row, col)))
                # Change the LSB of the first channel to match the message bit
                pixel[0] = pixel[0] & ~1 | int(binary_message[index])
                encoded_img.putpixel((col, row), tuple(pixel))
                index += 1
            else:
                return encoded_img
    # return encoded_img


def decode_message(img_path):
    img = Image.open(img_path)
    binary_message = ""
    width, height = img.size
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((row, col))
            binary_message += str(pixel[0] & 1)
            # Check if we've reached the end marker for the message
            if binary_message.endswith('01111101'):  # Binary for "}"
                return ''.join([chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message) - 8, 8)])


message = "IT"
image_path = "../assets/image/doge.jpg"
save_path = "../assets/image/watermark.jpg"
final_path = "../assets/image/hidden-and-watermark.jpg"
color_channel = 'R'
last_row_index = 0
last_col_index = 100

# hashed_message = generate_fingerprinting(message)
# add_text_watermark(image_path, hashed_message,(140,490), save_path)
# encoded_img = encode_message(save_path, message)
# encoded_img.save(final_path)

recovery_message = decode_message(final_path)
print(recovery_message)
