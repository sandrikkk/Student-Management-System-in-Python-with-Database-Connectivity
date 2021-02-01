from tkinter import *
from tkinter import ttk,messagebox
import pymysql
import os

class Students:
    def __init__(self,root):
        self.root=root
        self.root.title('Student Management System')
        self.root.geometry('1350x720+0+0')
        title=Label(self.root,text='Student Management System',font=('times new rommon',30,'bold'
            ),bg='yellow',fg='red',bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)
#====================Variable=======================
        self.s_id = StringVar()
        self.f_name = StringVar()
        self.s_name = StringVar()
        self.c_code = StringVar()
        self.exam_no = StringVar()
        self.t_score = StringVar()
        self.average = StringVar()
        self.ranking = StringVar()

        self.math = IntVar()
        self.hindi = IntVar()
        self.english = IntVar()
        self.physics = IntVar()
        self.python = IntVar()
        self.computing = IntVar()
        self.business = IntVar()
        self.biology = IntVar()
#===============================Frame=================
        F1=Frame(self.root,bg='#00ffff',relief=RIDGE,bd=4)
        F1.place(x=10,y=65,width=900,height=370)

        F2 = Frame(self.root, relief=RIDGE, bd=4)
        F2.place(x=920, y=65, width=420, height=370)

        F3=Frame(self.root,relief=RIDGE,bd=4)
        F3.place(x=10,y=440,width=1330,height=190)

        F4 = Frame(self.root, bg='#00ffff', relief=RIDGE, bd=4)
        F4.place(x=10, y=635, width=1330, height=80)

        #===================Student details=====================
        lbl_id=Label(F1,text='Student ID',bg='#00ffff',font=('times new rommon',18,'bold'))
        lbl_id.grid(row=0,column=0,padx=20,pady=5,sticky='w')
        txt_id=Entry(F1,font=('times new rommon',15,'bold'),bd=5,relief=GROOVE,textvariable=self.s_id)
        txt_id.grid(row=0,column=1,pady=5)

        lbl_fn = Label(F1, text='First Name:', bg='#00ffff', fg='black', font=('times new romon', 18, 'bold'), )
        lbl_fn.grid(row=1, column=0, padx=20, pady=5, sticky='w')
        txt_fn = Entry(F1, font=('times new romon', 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.f_name)
        txt_fn.grid(row=1, column=1, pady=5, sticky='w')

        lbl_s = Label(F1, text="Surname:", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_s.grid(row=2, column=0, pady=5, padx=20, sticky="w")
        txt_s = Entry(F1, font=("times new rommon", 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.s_name)
        txt_s.grid(row=2, column=1, pady=5, sticky="w")

        lbl_cc = Label(F1, text="Course Code:", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_cc.grid(row=3, column=0, pady=5, padx=20, sticky="w")

        combo_cc=ttk.Combobox(F1,font=("times new rommon", 15, 'bold'),state='readonly',width=18,textvariable=self.c_code)
        combo_cc['values']=('CC1255','CC1256','CC1257','CC1258','CC1259')
        combo_cc.grid(row=3,column=1,pady=5,sticky='w')

        lbl_en = Label(F1, text="Exam No.", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_en.grid(row=4, column=0, pady=5, padx=20, sticky="w")
        txt_en = Entry(F1, font=("times new rommon", 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.exam_no)
        txt_en.grid(row=4, column=1, pady=5, sticky="w")

        lbl_ts = Label(F1, text="Total Score :", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_ts.grid(row=5, column=0, pady=5, padx=20, sticky="w")
        txt_ts = Entry(F1, font=("times new rommon", 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.t_score,
                       state=DISABLED)
        txt_ts.grid(row=5, column=1, pady=5, sticky="w")

        lbl_avg = Label(F1, text="Percentage:", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_avg.grid(row=6, column=0, pady=5, padx=20, sticky="w")
        txt_avg = Entry(F1, font=("times new rommon", 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.average,
                        state=DISABLED)
        txt_avg.grid(row=6, column=1, pady=5, sticky="w")

        lbl_rank = Label(F1, text="Division:", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_rank.grid(row=7, column=0, pady=5, padx=20, sticky="w")
        txt_rank = Entry(F1, font=("times new rommon", 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.ranking,
                         state=DISABLED)
        txt_rank.grid(row=7, column=1, pady=5, sticky="w")

#=============================Subjects=========================
        lbl_m = Label(F1, text="Hindi", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_m.grid(row=0, column=2, pady=5, padx=40, sticky="w")
        txt_m = Entry(F1, font=("times new rommon", 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.hindi)
        txt_m.grid(row=0, column=3, pady=5, sticky="w")

        lbl_e = Label(F1, text="English", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_e.grid(row=1, column=2, pady=5, padx=40, sticky="w")
        txt_e = Entry(F1, font=("times new rommon", 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.english)
        txt_e.grid(row=1, column=3, pady=5, sticky="w")

        lbl_p = Label(F1, text="Python:", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_p.grid(row=2, column=2, pady=5, padx=40, sticky="w")
        txt_p = Entry(F1, font=("times new rommon", 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.python)
        txt_p.grid(row=2, column=3, pady=5, sticky="w")

        lbl_ph = Label(F1, text="Physics:", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_ph.grid(row=3, column=2, pady=5, padx=40, sticky="w")
        txt_ph = Entry(F1, font=("times new rommon", 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.physics)
        txt_ph.grid(row=3, column=3, pady=5, sticky="w")

        lbl_c = Label(F1, text="Computing:", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_c.grid(row=4, column=2, pady=5, padx=40, sticky="w")
        txt_c = Entry(F1, font=("times new rommon", 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.computing)
        txt_c.grid(row=4, column=3, pady=5, sticky="w")

        lbl_m = Label(F1, text="Maths:", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_m.grid(row=5, column=2, pady=5, padx=40, sticky="w")
        txt_m = Entry(F1, font=("times new rommon", 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.math)
        txt_m.grid(row=5, column=3, pady=5, sticky="w")

        lbl_b = Label(F1, text="Biology:", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_b.grid(row=6, column=2, pady=5, padx=40, sticky="w")
        txt_b = Entry(F1, font=("times new rommon", 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.biology)
        txt_b.grid(row=6, column=3, pady=5, sticky="w")

        lbl_B = Label(F1, text="Business", bg='#00ffff', fg='black', font=("times new romman", 18, 'bold'))
        lbl_B.grid(row=7, column=2, pady=5, padx=40, sticky="w")
        txt_B = Entry(F1, font=("times new rommon", 15, 'bold'), bd=5, relief=GROOVE,textvariable=self.business)
        txt_B.grid(row=7, column=3, pady=5, sticky="w")

#=====================Taxtarea==========================
        lbl_t=Label(F2,text='Student Results',font='arial 15 bold',fg='black',relief=GROOVE,bd=7)
        lbl_t.pack(side=TOP,fill=X)

        scrol=Scrollbar(F2,orient=VERTICAL)
        scrol.pack(side=RIGHT,fill=Y)
        self.textarea=Text(F2,font='arial 15',yscrollcommand=scrol.set)
        self.textarea.pack(fill=BOTH)
        scrol.config(command=self.textarea.yview)

#=================================table===================

        yscrol=Scrollbar(F3,orient=VERTICAL)
        self.student_table = ttk.Treeview(F3, columns=('student id', 'course code', 'hindi'
            , 'english', 'python', 'physics', 'computer', 'math', 'biology',
        'business', 'total score','percentage', 'division'),yscrollcommand=yscrol.set)
        yscrol.pack(side=RIGHT,fill=Y)
        yscrol.config(command=self.student_table.yview)

        self.student_table.heading('student id',text='Student ID')
        self.student_table.heading('course code',text='Course Code')
        self.student_table.heading("hindi", text="Hindi")
        self.student_table.heading("english", text="English")
        self.student_table.heading("python", text="Python")
        self.student_table.heading("physics", text="Physics")
        self.student_table.heading("computer", text="Computer")
        self.student_table.heading("math", text="Maths")
        self.student_table.heading("biology", text="Biology")
        self.student_table.heading("business", text="Business")
        self.student_table.heading("total score", text="Total Score")
        self.student_table.heading("percentage", text="Percentage")
        self.student_table.heading("division", text="Division")
        self.student_table['show'] = 'headings'

        self.student_table.column('student id',width=100)
        self.student_table.column("course code", width=100)
        self.student_table.column("hindi", width=100)
        self.student_table.column("english", width=100)
        self.student_table.column("python", width=100)
        self.student_table.column("physics", width=100)
        self.student_table.column("computer", width=100)
        self.student_table.column("math", width=100)
        self.student_table.column("biology", width=100)
        self.student_table.column("business", width=100)
        self.student_table.column("total score", width=100)
        self.student_table.column("percentage", width=100)
        self.student_table.column("division", width=100)
        self.student_table.pack()
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()

#=================================Buttons==============================
        btn1=Button(F4,text='Student Result',font='arial 20 bold',fg='crimson',bg='yellow',width=12,command=self.add)
        btn1.grid(row=0,column=0,padx=15,pady=5)

        btn2 = Button(F4, text='Transcript', font='arial 20 bold', fg='crimson', bg='yellow',width=12,command=self.result)
        btn2.grid(row=0, column=1, padx=15, pady=5)

        btn3 = Button(F4, text='Print', font='arial 20 bold', bg='yellow', fg='crimson',width=10,command=self.print)
        btn3.grid(row=0, column=3, padx=15, pady=5)

        btn4 = Button(F4, text='Delete', font='arial 20 bold', bg='yellow', fg='crimson',width=10,command=self.delete)
        btn4.grid(row=0, column=4, padx=15, pady=5)

        btn5 = Button(F4, text='Reset', font='arial 20 bold', bg='yellow', fg='crimson',width=10,command=self.reset)
        btn5.grid(row=0, column=5, padx=15, pady=5)

        btn6 = Button(F4, text='Exit', font='arial 20 bold', bg='yellow', fg='crimson',width=10,command=self.exit)
        btn6.grid(row=0, column=6, padx=15, pady=5)

#=====================Fuctions======================
    def total(self):
        t=(self.hindi.get()+
           self.english.get()+
           self.python.get()+
           self.physics.get()+
           self.computing.get()+
           self.math.get()+
           self.biology.get()+
           self.business.get())
        p=t/8
        self.t_score.set(str(t))
        self.average.set(str(p)+'%')
        if p>=60:
            self.ranking.set('Ist')
        elif p>=45:
            self.ranking.set('IInd')
        elif p>33:
            self.ranking.set('IIIrd')
        else:
            self.ranking.set('Fail')


    def add(self):
        if self.s_id.get() == '' or self.f_name.get() == '' or self.s_name.get() == '' or self.c_code.get() == '' or self.exam_no.get() == '':
            messagebox.showerror('Error','Student details are must')
        else:

            self.total()
            con=pymysql.connect(host='localhost',user='root',password='',database='st')
            cur=con.cursor()
            cur.execute("Select * from student_record")
            rows=cur.fetchall()
            for row in rows:
                if row[0]==self.s_id.get():
                    messagebox.showerror('Error','Duplicate entry not allowed')
                    return
            cur.execute("Insert into student_record values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.s_id.get(),
                        self.c_code.get(),
                        self.hindi.get(),
                        self.english.get(),
                        self.python.get(),
                        self.physics.get(),
                        self.computing.get(),
                        self.math.get(),
                        self.biology.get(),
                        self.business.get(),
                        self.t_score.get(),
                        self.average.get(),
                        self.ranking.get(),
                        self.f_name.get(),
                        self.s_name.get(),
                        self.exam_no.get())

            )
            con.commit()
            self.fatch_data()
            con.close()

    def fatch_data(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='st')
        cur = con.cursor()
        cur.execute("Select * from student_record")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def result(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, '\n************************************************')
        self.textarea.insert(END, '\n================================')
        self.textarea.insert(END, f'\nStudent ID:\t\t{self.s_id.get()}')
        self.textarea.insert(END, '\n================================')
        self.textarea.insert(END, f'\n\nFull Name:\t\t{self.f_name.get()} {self.s_name.get()}')
        self.textarea.insert(END, f'\nCourse Code:\t\t{self.c_code.get()}')
        self.textarea.insert(END, f'\nExam No: \t\t{self.exam_no.get()}')
        self.textarea.insert(END, f'\nHindi:   \t\t{self.hindi.get()}')
        self.textarea.insert(END, f'\nEnglish: \t\t{self.english.get()}')
        self.textarea.insert(END, f'\nPython:  \t\t{self.python.get()}')
        self.textarea.insert(END, f'\nPhysics: \t\t{self.physics.get()}')
        self.textarea.insert(END, f'\nComputer:\t\t{self.computing.get()}')
        self.textarea.insert(END, f'\nMaths:   \t\t{self.math.get()}')
        self.textarea.insert(END, f'\nBiology: \t\t{self.biology.get()}')
        self.textarea.insert(END, f'\nBusiness:\t\t{self.business.get()}')
        self.textarea.insert(END, '\n\n================================')
        self.textarea.insert(END, f'\nTotal Score:\t\t{self.t_score.get()}')
        self.textarea.insert(END, f'\nPercentage:\t\t{self.average.get()}')
        self.textarea.insert(END, f'\nDivision:\t\t{self.ranking.get()}')
        self.textarea.insert(END, '\n================================')

        self.textarea.insert(END, '\n\n************************************************')

    def print(self):
        q=self.textarea.get('1.0',END)
        if q!='':
            filename='C:\\Users\\acer\\PycharmProjects\\python Project in GUI\\Student Record\\'+(self.s_id.get())+'.txt'
            open(filename,'w').write(q)
            os.startfile(filename,'print')
        else:
            messagebox.showerror('Error','There is nothing tobe print')

    def delete(self):
        if self.s_id.get()=='':
            messagebox.showerror('Error','Please enter Student ID to delete the Record')
        else:
            con = pymysql.connect(host='localhost', user='root', password='', database='st')
            cur = con.cursor()
            cur.execute("delete from student_record where Student_ID=%s",self.s_id.get())
            con.commit()
            con.close()
            self.fatch_data()
            self.reset()

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']
        self.s_id.set(row[0])
        self.c_code.set(row[1])
        self.math.set(row[2])
        self.hindi.set(row[3])
        self.english.set(row[4])
        self.physics.set(row[5])
        self.python.set(row[6])
        self.computing.set(row[7])
        self.business.set(row[8])
        self.biology.set(row[9])
        self.t_score.set(row[10])
        self.average.set(row[11])
        self.ranking.set(row[12])
        self.f_name.set(row[13])
        self.s_name.set(row[14])
        self.exam_no.set(row[15])

    def reset(self):
        self.textarea.delete(1.0,END)
        self.s_id.set('')
        self.f_name.set('')
        self.s_name.set('')
        self.c_code.set('')
        self.exam_no.set('')
        self.t_score.set('')
        self.average.set('')
        self.ranking.set('')

        self.math.set(0)
        self.hindi.set(0)
        self.english.set(0)
        self.physics.set(0)
        self.python.set(0)
        self.computing.set(0)
        self.business.set(0)
        self.biology.set(0)


    def exit(self):
        if messagebox.askyesno('Exit','Do you want to exit ?'):
            root.destroy()
root=Tk()
ob=Students(root)
root.mainloop()