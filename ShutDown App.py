#Libraries
from tkinter import *
from tkinter import messagebox, filedialog, simpledialog, colorchooser
import os

#Application setup
root = Tk()
root.geometry("600x580+380+30")
root.resizable(False,False)
root.configure(bg="slate grey")
root.title("ShutDown App")

#Functions
lb = Button(root,text="...",width=3,height=2,bg="slate grey",fg="white")
lb.place(x=300,y=0)
def color(event):
    cls = colorchooser.askcolor(title="Select color to change")
    root.config(bg=cls[1])
    btn1.config(bg=cls[1])
    btn2.config(bg=cls[1])
    btn3.config(bg=cls[1])
    btn4.config(bg=cls[1])
    btn5.config(bg=cls[1])

def message():
    messagebox.askokcancel("Message","To change the background color press Clt+g")

def restarttime():
    if(messagebox.askyesno("ShutDown","Do you want to restart the system? It will be restart"
    "after 30 sec.")):
        os.system("shutdown /r /t 30")
    else:
        exit

def shutdown():
    if(messagebox.askyesno("ShutDown","Do you want to shutdown the system?")):
       os.system("shutdown /s /t 1")
    else:
        exit

def restart():
    if(messagebox.askyesno("ShutDown","Do Do you want to restart the system?")):
        os.system("shutdown /r /t 1")
    else:
        exit
    
#Application creation
img1 = PhotoImage(file="E:\\pyImages\\shut_downapp_logo.png")
img2 = PhotoImage(file="E:\\pyImages\\restarttime.png")
img3 = PhotoImage(file="E:\\pyImages\\close.png")
img4 = PhotoImage(file="E:\\pyImages\\restart.png")
img5 = PhotoImage(file="E:\\pyImages\\shutdown.png")
root.iconphoto(False,img1)
btn1 =  Button(root,image=img2,bg="slate grey",activebackground="slate grey",bd=0,cursor="hand2",
        command=restarttime)
btn1.place(x=40,y=10)
btn2 =  Button(root,image=img3,bg="slate grey",activebackground="slate grey",bd=0,cursor="hand2",
        command=root.destroy)
btn2.place(x=350,y=10)
btn3 =  Button(root,image=img4,bg="slate grey",activebackground="slate grey",bd=0,cursor="hand2",
        command=restart)
btn3.place(x=40,y=300)
btn4 =  Button(root,image=img5,bg="slate grey",activebackground="slate grey",bd=0,cursor="hand2",
        command=shutdown)
btn4.place(x=350,y=300)
btn5 = Button(root,text="...",width=3,height=2,bg="slate grey",fg="white",command=message)
btn5.place(x=300,y=0)
root.bind('<Control-g>',color)
root.mainloop()
