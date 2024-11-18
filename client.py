import socket
from threading import Thread
from tkinter import *
import random
from PIL import ImageTk,Image

def ask_name():
    global player_name
    global name_entry
    global canvas1
    global nameWindow
    global screen_width
    global screen_height

    nameWindow = Tk()
    nameWindow.title("Tambola")
    nameWindow.geometry('800x600')

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()
    print(screen_width,screen_height)

    bg = ImageTk.PhotoImage(file="assets/background.png")

    canvas1 = Canvas(nameWindow,width=500,height=500)
    canvas1.pack(fill="both",expand=True)
    canvas1.create_image(0,0,image=bg,anchor='nw')
    canvas1.create_text(screen_width/4.5,screen_height/8,text='Enter your name :', font=('Chalkboard SE',60),fill="black")

    name_entry = Entry(nameWindow,justify="center",bd=5,bg='white',font=('Chalkboard SE',30),width=15)
    name_entry.place(x=screen_width/7,y=screen_height/5.5)

    button = Button(nameWindow,text="Save",font=("Chalkboard SE",30),width=11,command=save_name,height=2,bg='#80deea',bd=3)
    button.place(x=screen_width/6,y=screen_height/4)

    nameWindow.resizable(True,True)
    nameWindow.mainloop()

def rcv_msg():
    pass

def save_name():
    global SERVER
    global player_name
    global nameWindow
    global name_entry

    player_name = name_entry.get()
    name_entry.delete(0,END)
    nameWindow.destroy()

    SERVER.send(player_name.encode())

def setup():
    global SERVER
    global PORT
    global IP_ADDR

    PORT = 6000
    IP_ADDR = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDR,PORT))

    ask_name()

    recv_msg_thread = Thread(target=rcv_msg)
    recv_msg_thread.start()

setup()