#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import html5lib
import random
import urllib.request
import base64
from tkinter.ttk import *
from tkinter import messagebox as mb
from patientslog import *
from functools import partial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

#import CovidReference as stats
DF=pd.read_html("https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US:en")
df=DF[0]
df=df[df['Recovered'] != '—']
df=df[df['Location'] != 'United Kingdom']
df=df[df['Location'] != 'Netherlands']
#print (df.head(10))
df1=df
df1=df
df1=df1.drop(df1.index[5:12])
df1=df1.head(6)
df1['Recovered']=df1['Recovered'].apply(pd.to_numeric)



# from mainpage import *
# def xyz():
text = 'STAY HOME\nKEEP A SAFE DISTANCE\nWASH YOUR HANDS OFTEN\nCOVER YOUR COUGH\nSICK ? CALL THE HELPLINE'
text_li = list(text.split('\n'))
color_li = ['black', 'red', 'white', 'yellow']


def on1(e):
    button1['background'] = '#667eea'
    button1.config(relief = 'sunken')
def off1(e):
    button1['background'] = 'white'
    button1.config(relief = 'ridge')

def onc(e):
    Credits['background'] = '#667eea'
    Credits.config(relief = 'sunken')
def offc(e):
    Credits['background'] = 'white'
    Credits.config(relief = 'ridge')

def ong(e):
    graph_button['background'] = '#667eea'
    graph_button.config(relief = 'sunken')
def offg(e):
    graph_button['background'] = 'white'
    graph_button.config(relief = 'ridge')


def on2(e):
    button2['background'] = '#667eea'
    button2.config(relief = 'sunken')
def off2(e):
    button2['background'] = 'white'
    button2.config(relief = 'ridge')

def on5(e):
    button5['background'] = '#667eea'
    button5.config(relief = 'sunken')
def off5(e):
    button5['background'] = 'white'
    button5.config(relief = 'ridge')

def on4(e):
    button4['background'] = '#667eea'
def off4(e):
    button4['background'] = 'white'


class WebImage:
    def __init__(self, url):
        u = urllib.request.urlopen(url)
        raw_data = u.read()
        u.close()
        self.image = PhotoImage(data=base64.encodebytes(raw_data))

    def get(self):
        return (self.image)


from tkinter import *


class windows:
    def __init__(self, master, title, bg='white', geo='1024x640'):
        self.master = master
        master.title(title)
        master.geometry(geo)
        master['bg'] = bg

    '''def Destroy(self):
        self.master.destroy()'''


main = Tk()
Main = windows(main, 'Home', bg='#a1c4fd')
main.resizable(False,False)


Label(main, text='Welcome to Hospital  Management System', font=('algerian', 32, 'bold'), fg='purple',bg='#a1c4fd').pack()

mb.showwarning('ALERT','you need an active network connection\n\n\nThe program would start in a moment')

precaution = Label(main, text='PRECAUTIONS', bg='green', fg='red', width=70, font=('times new roman', 20, 'normal'))
precaution.pack()


k = 0


def change(precaution):
    def count():
        global k
        precaution.config(text=text_li[k], bg=color_li[k], fg=color_li[3 - k])
        k += 1
        precaution.after(1250, count)
        if k == 4:
            k = 0

    count()

frame_1 = Frame(main, bg='#a1c4fd')
frame_1.pack(pady = 10,fill='x')

image1 = WebImage('http://coronavirus.bernews.com/wp-content/uploads/2020/03/giphyrefgrwegwer.gif')
Label(main, image=image1.get()).pack(pady=(30))

frame_2 = Frame(main,bg='#a1c4fd')
frame_2.pack(fill='both',expand=True,pady=(0,30))

frame_3 = Frame(main,bg='#a1c4fd')
frame_3.pack(side='bottom',fill='both')

x_list = []


