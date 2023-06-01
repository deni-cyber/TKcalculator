# calculator
from tkinter import *
root=Tk()
root.configure(background='teal')
root.geometry('300x400')

class Calculate:
    def __init__(self):
        pass
    def set1():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,'1')
        entry.configure(state='disabled')
        
        
    def set2():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,'2')
        entry.configure(state='disabled')

    def set3():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,'3')
        entry.configure(state='disabled')

    def set4():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,'4')
        entry.configure(state='disabled')

    def set5():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,'5')
        entry.configure(state='disabled')

    def set6():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,6)
        entry.configure(state='disabled')

    def set7():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,'7')
        entry.configure(state='disabled')

    def set8():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,'8')
        entry.configure(state='disabled')

    def set9():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,'9')
        entry.configure(state='disabled')

    def set0():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,'0')
        entry.configure(state='disabled')

    def setp():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,'+')
        entry.configure(state='disabled')

    def sets():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,'-')
        entry.configure(state='disabled')

    def setm():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,'x')
        entry.configure(state='disabled')

    def setd():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.insert(l,'÷')
        entry.configure(state='disabled')

    def dele():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        if l!=0:
            current=current[0:l-1]
            entry.delete(0,l)
            entry.insert(0,current)
        else:
            pass
        entry.configure(state='disabled')

    def clear():
        entry.configure(state='normal')
        current=str(entry.get())
        l=len(current)
        entry.delete(0,l)
        entry.configure(state='disabled')

    def solve():
        entry.configure(state='normal')
        expression=str(entry.get())
        l=len(expression)
        p=expression.find('+')
        if p==True:
            v1=int (expression[:p])
            v2=int (expression[p+1:])
            ans=v1+v2
        else:
            ans='error'

        entry.delete(0,l)
        entry.insert(0,ans)
        entry.configure(state='disabled')
    


frame=Frame(root,background='grey',border=2)
frame.pack()
entry=Entry(frame,state='disabled',font=(24),borderwidth=5,bg='grey',fg='red')
entry.grid(row=0,column=0,columnspan=3)



but1=Button(frame, text='1',font=(24),borderwidth=5, bg='#808080',fg='white',command=Calculate.set1)
but2=Button(frame, text='2',font=(24),borderwidth=5, bg='#808080',fg='white',command=Calculate.set2)
but3=Button(frame, text='3',font=(24),borderwidth=5, bg='#808080',fg='white',command=Calculate.set3)

but4=Button(frame, text='4',font=(24),borderwidth=5, bg='#808080',fg='white',command=Calculate.set4)
but5=Button(frame, text='5',font=(24),borderwidth=5, bg='#808080',fg='white',command=Calculate.set5)
but6=Button(frame, text='6',font=(24),borderwidth=5, bg='#808080',fg='white',command=Calculate.set6)

but7=Button(frame, text='7',font=(24),borderwidth=5, bg='#808080',fg='white',command=Calculate.set7)
but8=Button(frame, text='8',font=(24),borderwidth=5, bg='#808080',fg='white',command=Calculate.set8)
but9=Button(frame, text='9',font=(24),borderwidth=5, bg='#808080',fg='white',command=Calculate.set9)

but0=Button(frame, text='0',font=(24),borderwidth=5, bg='#808080',fg='white',command=Calculate.set0)

butPlus=Button(frame, text='+',font=(24),borderwidth=5, bg='black',fg='white',command=Calculate.setp)
butMinus=Button(frame, text=' - ',font=(24),borderwidth=5, bg='black',fg='white',command=Calculate.sets)
butMultiply=Button(frame, text='x',font=(24),borderwidth=5, bg='black',fg='white',command=Calculate.setm)
butDivide=Button(frame, text='÷',font=(24),borderwidth=5, bg='black',fg='white',command=Calculate.setd)
butEquals=Button(frame,text='    =    ',font=(24),borderwidth=5, bg='green',command=Calculate.solve)
butDel=Button(frame,text='←',font=(24),borderwidth=5, bg='red',command=Calculate.dele)
butclear=Button(frame,text='Clear',font=(24),borderwidth=5, bg='blue',command=Calculate.clear)

but1.grid(row=1 ,column=0 )
but2.grid(row=1 ,column= 1)
but3.grid(row=1 ,column= 2)
but4.grid(row=2 ,column=0 )
but5.grid(row=2 ,column= 1)
but6.grid(row=2 ,column= 2)
but7.grid(row=3 ,column=0 )
but8.grid(row=3 ,column= 1)
but9.grid(row=3 ,column=2 )

but0.grid(row=4,column= 1)
butPlus .grid(row=4,column=0 )
butMinus .grid(row=4,column=2 )

butMultiply .grid(row=5 ,column=0 )
butDivide.grid(row=5, column=1 )
butDel.grid(row=5,column= 2)
butclear.grid(row=6,columnspan=1)
butEquals.grid(row=6,column=2)

mainloop()
