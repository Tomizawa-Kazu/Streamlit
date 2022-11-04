import streamlit as st
import webcolors as wc
from PIL import Image, ImageDraw

col1, col2 = st.columns(2)

color_name1 = col1.text_input('色1を入力(英語)')
r1 = col1.slider('R',0,255,255)
g1 = col1.slider('G',0,255,0)
b1 = col1.slider('B',0,255,0)

color_name2 = col1.text_input('色2を入力(英語)')
r2 = col1.slider('R',0,255,0)
g2 = col1.slider('G',0,255,255)
b2 = col1.slider('B',0,255,1)

if st.button('色表示'):
  #im = Image.new('RGB', (500, 500), (240,221,195))
  im = Image.new('RGB', (1000, 500), (255, 255, 255))
  draw = ImageDraw.Draw(im)
  if color_name1 == "":
    draw.rectangle((400, 0, 600, 500), fill=(r1,g1,b1), outline=(255, 255, 255))
  else:
    draw.rectangle((400, 0, 600, 500), fill=(color_name1), outline=(255, 255, 255))

  if color_name2 == "":
    draw.rectangle((600, 0, 800, 500), fill=(r2,g2,b2), outline=(255, 255, 255))
  else:
    draw.rectangle((600, 0, 800, 500), fill=(color_name2), outline=(255, 255, 255))
  
  im.save('pillow_imagedraw.jpg', quality=95)
  col2.image('pillow_imagedraw.jpg')