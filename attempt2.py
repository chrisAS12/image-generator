from PIL import Image, ImageDraw, ImageFont

img_w = 100
img_h = 100
img_bg_color = '#FF0000' # hex || rgb --> #FF0000 || (255,0,0)

img = Image.new('RGB', (img_w, img_h), color=img_bg_color)

text = "Hello there!"
text_x_pos = 20
text_y_pos = 20
text_color = '#FFFFFF'
font_name = 'Roboto-Bold.ttf'
font_size = 10

font = ImageFont.truetype(font_name, size=font_size)
canvas = ImageDraw.Draw(img)
canvas.text((text_x_pos, text_y_pos), text, font=font, fill=text_color)


img.show()
