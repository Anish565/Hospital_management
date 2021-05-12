from tkinter import *
from tkinter import messagebox as mb

def crt(hos):
    if hos.max_patients==0:
        mb.showerror("!! ALERT !!", "Sorry, no beds available please!! go to another hospital!!")
        return
    global x,y,z,q,m,w,v
    def write():
        count = 0
        j =[]
        j.append(w.get())
        j.append(x.get())
        j.append(y.get())
        j.append(z.get())
        j.append(q.get())
        j.append(m.get())
        if v.get() == 1:
            s = 'Male'
        elif v.get() == 2:
            s = 'Female'
        print(j)
        h = []
        for i in j:
            print(i)
            if i == 1:
                h.append('P')
                count += 1
            elif i == 2:
                h.append('N')
                pass
        
        if count == 6:
            stats = 'Critical patient'
            if hos.ventilators==0:
                mb.showerror("!! ALERT !!", "Sorry, no ventilators available please!! go to another hospital!!")
                return
            hos.max_patients-=1
            hos.ventilators-=1
        elif count == 5:
            stats = 'Positive Patient'
            hos.max_patients-=1
        elif count >= 3:
            stats = 'Under observation'
            hos.max_patients-=1
        elif count >= 1:
            stats = 'Self Quarantine'
        elif count == 0:
            k = Toplevel()
            def d():
                r.destroy()
                k.destroy()
            l = Label(k,text = 'You are all healthy!!').grid(row = 1,column = 1)
            b = Button(k)
            b.config(text = 'ok',command = d)
            b.grid(row = 2,column = 1)
            return
        
        print(str(hos.Id)+'\t'+e1.get()+'\t'+e2.get()+'\t'+str(v.get())+'\t'+e3.get()+'\t'+e4.get()+'\t' +str(h[0])+'\t'+str(h[1])+'\t'+str(h[2])+'\t'+str(h[3]) +'\t'+str(h[4])+'\t'+str(h[5])+ '\t'+stats+'\n')
        f=open(hos.name+'.txt','a')
        f.write(str(hos.Id).format('-3')+'\t'+e1.get().format('^10')+'\t'+e2.get().format('^10')+'\t'+s.format('^3')+'\t'+e3.get().format('^3')+'\t'+e4.get().format('^20')+'\t'+e5.get().format('^11')+'\t'+str(h[0])+'\t'+str(h[1])+'\t'+str(h[2])+'\t'+str(h[3]) +'\t'+str(h[4])+'\t'+str(h[5])+ '\t'+stats.format('+')+'\n')
        hos.Id += 1
        f.close()
        r.destroy()

    def confirm():
        c=Toplevel()
        def d():
            r.destroy()
            c.destroy()
        c.title('Confirm')
        l=Label(c,text='Do you want to exit without saving??').grid(row=1,column=1)
        b1=Button(c)
        b2=Button(c)
        b1.config(text='yes',command=d)
        b1.grid(row=2,column=1)
        b2.config(text='no',command=c.destroy)
        b2.grid(row=2,column=2)
    r=Tk()

    v = IntVar(r,0)
    w= IntVar(r,0)
    m = IntVar(r,0)
    x= IntVar(r,0)
    q = IntVar(r,0)
    y=IntVar(r,0)
    z= IntVar(r,0)

    r.title('Patient details')
    l1=Label(r,text='First Name').grid(row=0,column=0)
    l2=Label(r,text='Last Name').grid(row=0,column=2)
    e1 = Entry(r) 
    e2 = Entry(r) 
    e1.grid(row=0, column=1) 
    e2.grid(row=0, column=3)

    l3=Label(r,text='Gender').grid(row=1)

    Radiobutton(r, text='Male', variable=v, value= 1).grid(row=1,column=1)
    Radiobutton(r, text='Female', variable=v, value= 2).grid(row=1,column=2)

    l4=Label(r,text='Age').grid(row=2,)
    e3=Entry(r)
    e3.grid(row=2,columnspan = 3)

    l5=Label(r,text='Address').grid(row=3)
    e4=Entry(r)
    e4.grid(row=3,columnspan = 3)

    l6=Label(r,text='Contact no.').grid(row=4)
    e5=Entry(r)
    e5.grid(row=4,columnspan = 3)

    l6=Label(r,text='RT-PCR').grid(row=5)

    Radiobutton(r,text='Positive',variable=w,value=1).grid(row=5,column=1)
    Radiobutton(r,text='Negative',variable=w,value=2).grid(row=5,column=2)

    l7=Label(r,text='Swab Test').grid(row=6)

    Radiobutton(r,text='Positive',variable=x,value=1).grid(row=6,column=1)
    Radiobutton(r,text='Negative',variable=x,value=2).grid(row=6,column=2)


    l8=Label(r,text='Thermal test').grid(row=7)

    Radiobutton(r,text='Positive',variable=y,value=1).grid(row=7,column=1)
    Radiobutton(r,text='Negative',variable=y,value=2).grid(row=7,column=2)


    l9=Label(r,text='Blood Test').grid(row=8)

    Radiobutton(r,text='Positive',variable=z,value=1).grid(row=8,column=1)
    Radiobutton(r,text='Negative',variable=z,value=2).grid(row=8,column=2)
    #print(z.get())
    l10 = Label(r,text = 'Nasal aspirate').grid(row = 9)

    Radiobutton(r,text='Positive',variable=q,value=1).grid(row=9,column=1)
    Radiobutton(r,text='Negative',variable=q,value=2).grid(row=9,column=2)


    l11 = Label(r,text = 'Tracheal aspirate').grid(row = 10)

    Radiobutton(r,text='Positive',variable=m,value=1).grid(row=10,column=1)
    Radiobutton(r,text='Negative',variable=m,value=2).grid(row=10,column=2)

    butonWrite = Button(r)
    butonWrite.config(text = 'Save Details', command = write)
    butonWrite.grid(row=11, column=1)

    butt=Button(r)
    butt.config(text='Exit without Saving',command=confirm)
    butt.grid(row=11,column=2)