class hospital:
    def __init__(self, name, doctors, nurses, areas, ventilators, max_patients, Id, password):
        # self.patients = patients
        try:
            self.doctors = int(doctors)
            
            
            self.nurses = int(nurses)
            self.ventilators = int(ventilators)
            self.max_patients = int(max_patients)
            self.Id = int(Id)
            self.name = name
            self.area = areas
            self.password = password
        except ValueError:
            mb.showerror('Input Mismatch','Give appropiate inputs')

    def get(self):
        x_list = [self.name, self.area, self.doctors, self.nurses, self.ventilators, self.max_patients, self.Id,
                  self.password]
        return x_list


hos_list = []

try:
    f = open('hos_list.txt', 'r')
    lines = f.readlines()

    for i in lines:
        i = i.strip('\n')
        O_buff = i.split(',')
        #print(O_buff)
        X_buff = hospital(password=O_buff[7], name=O_buff[0], doctors=O_buff[2], nurses=O_buff[3], areas=O_buff[1],
                          ventilators=O_buff[4], max_patients=O_buff[5], Id=O_buff[6])
        hos_list.append(X_buff)
    f.close()
except FileNotFoundError:
    f = open('hos_list.txt', 'w')
    f.close()

fields = ['Hospital Name: ', 'Area: ', 'Number of doctors:- ', 'No. of Nurses: ', 'Ventilators available: ',
          'Maximum Patient Admissions: ']
pat = ['UID', 'First Name: ', 'Last Name: ', 'Gender: ', 'Age: ', 'Address: ', 'Contact: ', 'Test #1: ', 'Test #2: ',
       'Test #3: ', 'Test #4: ', 'Test #5: ', 'Test #6: ', 'Category: ']


def extract(fname, x):
    f = open(fname, 'r')
    xc = f.readlines()
    ALL = []
    sp = []
    for i in xc:
        k = i.split('\t')
        sp.append(k)
        ALL.append(k[x])
    f.close()
    return ALL, sp


