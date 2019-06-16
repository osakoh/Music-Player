from tkinter import *


root = Tk()  # creates a window
root.title("Music Player")
root.iconbitmap(r'red-audio.ico')
# *************** Centralise the window **********************
window_height = 300
window_width = 500
# specifies width and height of window1
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# specifies the co-ordinates for the screen
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.configure(background='#6b778d')
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
root.resizable(False, False)  # This code helps to disable windows from resizing
# *************** End of code **********************

root.mainloop()