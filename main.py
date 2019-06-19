from tkinter import *
from pygame import mixer

# initialise mixer
mixer.init()

root = Tk()  # creates a window
root.title("Music Player")
root.iconbitmap(r'img/red-audio.ico')


txt = Label(root, text='Music is playing')
txt.pack()


# *************************************************** Multimedia functions *********************************************
def play_msc():
    mixer.music.load("raise.mp3")
    mixer.music.play()


def stop_msc():
    mixer.music.stop()


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
volScale.set(80)
volScale.pack()


# *********************************************** End of Multimedia controls *******************************************

# ************************************************* Menu bar ***********************************************************
menuBar = Menu(root)  # creates an empty menu bar
root.config(menu=menuBar)
# ************************************************* End of Menu bar ****************************************************

# ************************************************* Submenu bar ********************************************************
subMenu = Menu(menuBar)
menuBar.add_cascade(label='File', menu=subMenu)  # for the menu bar
subMenu.add_command(label='Open')  # create the drop down menu for File
subMenu.add_command(label='Exit')  # create the drop down menu for File
# ************************************************* End of Submenu bar *************************************************

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