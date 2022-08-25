import tkinter
from tkinter import*
import time
from PIL import Image,ImageTk
import psutil
import platform
import cpuinfo

alpha=10000
print()
root=tkinter.Tk()
root.title("LARA")

root.configure(background="black")
root.resizable(width=False,height=False)
root.geometry("1000x675+1+30")
def clock():
    y=time.strftime('%I:%M:%S:%p')
    my_label.config(text=y)
    my_label.after(200,clock)
my_label=tkinter.Label(root,text="",font=("algerian 50"),fg="white",bg="black")
my_label.pack(anchor="nw")

def po():
    u=time.strftime('%A')
    day.config(text=u)
    day.after(200,po)

day=tkinter.Label(root,text="",font=("algerian 20"),fg="DodgerBlue2",bg="black")
day.pack(anchor='nw')

def date():
    v=time.strftime('%d %B %Y')
    da.config(text=v)
    da.after(200,date)

def ko():
    r=psutil.sensors_battery()[0]
    mr.config(text=f"Battery:{r} %")
    if r>=0 and r<20:
        mr.config(fg="red")
    if r>=20 and r<35:
        mr.config(fg="orange")
    if r>=35 and r<45:
        mr.config(fg="yellow")
    if r>=45:
        mr.config(fg="green")

    mr.after(200,ko)
def power():
    r=psutil.sensors_battery()[2]
    if r==0:
        ba.config(text="Power plugged:NO")
    if r==1:
        ba.config(text="Power plugged:Yes")

    
    ba.after(200,power)
def cp():
    r=psutil.cpu_percent()
    cpu.config(text=f"CPU percentage= {r}")
    cpu.after(250,cp)



image=Image.open("icons/hi.png")
image=image.resize((300,300), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
image_label=Label(image=photo,bg="black")

da=Label(root,text="",font=("algerian 20"),fg="DodgerBlue2",bg="black")
da.pack(anchor='nw')

mr=Label(root,text="",font=("arial 20"),bg="black")
mr.pack(anchor="ne")

ba=Label(root,text="",font=("arial 20"),fg="white",bg="black")
ba.pack(anchor="ne")
f=Frame(root,bg="red",relief=RAISED,borderwidth=5)
n= platform.node()
m=platform.machine()
an=Label(f,text='            PC_name='+n+"           machine="+m,font="arial 20",fg="DarkOrange2",bg="black")
an.pack(side=RIGHT)
cpu=Label(root,text='',font="arial 20",fg="orange",bg="black")

pp=cpuinfo.get_cpu_info()['brand_raw']
f2=Frame(root,bg="black",relief=RAISED,borderwidth=0)

p=Label(f2,text="Processor is "+pp,font="arial 20",fg="cyan",bg="black")
p.pack()
cpu.pack(anchor="ne")
a=platform.system()
b=platform.release()
windows=Label(f,text=a+""+b,font="arial 20",fg="DarkOrange2",bg="black")
windows.pack(side=LEFT)
f.pack(side=BOTTOM)
f2.pack(side=BOTTOM)



image_label.pack(anchor="center")




clock()
po()
date()
ko()
power()
cp()
root.mainloop()
