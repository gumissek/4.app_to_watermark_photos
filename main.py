# Ubuntu
# sudo apt-get install python3-tk
# Fedora
# sudo dnf install python3-tkinter
# MacOS
# brew install python-tk

from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path
import os
folder_path = Path('photos_to_watermark')
files = [file.name for file in folder_path.iterdir() if file.is_file() ]

for file in files:
    # print(file.split('.')[0])

    window = Tk()
    window.title('Watermarking app')

    photo = Image.open(f'photos_to_watermark/{file}').convert('RGBA')
    img_tk = ImageTk.PhotoImage(photo)
    window.config(width=photo.width,height=photo.height)

    watermark = Image.open('watermark/watermark.png').convert('RGBA')
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
    file_without_extension=file.split('.')[0]
    extension=file.split('.')[1].upper()
    ps_image.save(f'outputs/{file_without_extension}',format=extension)

os.remove('canvas_output.ps')

