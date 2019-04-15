from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import font

def credits1(b10):
    messagebox.showinfo("Credit","Created by: Paras Jain")
    
def play(b13):
        gui.destroy()   

def buttonpress1(b1):
    b1["text"]="A"
    if (b2["text"]=="N" and b3["text"]=="T") or (b4["text"]=="C" and b7["text"]=="H") or (b5["text"]=="A" and b9["text"]=="W") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress2(b2):
    b2["text"]="N"
    if (b1["text"]=="A" and b3["text"]=="T") or (b5["text"]=="A" and b8["text"]=="O") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress3(b3):
    b3["text"]="T"
    if (b2["text"]=="N" and b1["text"]=="A") or (b6["text"]=="N" and b9["text"]=="W") or (b5["text"]=="A" and b7["text"]=="H") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress4(b4):
    b4["text"]="C"
    if (b1["text"]=="A" and b7["text"]=="H") or (b5["text"]=="A" and b6["text"]=="N") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress5(b5):
    b5["text"]="A"
    if (b2["text"]=="N" and b8["text"]=="O") or (b4["text"]=="C" and b6["text"]=="N") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress6(b6):
    b6["text"]="N"
    if (b3["text"]=="I" and b9["text"]=="W") or (b4["text"]=="C" and b5["text"]=="A") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress7(b7):
    b7["text"]="H"
    if (b1["text"]=="A" and b4["text"]=="C") or (b8["text"]=="O" and b9["text"]=="W") or (b5["text"]=="A" and b3["text"]=="T") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress8(b8):
    b8["text"]="O"
    if (b2["text"]=="N" and b5["text"]=="A") or (b7["text"]=="H" and b9["text"]=="W") :
        messagebox.showinfo("Warning","Your chances over ,check result")
        
def buttonpress9(b9):
    b9["text"]="W"
    if (b6["text"]=="N" and b3["text"]=="T") or (b8["text"]=="O" and b7["text"]=="H") or (b5["text"]=="A" and b1["text"]=="A") :
        messagebox.showinfo("Warning","Your chances over ,check result")
         
             
         #messagebox.showinfo("Warning","Your chances over ,check result")     
         
         
    

        
def Showresult(b11):
    def check(event):
            name=entry.get()
            if b1["text"]=="A" and b2["text"]=="N" and b3["text"]=="T" :
                                              messagebox.showinfo("Result","You win : "+name)
            elif b4["text"]=="C" and b5["text"]=="A" and b6["text"]=="N" :
                                              messagebox.showinfo("Result","You win : "+name)
            elif b7["text"]=="H" and b8["text"]=="O" and b9["text"]=="W" :
                                              messagebox.showinfo("Result","You win : "+name)
            else:
               messagebox.showinfo("Result","Try Again You loose : "+name)

            gui1.destroy()
    gui1=tkinter.Tk()
    gui1.geometry("250x100")
    Label(gui1,text="Enter Your Name",fg="white",bg="black").pack()
    lab=Label(gui1,text="")
    lab.pack()
    entry=Entry(gui1)
    entry.bind("<Return>",check)
    entry.pack()
    lab=Label(gui1,text="")
    lab.pack()
    lab=Label(gui1,text=" Thanks for Playing The Game, Have Fun!! ")
    lab.pack()
        #b1=Button(gui1,text="submit",command=)
        #b1.grid(row=4,column=1)
    gui1.mainloop()
    
    
                                          
        
                                          


        
def reset(b12):
    b1["text"]=" "
    b2["text"]=" "
    b3["text"]=" "
    b4["text"]=" "
    b5["text"]=" "
    b6["text"]=" "
    b7["text"]=" "
    b8["text"]=" "
    b9["text"]=" "
    
    


gui=tkinter.Tk()
gui.title("Word Guess")
b1=Button(gui,text=" ",width=10,height=5,font="Verdana 10 bold",command=lambda:buttonpress1(b1))
b1.grid(row=0,column=0)
b2=Button(gui,text=" ",width=10,height=5,font="Verdana 10 bold",command=lambda:buttonpress2(b2))
b2.grid(row=0,column=1)
b3=Button(gui,text=" ",width=10,height=5,font="Verdana 10 bold",command=lambda:buttonpress3(b3))
b3.grid(row=0,column=2)
b4=Button(gui,text=" ",width=10,height=5,font="Verdana 10 bold",command=lambda:buttonpress4(b4))
b4.grid(row=1,column=0)
b5=Button(gui,text=" ",width=10,height=5,font="Verdana 10 bold",command=lambda:buttonpress5(b5))
b5.grid(row=1,column=1)
b6=Button(gui,text=" ",width=10,height=5,font="Verdana 10 bold",command=lambda:buttonpress6(b6))
b6.grid(row=1,column=2)
b7=Button(gui,text=" ",width=10,height=5,font="Verdana 10 bold",command=lambda:buttonpress7(b7))
b7.grid(row=2,column=0)
b8=Button(gui,text=" ",width=10,height=5,font="Verdana 10 bold",command=lambda:buttonpress8(b8))
b8.grid(row=2,column=1)
b9=Button(gui,text=" ",width=10,height=5,font="Verdana 10 bold",command=lambda:buttonpress9(b9))
b9.grid(row=2,column=2)
b10=Button(gui,text="Credits",width=10,height=5,bg="yellow",fg="black",font="Verdana 10 bold",command=lambda:credits1(b10))
b10.grid(row=3,column=0)
b12=Button(gui,text="Reset",width=10,height=5,bg="blue",fg="white",font="Verdana 10 bold",command=lambda:reset(b12))
b12.grid(row=3,column=2)
b11=Button(gui,text="Result",width=10,height=5,bg="green",fg="white",font="Verdana 10 bold",command=lambda:Showresult(b11))
b11.grid(row=0,column=3)
b13=Button(gui,text="Quit",width=10,height=5,bg="red",fg="white",font="Verdana 10 bold",command=lambda:play(b13))
b13.grid(row=1,column=3)
#e1=Entry(gui,bd=2)
#e1.grid(row=1,column=4)
#L1=Label(gui,text="Click Play",fg="white",bg="black",font="Verdana 10 bold").grid(row=2,column=4)
L1=Label(gui,text="Word Guess",fg="white",bg="red",font="Verdana 10 bold").grid(row=3,column=1)
L1=Label(gui,text="Just 3 Words",width=10,height=5,fg="white",bg="orange",font="Verdana 10 bold").grid(row=3,column=3)
L1=Label(gui,text="Guess it",width=10,height=5,fg="black",bg="white",font="Verdana 10 bold").grid(row=2,column=3)

gui.mainloop()
