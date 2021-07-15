import tkinter as tk
from tkinter import filedialog
from PIL import Image , ImageTk
import ImageToString as ITS
import Database as db




root = tk.Tk()
root.geometry("500x500")
root.config(bg = 'grey')

root.rowconfigure([0,1,2,3,4,5,6,7,8] , minsize = 50 , weight = 1)
root.columnconfigure([0,1,2] , minsize = 100 , weight =1)

imgLabel =  tk.Label()
imgLabel.grid(row = 1 , column = 1)
imgLabel.grid_forget()


fileLabel = tk.Label(text = 'C H O O S E N F I L E')
fileLabel.grid(row = 3 , column = 1)


fineLabel = tk.Label(text = 'E N T E R  T H E  F I N E  D E T A I L S')
fineDetails = tk.Entry(master = root)
fineLabel.grid(row = 4 ,column = 0)
fineDetails.grid(row = 4 , column = 1)

cLabel = tk.Label(text = 'E N T E R  T H E  C O M P L A I N T')
cDetails = tk.Entry(master = root)
cLabel.grid(row = 5 , column = 0)
cDetails.grid(row = 5 , column = 1)

cityLabel = tk.Label(text = 'E N T E R  T H E  C I T Y')
cityDetails = tk.Entry(master = root)
cityLabel.grid(row = 6 , column = 0)
cityDetails.grid(row = 6 , column = 1)

policeLabel = tk.Label(text = 'E N T E R  P O L I C E I D')
policeDetails = tk.Entry(master = root)
policeLabel.grid(row = 7 , column = 0)
policeDetails.grid(row = 7 , column = 1)


def submit():
    global fineDetails
    global cDetails
    global cityDetails
    global policeDetails

    print(fineDetails.get())
    print(cDetails.get())
    print(cityDetails.get())
    print(policeDetails.get())

    refresh()

def open():
    global root
    
    global fileLabel
    global imgLabel

    imgLabel.grid_forget()
    fileLabel.grid_forget()
   

    fileChosen = filedialog.askopenfile(initialdir="/").name
    fileLabel = tk.Label(text = fileChosen)

    fileLabel.grid(row = 3 , column = 1)

    img = ImageTk.PhotoImage(Image.open(fileChosen))
    
    try:
        imgLabel = tk.Label(image = img)
        imgLabel.grid(row = 1 , column = 1)
    except:
        imgLabel = tk.Label(text = 'Error in opening the file')
        imgLabel.grid(row = 1 , column = 1)
    
    number = ITS.extract(fileChosen)
    
    tk.messagebox.showinfo('Plate Number' , number)

    refresh()



def clear():
    global root
    global imgLabel
    global fileLabel
    
    global fineDetails
    global cDetails
    global cityDetails
    global policeDetails

    imgLabel.grid_forget()
    fileLabel.grid_forget()

    fineDetails.delete(0,tk.END)
    fineDetails.insert('0' , '')

    cDetails.delete(0,tk.END)
    cDetails.insert('0', '')

    cityDetails.delete(0,tk.END)
    cityDetails.insert('0' , '')

    policeDetails.delete(0,tk.END)
    policeDetails.insert('0' ,'')

    fileLabel = tk.Label(text = 'C H O O S E N F I L E')
    fileLabel.grid(row = 3 , column = 1)


    refresh()

# def show():
#     try:
#         second = tk.Tk()

#         obj = db.connectdb("testdb")
#         data = db.selectquery(obj)

#         textBox = tk.Text(master = second)
        
#         for x in data:
#             for i in x:
#                 textBox.insert(tk.END , i)
#                 textBox.insert(tk.END , "  ")
#             textBox.insert(tk.END,"\n")

#         textBox.pack()


#         second.mainloop()
#     except:
#         tk.messagebox.showinfo("Error" , "Error in accessing the database")

def refresh():

    global root

    titleLabel = tk.Label(text = 'T E X T E X T R A C T E R')
    titleLabel.grid(row = 0 , column = 1)

    browseBtn = tk.Button(text = 'C H O O S E F I L E' , command = open)
    browseBtn.grid(row =  2, column = 0)

    ClearBtn = tk.Button(text = 'C L E A R' , command =clear)   
    ClearBtn.grid(row =  2, column = 2)

    BtnSubmit = tk.Button(text = 'S U B M I T' , command = submit)
    BtnSubmit.grid(row = 8 , column = 1)

    root.mainloop()


refresh()