# file_list = []
def add_hospital():
      add_win = Tk()
      Add_win = windows(add_win, 'Create Profile ', 'black', '480x280')

      name = Label(add_win, text='Enter Name of the hospital:- ', justify='left', fg='white', bg='black').grid(row=0,
                                                                                                             column=0,
                                                                                                             sticky='w')
      name_entry = Entry(add_win)
      name_entry.grid(row=0, column=1)

      doctors = Label(add_win, text='Total no. of doctors present in the hospital:- ', justify='left', fg='white',
                    bg='black').grid(row=1, column=0, sticky='w')
      doctors_entry = Entry(add_win)
      doctors_entry.grid(row=1, column=1)

      nurses = Label(add_win, text='Total number of nurses in the hospital:- ', justify='left', fg='white',
                   bg='black').grid(row=2, column=0, sticky='w')
      nurses_entry = Entry(add_win)
      nurses_entry.grid(row=2, column=1)

      areas = Label(add_win, text='Enter area : ', justify='left', fg='white', bg='black').grid(row=3, column=0,
                                                                                              sticky='w')
      areas_entry = Entry(add_win)
      areas_entry.grid(row=3, column=1)

      ventilators = Label(add_win, text='Total number of ventilators available in the hospital:- ', justify='left',
                        fg='white', bg='black').grid(row=4, column=0, sticky='w')
      ventilators_entry = Entry(add_win)
      ventilators_entry.grid(row=4, column=1)

      max_patients = Label(add_win, text='Maximum patients can be allowed in the hospital:- ', justify='left', fg='white',
                         bg='black').grid(row=5, column=0, sticky='w')
      max_patients_entry = Entry(add_win)
      max_patients_entry.grid(row=5, column=1)

      password = Label(add_win, text='Password : ', justify='left', fg='white',
                     bg='black').grid(row=6, column=0, sticky='w')
      password_entry = Entry(add_win, show='*')
      password_entry.grid(row=6, column=1)

      def Saving():
            if (((name_entry.get()).strip()=='') or ((password_entry.get()).strip()== '') ):
                mb.showerror('!!Input1 Mismatch!!','Give appropiate input!')
            elif (((((doctors_entry.get()).strip())=='') or (((nurses_entry.get()).strip())=='') or (((max_patients_entry.get()).strip())=='') or (((ventilators_entry.get()).strip())=='' ))):
                mb.showerror('!!Input1 Mismatch!!','Give appropiate input!') 
                
            elif ((((doctors_entry.get()).strip()).isalpha()) or (((nurses_entry.get()).strip()).isalpha()) or (((max_patients_entry.get()).strip()).isalpha()) or (((ventilators_entry.get()).strip()).isalpha()) ):
                mb.showerror('!!Input1 Mismatch!!','Give appropiate input!')
            else:
                
                try:

                      col, xc = extract(name_entry.get() + '.txt', 0)
                      P_buff = hospital(name_entry.get(), doctors_entry.get(), nurses_entry.get(), areas_entry.get(),
                                  ventilators_entry.get(), max_patients_entry.get(), int(col[-1]) + 1, password_entry.get())
                except FileNotFoundError:
                      P_buff = hospital(name_entry.get(), doctors_entry.get(), nurses_entry.get(), areas_entry.get(),
                              ventilators_entry.get(), max_patients_entry.get(), 0, password_entry.get())
            
                hos_list.append(P_buff)
                add_win.destroy()

            '''if name_entry.==None or doctors_entry.get()== None or nurses_entry.get(), areas_entry.get(),
                              ventilators_entry.get(), max_patients_entry.get(), int(col[-1]) + 1, password_entry.get())'''
            #print(hos_list)

            
      def a0(e):
            submit_button['background'] = '#667eea'
      def a2(e):
            submit_button['background'] = 'white'
      submit_button = Button(add_win, text='SUBMIT', command=Saving)
      submit_button.bind('<Enter>', a0)
      submit_button.bind('<Leave>', a2)
      submit_button.grid(row=7, column=0, sticky='s')
    # P_buff=hospital(name,doctors,nurses,areas,ventilators,max_patients)
    # hos_list.append(P_buff)
    # file_list.append(open('name','w')
      '''copyright_label = Label(add_win,text='© APASCAS',bg='#a1c4fd',fg='#dce7fa',font=('times new roman',12,'bold'))
      copyright_label.grid(row=10,column=1)'''
    
def view_hospital():
      view_win = Tk()
      View_win = windows(view_win, 'DETAILS',geo='600x500')

      n = StringVar()
      Label(view_win, text='Choose hospital').grid(row=0, pady='50')
      choose1 = Combobox(view_win, width=45, textvariable=n)
      choose1['values'] = [i.name for i in hos_list]
      choose1.grid(row=0, column=1)
      choose1.current()

      def view_data(event):
          index = choose1.current()

          details_list = hos_list[index].get()

          frame = Frame(view_win)
          frame.grid(row=5, column=1, rowspan=10)
        # print(details_list)
          for i in range(len(details_list)-2):
                label_1 = Label(frame, text=fields[i], font=('calibre', 12, 'bold'))
                label_2 = Label(frame, text=details_list[i])
                label_1.grid(row=i, column=0, sticky='w')
                label_2.grid(row=i, column=1)

      choose1.bind('<<ComboboxSelected>>', view_data)
    # view_but = Button(view_win, text = 'VIEW').grid()
      def q0(e):
            q1['background'] = '#667eea'
      def q2(e):
            q1['background'] = 'white'
      q1 = Button(view_win, text='QUIT', command=view_win.destroy)
      q1.bind('<Enter>', q0)
      q1.bind('<Leave>', q2)  
      q1.grid(row=70)
      '''copyright_label = Label(view_win,text='© APASCAS',bg='#a1c4fd',fg='#dce7fa',font=('times new roman',12,'bold'))
      copyright_label.grid(row=80,column=5,sticky='s')'''
    

