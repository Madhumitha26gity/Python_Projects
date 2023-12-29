import tkinter
import tkinter.messagebox
parent=tkinter.Tk()
parent.title("REGISTRATION FORM")
parent.geometry("500x400")
parent.config(bg="lightblue")
radio=tkinter.StringVar()
var1=tkinter.IntVar()
var2=tkinter.IntVar()
def sub():
	submit=tkinter.Toplevel(parent)
	submit.title("REGISTRATION STATUS")
	submit.geometry("500x400")

	name=tkinter.Label(submit,text="NAME:")
	name.grid(row=0,column=3,pady=10,padx=5)
	user=tkinter.Label(submit,text=e1.get())
	user.grid(row=0,column=4)

	app=tkinter.Label(submit,text="APPLICATION NUMBER:")
	app.grid(row=1,column=3,pady=10,padx=5)
	num=tkinter.Label(submit,text=e2.get())
	num.grid(row=1,column=4)

	gender=tkinter.Label(submit,text="GENDER:")
	gender.grid(row=2,column=3,pady=10,padx=5)
	gen=tkinter.Label(submit,text=radio.get())
	gen.grid(row=2,column=4,pady=10,padx=5)

	phone=tkinter.Label(submit,text="PHONE:")
	phone.grid(row=3,column=3,pady=10,padx=5)
	ph=tkinter.Label(submit,text=e3.get())
	ph.grid(row=3,column=4,pady=10,padx=5)

	email=tkinter.Label(submit,text="E-MAIL ID:")
	email.grid(row=4,column=3,pady=10,padx=5)
	em=tkinter.Label(submit,text=e4.get())
	em.grid(row=4,column=4,pady=10,padx=5)

	qual=tkinter.Label(submit,text="QUALIFICATION:")
	qual.grid(row=5,column=3,pady=10,padx=5)
	q1="UG"
	q2="PG"
	q= q1+q2
	if(var1==1):
		q3=tkinter.Label(submit, text=q1)
		q3.grid(row=5,column=4)
	if(var2==1):
		q3=tkinter.Label(submit,text=q2)
		q3.grid(row=5,column=4)

	msg=tkinter.Label(submit,text="SUBMITTED SUCCESSFULLY!")
	msg.grid(row=6,column=5)

	submit.mainloop()

def can():
	tkinter.messagebox.showinfo("REGISTRATION STATUS","CANCELLED SUCCESSFULLY! ")


name=tkinter.Label(parent,text="NAME:")
name.grid(row=0,column=3,pady=10,padx=5)
e1= tkinter.Entry(parent)
e1.grid(row=0,column=4)

app=tkinter.Label(parent,text="APPLICATION NUMBER:")
app.grid(row=1,column=3,pady=10,padx=5)
e2= tkinter.Entry(parent)
e2.grid(row=1,column=4)

gender=tkinter.Label(parent,text="GENDER:")
gender.grid(row=2,column=3,pady=10,padx=5)

g1=tkinter.Radiobutton(parent,text="MALE",value="MALE",variable=radio)
g1.grid(row=2,column=4)
g2=tkinter.Radiobutton(parent,text="FEMALE",value="FEMALE",variable=radio)
g2.grid(row=2,column=5)

phone=tkinter.Label(parent,text="PHONE:")
phone.grid(row=3,column=3,pady=10,padx=5)
e3= tkinter.Entry(parent)
e3.grid(row=3,column=4)

email=tkinter.Label(parent,text="E-MAIL ID:")
email.grid(row=4,column=3,pady=10,padx=5)
e4= tkinter.Entry(parent)
e4.grid(row=4,column=4)

qual=tkinter.Label(parent,text="QUALIFICATION:")
qual.grid(row=5,column=3,pady=10,padx=5)

e5= tkinter.Checkbutton(parent,text="UG",variable=var1)
e5.grid(row=5,column=4)
e6= tkinter.Checkbutton(parent,text="PG",variable=var2)
e6.grid(row=5,column=5)

b1 = tkinter.Button(parent, text="SUBMIT",command=sub)
b1.grid(row=8,column=4) 
b2 = tkinter.Button(parent, text="CANCEL",command=can)
b2.grid(row=8,column=7)

parent.mainloop()
