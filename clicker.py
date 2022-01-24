from tkinter import*
k=0
def klikker(event):
	global k
	k+=1
	nupp.config(text=k)
def klikker_(event):
	global k
	k+=100
	nupp.config(text=k)
def txt_to_lbl(event):
	text=txt.get()
	lbl.configure(text=text)
	txt.delete(0,END)
def valimine(var:str):
	valik=var.get()
	lbl.configure(text=var)
	
aken=Tk()
aken.title("爪卂ㄒ丂ㄩ尺丨")
aken.geometry("1280x1024")
nupp=Button(aken,text="𝓢𝓱𝓪𝓴𝓾𝓻",font="TimesNewRoman 55",width=20,fg="white",bg="#001332",relief=RAISED)
nupp.pack() #side=LEFT x=300,y=280
nupp.bind("<Button-1>",klikker)
nupp.bind("<Button-3>",klikker_)
lbl=Label(aken,text="Hallo, this is clicker",height=3,width=20,font="Arial 20",fg="grey",bg="lightblue",relief="solid")
lbl.pack()
txt=Entry(aken,width=20,font="Arial 20",fg="white",bg="grey",justify=CENTER)
txt.pack()
txt.bind("<Return>", txt_to_lbl) #Enter

i1=PhotoImage(file="AMOGUS.png")
i2=PhotoImage(file="banan.gif")
i3=PhotoImage(file="8552.gif")
var=StringVar()
var.set("Üks")

r1=Radiobutton(aken,image=i1,variable=var,value="Üks", command=valimine)
r2=Radiobutton(aken,image=i2,variable=var,value="Kaks", command=valimine)
r3=Radiobutton(aken,image=i3,variable=var,value="Kolm", command=valimine)
aken.mainloop()