def Search(hos):
    col, xc = extract(hos.name + '.txt', 0)
    # print(col,xc)
    search_win = Tk()
    Search_win = windows(search_win, 'PATIENT DETAILS')
    n = StringVar()
    Label(search_win, text='Choose UID ').grid(row=0, pady='50')
    choose3 = Combobox(search_win, width=45, textvariable=n)
    choose3['values'] = [i for i in col]
    choose3.grid(row=0, column=1)
    choose3.current()

    def search_data(event):
        for i in col:
            # print(i,n.get())
            if i == choose3.get():
                frame = Frame(search_win)
                frame.grid(row=5, column=5, rowspan=10)
                # print(details_list)
                for j in range(len(xc[col.index(i)])):
                    label_1 = Label(frame, text=pat[j], font=('calibre', 12, 'bold'), height='1')
                    label_2 = Label(frame, text=xc[col.index(i)][j], height='1', font=('times new roman', 12, 'normal'))
                    label_1.grid(row=j, column=0, sticky='w')
                    label_2.grid(row=j, column=1)
                break

    choose3.bind('<<ComboboxSelected>>', search_data)
    copyright_label = Label(search_win,text='© APASCAS',bg='#a1c4fd',fg='#dce7fa',font=('times new roman',12,'bold'))
    copyright_label.grid(row=30,column=5)


def LogIn():
      log_win = Tk()
      Log_win = windows(log_win, 'LOG IN', geo='320x200',bg='#FFDD3C')

      n = StringVar()
      label1 = Label(log_win, text='Choose hospital',bg='#FFDD3C')

      label1.grid(row=0, pady='50')
      
      choose2 = Combobox(log_win, width=20, textvariable=n)
      choose2['values'] = [i.name for i in hos_list]
      choose2.grid(row=0, column=1)
      choose2.current()

      #print('test', choose2.current())

      def menu(event):
            label2=Label(log_win, text='password',bg='#FFDD3C')
            label2.grid(row=1, column=0)
            passkey = Entry(log_win, show='*')
            passkey.grid(row=1, column=1)
            hos = hos_list[choose2.current()]
            def checker(hos):
                  hos = hos_list[choose2.current()]
                  if hos.password == passkey.get():
                        a = partial(crt, hos)
                        b = partial(Search, hos)
                        details_list = hos.get()
                        choose2.destroy()
                        label2.destroy()
                        label1.destroy()
                        passkey.destroy()
                        button6.destroy()
                        log_win.geometry('320x150')
                        log_win.title(hos.name.title())
                        #log_win.geometry('200x200')
                      # global a
                        def on3(e):
                              button3['background'] = '#667eea'
                        def off3(e):
                              button3['background'] = 'white'
                        def on5(e):
                            button5['background'] = '#667eea'
                            
                        def off5(e):
                            button5['background'] = 'white'
                            

                        button3 = Button(log_win, text='ADD PATIENT', command=a,width=25)
                        button3.bind('<Enter>', on3)
                        button3.bind('<Leave>', off3)
                        button3.grid(row=50,column=1,padx=(30,0),pady=(10,20))
                        button5 = Button(log_win, text='SEARCH PATIENT', command=b,width=25)
                        button5.bind('<Enter>', on5)
                        button5.bind('<Leave>', off5)
                        button5.grid(row=60,column=1,padx=(30,0),pady=(0,20))
                  else:
                        mb.showerror('Login error', 'The password you entered is incorrect')
            def n3(e):
                  button6['background'] = '#667eea'
                  button6.config(relief = 'sunken')
            def f3(e):
                  button6['background'] = 'white'
                  button6.config(relief = 'raised')

            c=partial(checker,hos)
            button6 = Button(log_win, text='LOGIN', command=c, relief='raised',width=15)
            button6.bind('<Enter>', n3)
            button6.bind('<Leave>', f3)
            button6.grid(row=2, column=1)

      choose2.bind('<<ComboboxSelected>>', menu)
      def o3(e):
            q1['background'] = '#667eea'
      def o4(e):
            q1['background'] = 'white'
      q1 = Button(log_win, text='QUIT', command=log_win.destroy,width=10)
      q1.bind('<Enter>', o3)
      q1.bind('<Leave>', o4)
      q1.grid(row=70,column=2,sticky='e')
      '''copyright_label = Label(log_win,text='© APASCAS',bg='#FFDD3C',fg='#dce7fa',font=('times new roman',12,'bold'))
      copyright_label.grid(row=80,column=2)'''

