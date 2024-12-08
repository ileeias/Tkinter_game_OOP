from tkinter import *
import time

WIDTH = 200
HEIGHT = 500
xVelocity = 1
yVelocity = 1
tk = Tk()

canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

png = PhotoImage(file='Hero.png')
img = canvas.create_image(0,0,image=png, anchor=NW)

img_width = png.width()
img_height = png.height()

while True:
    coordinates = canvas.coords(img)
    print(coordinates)
    if coordinates[0]>=WIDTH-img_width or coordinates[0]<0:
        xVelocity = -xVelocity
    canvas.move(img, xVelocity,0)
    tk.update()
    time.sleep(0.01)

tk.mainloop()