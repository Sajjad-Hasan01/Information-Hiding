from PIL import Image, ImageDraw, ImageFont, ImageEnhance

def add_text_watermark(image, text, position, font='', font_size=30, color=(255,255,255,100)):
    image = Image.open(image).convert('RGBA')
    txt = Image.new('RGBA', image.size, color=(255,255,255,0))
    font = ImageFont.truetype(font, font_size)
    d = ImageDraw.Draw(txt)
    d.text(position, text, fill=color, font=font)

    watermarked = Image.alpha_composite(image, txt)
    watermarked = watermarked.convert('RGB')
    watermarked.show()
    watermarked.save("new-image.jpg")


def add_image_watermark(image, logo, position, opacity=255):
    background = Image.open(image).convert('RGBA')
    watermark = Image.open(logo).convert('RGBA')
    watermark = watermark.resize((50,50))

    if opacity < 255:
        alpha = watermark.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity / 255.0)
        watermark.putalpha(alpha)

    transparent = Image.new('RGBA', background.size, color=(0, 0, 0, 0))
    transparent.paste(watermark, position, watermark)
    result = Image.alpha_composite(background, transparent)

    result = result.convert('RGB')
    result.show()
    result.save("watermark.jpg")


add_image_watermark('image.jpg','logo.jpg',(200,200))

# HOMEWORK :
# Change size of watermark
# How alpha does work ?
