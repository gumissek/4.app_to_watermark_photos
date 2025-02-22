# Ubuntu
# sudo apt-get install python3-tk
# Fedora
# sudo dnf install python3-tkinter
# MacOS
# brew install python-tk

from tkinter import  *
from PIL import Image, ImageTk


window = Tk()
window.title('Watermarking app')
window.config(padx=50,pady=50)

image = Image.open('photo.png')
img_tk=ImageTk.PhotoImage(image)

watermark=Image.open('watermark.png')
watermark_resized = watermark.resize((int(0.2*image.width),int(0.2*image.height)))
watermark_resized_tk=ImageTk.PhotoImage(watermark_resized)



print(image.width)
print(image.height)
canvas= Canvas(width=image.width,height=image.height)
canvas.config(highlightthickness=0)

canvas.create_image(image.width/2,image.height/2,image=img_tk)
canvas.create_image(image.width*0.9,image.height*0.9,image=watermark_resized_tk)
canvas.pack()
canvas.postscript(file='')



window.mainloop()