def SAVE():
      f = open('hos_list.txt', 'w')
      for hos in hos_list:
        details_list = hos.get()
        final_list = [str(item) for item in details_list]
        f.write(','.join(final_list) + '\n')
      f.close()
      msg=Tk()
      Msg=windows(msg,'SAVED!!',geo='400x100')
      Label(msg,text= 'YOUR DETAILS WERE SUCCESSFULLY SAVED').pack()
      msg.after(200,msg.destroy)


def AUTO():
      def counter():
            SAVE()
            main.after(30000,counter)
      counter()

def Statistics():

  def table(frame):
    df4=df
    i=0
    label_1 = Label(frame, text='Location    ', font=('calibre', 11, 'bold'))
    label_2 = Label(frame, text='Confirmed    ' , font=('calibre', 11, 'bold'))
    label_3 = Label(frame, text='Cases per 1M people    ', font=('calibre', 11, 'bold'))
    label_4 = Label(frame, text='Recovered   ', font=('calibre', 11, 'bold'))
    label_5 = Label(frame, text='Deaths  ', font=('calibre', 11, 'bold'))
    label_1.grid(row=i, column=0, sticky='w')
    label_2.grid(row=i, column=1)
    label_3.grid(row=i, column=2)
    label_4.grid(row=i, column=3)
    label_5.grid(row=i, column=4)
    i=1
    for ind in df4.index: 
        #print(df['Name'][ind], df['Stream'][ind]) 
        label_1 = Label(frame, text=df4['Location'][ind], font=('calibre', 10, 'bold'))
        label_2 = Label(frame, text=df4['Confirmed'][ind])
        label_3 = Label(frame, text=df4['Cases per 1M people'][ind])
        label_4 = Label(frame, text=df4['Recovered'][ind])
        label_5 = Label(frame, text=df4['Deaths'][ind])
        label_1.grid(row=i, column=0, sticky='w')
        label_2.grid(row=i, column=1)
        label_3.grid(row=i, column=2)
        label_4.grid(row=i, column=3)
        label_5.grid(row=i, column=4)
        i=i+1
    return
  def toptable():
      print (df1)

  def bargraph():
      df5=df1
      df5=df5.drop(columns=['Cases per 1M people'])
      root= tk.Tk()
    
      figure1 = plt.Figure(figsize=(16,15), dpi=100)
      ax1 = figure1.add_subplot(121)
      bar1 = FigureCanvasTkAgg(figure1, root)
      bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
      #df1.plot(kind='bar', legend=True, ax=ax1)


      #toptable()
      #fig, ax = plt.subplots(figsize=(13,6))
      index = np.arange(6)
      bar_width = 0.25
      opacity = 0.8
      df5 = df5.groupby('Location').sum()
      #ax.get_legend().remove('')
      df5.plot(kind='bar', legend=True, ax=ax1)
      ax1.set_title('Country-wise Comparison Graph')
 # def lgraph():
      dfc=pd.read_csv('covid_19_india.csv')
      #fig, ax = plt.subplots(figsize=(13,6))
      #root= tk.Tk()

      #figure1 = plt.Figure(figsize=(6,5), dpi=100)
      ax2 = figure1.add_subplot(222)
      #bar1 = FigureCanvasTkAgg(figure1, root)

      dfc['Date']=pd.to_datetime(dfc['Date'], format='%d/%m/%y') 
      #print(dfc.dtypes)
      dfd=dfc.groupby("Date")["Confirmed"].sum()
      dfd.plot(kind='line', legend=True, ax=ax2,x='Time',y='Cases')
      ax2.set_title('Cases over time')
      #plt.xlabel('Time')
      #plt.ylabel('Population')
      #type(dfd)
      #plt.plot(dfd)
      #root.mainloop()

  stat_win=Tk()
  Stat_win=windows(stat_win, 'STATISTICS', geo='620x400')
  
  selected_option = StringVar()
  #choose_4 = Combobox(stat_win,width=45,textvariable=selected_option)
  #choose_4['values'] = ('Table','Graphs')
  frame = Frame(stat_win)
  frame.grid(row=5, column=5, rowspan=10)
  table(frame)
  bargraph()
  #choose_4.grid(row=0,column=1) 
  #choose_4.current()



  def showcase(event):
    index=choose_4.current()
    print ("CBIT=",index)
    frame = Frame(stat_win)
    frame.grid(row=5, column=5, rowspan=10)
    li=[table(frame),bargraph()]
    #label_2.grid(row=i, column=1)
    li[index]


    
  #choose_4.bind('<<ComboboxSelected>>',showcase)
