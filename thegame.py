from tkinter import *
from tkinter import messagebox
import random
x = Tk()
def rand():
	li = ['rock','scissors','paper']
	lk = random.choice(li)
	lb.config(text='computer: '+lk)
	en = ent.get()
	lb1.config(text='player: '+en)
	if lk == 'rock'and en == 'paper':
		messagebox.showerror('lose','try again')
	if lk == 'paper' and en == 'rock':
		messagebox.showinfo('winner','You win!')
	if lk == 'scissors' and en == 'paper':
		messagebox.showerror('lose','try again')
	if lk == 'rock' and en == 'scissors':
		messagebox.showerror('lose','try again')
	if lk == 'paper' and en == 'scissors':
		messagebox.showinfo('winner','You win!')
	if lk == 'scissors'	and en == 'rock':
		messagebox.showinfo('winner','You win!')
	if lk == 'paper' and en == 'paper':
		messagebox.showinfo('no winner','تعادل يا عم الحاج')
	if lk == 'scissors' and en == 'scissors':
		messagebox.showinfo('no winner','تعادل يا عم الحاج')
	if lk == 'rock' and en == 'rock':
		messagebox.showinfo('no winner','تعادل يا عم الحاج')	
x.geometry('350x300')
x.config(bg='violet')
lbl = Label(text='sc,r,p:game',bg='lightblue',fg='black',font=('Courier',12))
lbl.pack()
img=PhotoImage(file='C:\\Users\\HELAL\\Desktop\\paper.png')
lbs = Label(image=img)
lbs.pack()
chos = Label(text='choose:')
chos.pack()
lb = Label(text='',bg='black',fg='white')
lb.pack()
lb1 = Label(text='')
lb1.pack()
ent = Entry(font=('Courier',12))
ent.pack()
but3 = Button(text='random',command=rand)
but3.pack()
x.mainloop()