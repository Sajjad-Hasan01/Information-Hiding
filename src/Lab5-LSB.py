from PIL import Image
import numpy as np


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
                pixel = list(img.getpixel((col, row)))
                # Change the LSB of the first channel to match the message bit
                pixel[0] = pixel[0] & ~1 | int(binary_message[index])
                encoded_img.putpixel((col, row), tuple(pixel))
                index += 1
            else:
                return encoded_img
    return encoded_img

def decode_message(img_path):
    img = Image.open(img_path)
    binary_message = ""
    width, height = img.size
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            binary_message += str(pixel[0] & 1)
            # Check if we've reached the end marker for the message
            if binary_message.endswith('01111101'):  # Binary for "}"
                return ''.join([chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message) - 8, 8)])

def string_to_binary(input_string):
    output = ' '.join(format(ord(char), 'b') for char in input_string)
    return output

def extract_lsb_matrix(image_path, color_channel, last_row_index, last_col_index):
    img = Image.open(image_path)

    img_array = np.array(img)

    channel_index = {'R':0, 'G':1, 'B':2}[color_channel]
    channel_data = img_array[:, :, channel_index]

    sub_matrix = channel_data[:last_row_index + 1, :last_col_index + 1]
    lsb_matrix = np.bitwise_and(sub_matrix, 1)

    return lsb_matrix


image_path = '../assets/image/doge.jpg'
color_channel = 'R'
last_row_index = 0
last_col_index = 100

message = 'Hello'

# Example usage1
# print(f'Binary of ({test}) is : ', string_to_binary(test))
# LSBs = extract_lsb_matrix(image_path, color_channel, last_row_index, last_col_index)
# print('Least significant bits of the new image :\n', LSBs)

# Example usage2
# encoded_img = encode_message('../assets/image/doge.jpg', 'hello world')
# encoded_img.save('../assets/image/hiddenmeassage.jpg')
recovery_message = decode_message('../assets/image/hiddenmeassage.jpg')
print(recovery_message)