# view_but = Button(view_win, text = 'VIEW').grid()
  def q0(e):
        q1['background'] = '#667eea'
  def q2(e):
        q1['background'] = 'white'
  q1 = Button(stat_win, text='QUIT', command=stat_win.destroy)
  q1.bind('<Enter>', q0)
  q1.bind('<Leave>', q2)  
def Credits():
    mb.showwarning('CREDITS','113-SRIPRANAV KUMAR M \n 84-Anish N \n 97-Sanan M \n 103-SAICHARAN K \n 82-Amith Reddy \n 114-Surya Pratap \n 83-Anant Sharma')
  
button1 = Button(frame_2,text='SIGN UP',font=('times new roman', 20 , 'bold'),relief = 'ridge', command=add_hospital)
button1.bind('<Enter>', on1)
button1.bind('<Leave>', off1)
button1.pack(side='left',fill='both',expand=True)

button2 = Button(frame_2,text='VIEW HOSPITAL',font=('times new roman', 20 , 'bold'),relief = 'ridge', command=view_hospital)
button2.bind('<Enter>', on2)
button2.bind('<Leave>', off2)
button2.pack(side='left',fill='both',expand=True)

button4 = Button(frame_1,text='Login',font=('times new roman',12,'bold') ,command=LogIn,height=2,width=7)
button4.bind('<Enter>', on4)
button4.bind('<Leave>', off4)
button4.pack(side='right',padx=(0,30))

button5 = Button(frame_2,text='    SAVE     ',font=('times new roman', 20, 'bold'),relief = 'ridge', command=SAVE)
button5.bind('<Enter>', on5)
button5.bind('<Leave>', off5)
button5.pack(side='left',fill='both',expand=True)

graph_button = Button(frame_1,text='LIVE Statistics',font=('times new roman',12,'bold'),command=Statistics ,height=2,width=12)
graph_button.bind('<Enter>', ong)
graph_button.bind('<Leave>', offg)
graph_button.pack(side='left',padx=(30,0))

Credits = Button(frame_1,text='Credits',font=('times new roman',12,'bold'),command=Credits ,height=2,width=7)
Credits.bind('<Enter>', onc)
Credits.bind('<Leave>', offc)
Credits.pack(side='top')

copyright_label = Label(frame_3,text='V. 1.5.2 © APASCAS',bg='#a1c4fd',fg='#dce7fa',font=('times new roman',12,'bold'))
copyright_label.pack(side='right')

AUTO()

change(precaution)
mainloop()


# In[ ]:




