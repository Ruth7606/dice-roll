import tkinter
import random
from PIL import Image, ImageTk

# top level widget which represents the main
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice')

# call main loop for TK
root.mainloop()

# Adding label into the frame
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()
# adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Hello from DataFlair!",
                             fg="light green",
                             bg="dark green",
                             font="Helvetica 16 bold italic")
HeadingLabel.pack()
# images
dice = ['die1.png', 'die2.png', 'die3.png',
        'die4.png', 'die5.png', 'die6.png']
# simulating the dice with random numbers between
# 0 to 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
# packing a widget in the parent widget
ImageLabel.pack(expand=True)
