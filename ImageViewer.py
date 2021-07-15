import tkinter as tk
from PIL import ImageTk , Image
import os

directory = r'F:/PythonProject/images'
n = len(os.listdir(directory))
curr = 1




def goback():
    global curr
    global n
    if(curr == 1):
        curr = n
    else:
        curr = curr-1
    
    refresh(curr)

    # showImg(curr)

def gofront():
    global curr
    global n
    if(curr == n):
        curr = 1
    else:
        curr = curr+1
    refresh(curr)

root = tk.Tk()
    
root.geometry("500x500")
root.config(bg = 'red')
root.rowconfigure([0,1,2] , minsize = 100 , weight = 1)
root.columnconfigure([0,1,2] , minsize = 100 , weight = 1)


def refresh(pos):
    global root    
    
    ##For title
    titleLabel = tk.Label(text = 'I M A G E V I E W E R')

    titleLabel.config(font = ('Verdana' , 15))

    titleLabel.grid(row = 0 , column = 1)


    ##For image
    try:
        img = ImageTk.PhotoImage(Image.open(directory+ './' + str(pos)  + '.png'))
        imgLabel = tk.Label(image = img)
        imgLabel.grid(row = 1 , column = 1)
    except:
        imgLabel = tk.Label(text = 'Error in opening')
        imgLabel.grid(row = 1 , column = 1)


    ##For button

    back = tk.Button(text = 'B A C K' , width = 20 , height =5 , command = goback)
    front = tk.Button(text = 'F O R W A R D' , width = 20 , height = 5, command = gofront)

    back.grid(row = 2 , column = 0 ,padx = 15 , pady =5)
    front.grid(row = 2 , column = 2 , padx = 15 , pady =5)

    root.mainloop()

refresh(1)