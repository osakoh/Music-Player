import os
from tkinter import *
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox
import os


# initialise mixer
mixer.init()

root = Tk()  # creates a window
root.title("Music Player")
root.iconbitmap(r'img/red-audio.ico')


txt = Label(root, text='Music is playing')
txt.pack()


# *************************************************** Multimedia functions *********************************************
def play_msc():
    try:
        mixer.music.load(filename)
        mixer.music.play()
        statusBar['text'] = "Playing Music" + ' : ' + os.path.basename(filename)
    except:
        tkinter.messagebox.showerror('File not loaded', 'Load a music file first!')


def stop_msc():
    mixer.music.stop()
    statusBar['text'] = "Stopped Music"


def vol_ctrl(val):
    volume = int(val)/100  # convert the val string to int 
    mixer.music.set_volume(volume)  # set_volume accepts values between 0 and 1

# ********************************************** End of multimedia functions *******************************************


# ************************************************** Multimedia controls ***********************************************
playPhoto = PhotoImage(file='img/play.png')
playBtn = Button(root, image=playPhoto, command=play_msc)
playBtn.pack()

stopPhoto = PhotoImage(file='img/stop.png')
stopBtn = Button(root, image=stopPhoto, command=stop_msc)
stopBtn.pack()

volScale = Scale(root, from_=0, to=125, orient=HORIZONTAL, command=vol_ctrl)
volScale.set(45)  # volume isn't set to 45 yet, it's using a default volume in the mixer class
mixer.music.set_volume(0.45)  # volume now set to 45
volScale.pack()


# *********************************************** End of Multimedia controls *******************************************

# ************************************************* Menu bar ***********************************************************
menuBar = Menu(root)  # creates an empty menu bar
root.config(menu=menuBar)
# ************************************************* End of Menu bar ****************************************************


# ************************************************** Menu functions ****************************************************
def about():
    tkinter.messagebox.showinfo('Info', 'Music player written with Python.')


def browse_music():
    global filename
    filename = filedialog.askopenfilename(filetypes=(("mp3 Music Files", "*.mp3"), ("m4a Music Files", "*.m4a")))
# *********************************************** End of menu functions ************************************************


# ************************************************* Submenu bar ********************************************************
subMenu = Menu(menuBar, tearoff=0)  # creates an empty dropdown menu
menuBar.add_cascade(label='File', menu=subMenu)  # for the menu bar
subMenu.add_command(label='Open', command=browse_music)  # create the drop down menu for File
subMenu.add_command(label='Exit',  command=root.destroy)  # create the drop down menu for File

subMenu = Menu(menuBar, tearoff=0)  # creates an empty dropdown menu
menuBar.add_cascade(label='Help', menu=subMenu)  # for the menu bar
subMenu.add_command(label='Contact')  # create the drop down menu for File
subMenu.add_command(label='About Software', command=about)  # create the drop down menu for File

# ************************************************* End of Submenu bar *************************************************


# *************************************************** Status bar *******************************************************
statusBar = Label(root, text="Mp3 Player", relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)
# ************************************************* End of status bar **************************************************

# **********************************************************************************************************************
# **********************************************************************************************************************

# **********************************************************************************************************************
# **********************************************************************************************************************

# **********************************************************************************************************************
# **********************************************************************************************************************

# **********************************************************************************************************************
# **********************************************************************************************************************

# **********************************************************************************************************************
# **********************************************************************************************************************

# **********************************************************************************************************************
# **********************************************************************************************************************







# ********************************************* Centralise the window **************************************************
window_height = 300
window_width = 500
# specifies width and height of window1
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# specifies the co-ordinates for the screen
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
# root.configure(background='#6b778d') fg="red"
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
root.resizable(False, False)  # This code helps to disable windows from resizing
# ******************************************* End of centralise code ***************************************************

root.mainloop()