from tkinter import *
import tkinter
sukman_root = Tk()
sukman_root.geometry("1200x1900")
sukman_root.minsize(400,600)
sukman_root.maxsize(343,433)
coder_root = Label(text="Sukhman")
coder_root.pack()
photo = PhotoImage(file="icon with.png")
harman_label = Label(image=photo)
harman_label.pack()
sukman_root.mainloop()

