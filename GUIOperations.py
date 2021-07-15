import tkinter as tk

def inc():
    v = int(l1['text'])
    l1['text']  = str(v+1)

def dec():
    v = int(l1['text'])
    l1['text']  = str(v-1)

def mul():
    v = int(l2['text'])
    l2['text']  = str(v*2)

def div():
    v = int(l2['text'])
    if(v==1):
        return
    l2['text']  = str(v//2)

firstWindow = tk.Tk()

f1 = tk.Frame(master = firstWindow , bg = 'red' , width = 50 , height = 50)
f2 = tk.Frame(master = firstWindow , bg = 'yellow' , width = 20 , height = 20)

f1.rowconfigure([0] , minsize = 50 ,weight = 1)
f1.columnconfigure([0,1,2] , minsize = 50 , weight = 1)

bt1 = tk.Button(master = f1 , text = '+' ,width = 20 , command = inc)
l1 = tk.Label(master = f1 , text = '0' ,width = 10)
bt2 = tk.Button(master = f1 , text = '-' , width = 20 , command = dec)

bt1.grid(row = 0 , column = 0 , padx = 2 , pady = 2 )
l1.grid(row = 0 , column = 1 ,padx = 2 , pady = 2)
bt2.grid(row = 0 , column = 2 ,padx = 2 , pady = 2)

f1.pack(fill = tk.BOTH ,expand = True)

###################################################

f2.rowconfigure([0] , minsize = 50 ,weight = 1)
f2.columnconfigure([0,1,2] , minsize = 50 , weight = 1)  #Configure the rows and columns

bt3 = tk.Button(master = f2 , text = '*' ,width = 20 , command = mul)
l2 = tk.Label(master = f2 , text = '1' ,width = 10)
bt4 = tk.Button(master = f2 , text = '/' , width = 20 , command = div)

bt3.grid(row = 0 , column = 0 , padx = 2 , pady = 2 )
l2.grid(row = 0 , column = 1 ,padx = 2 , pady = 2)
bt4.grid(row = 0 , column = 2 ,padx = 2 , pady = 2)



f2.pack(fill = tk.BOTH , expand = True)


firstWindow.mainloop()



