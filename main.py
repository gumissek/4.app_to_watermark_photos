# Ubuntu
# sudo apt-get install python3-tk
# Fedora
# sudo dnf install python3-tkinter
# MacOS
# brew install python-tk

from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title('Watermarking app')

photo = Image.open('JPEG_example_JPG_RIP_050.png').convert('RGBA')
img_tk = ImageTk.PhotoImage(photo)

watermark = Image.open('watermark.png').convert('RGBA')
watermark_resized = watermark.resize((int(0.2 * photo.width), int(0.2 * photo.height)))
watermark_resized_tk = ImageTk.PhotoImage(watermark_resized)

#to zapisuje tylko do 1x1 pixel kurwicy dostane
# juz nie zapisuje :3 3h w plecy
canvas = Canvas(width=photo.width, height=photo.height)
canvas.config(highlightthickness=0)

canvas.create_image(photo.width / 2, photo.height / 2, image=img_tk)
canvas.create_image(photo.width * 0.9, photo.height * 0.9, image=watermark_resized_tk)
canvas.pack()
#zawsze canvas update
canvas.update()
canvas.postscript(file="canvas_output.ps", colormode='color')
ps_image = Image.open("canvas_output.ps")
ps_image.save('wychodek.png')

