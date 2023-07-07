from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()

background_path = "C:/Users/toder/Desktop/6981998_3507563.jpg"
root.title("Steganography project")
root.geometry("700x500+150+180")
root.resizable(False, False)

background_image = ImageTk.PhotoImage(Image.open(background_path))

background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.configure(bg="#2D9EE9")
root.wm_attributes('-transparentcolor', "#2D9EE9")


def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File',
                                          filetypes=(("PNG file", "*.png"),
                                                     ("JPG File", "*.jpg"),
                                                     ("All file", "*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img


def hidetext():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)


def showtext():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)


def saveimage():
    secret.save("hidden.png")


# icon
icon_path = "C:/Users/toder/Desktop/logo.jpeg"
icon = Image.open(icon_path)
icon = ImageTk.PhotoImage(icon)

root.iconphoto(False, icon)

# Frame 1
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=30, y=80)

lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

# Frame 2

frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Arial 15", bg="white", fg="black", relief=GROOVE)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Frame 3

frame3 = Frame(root, bd=3, bg="#6907B5", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", bg="#11A8FE", fg="white", width=10, height=2, font="arial 14",
       command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", bg="#FE5845", fg="white", width=10, height=2, font="arial 14",
       command=saveimage).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#6907B5", fg="white").place(x=20, y=5)

# Frame 4

frame4 = Frame(root, bd=3, bg="#6907B5", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", bg="#11A8FE", fg="white", width=10, height=2, font="arial 14", command=hidetext).place(
    x=20, y=30)
Button(frame4, text="Show Data", bg="#FE5845", fg="white", width=10, height=2, font="arial 14", command=showtext).place(
    x=180, y=30)
Label(frame4, text="Picture, Image, Photo File", bg="#6907B5", fg="white").place(x=20, y=5)

root.mainloop()
