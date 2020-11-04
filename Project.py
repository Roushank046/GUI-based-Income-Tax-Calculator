from tkinter import*
from PIL import ImageTk, Image

class main:
    def __init__(self):
        self.root=Tk()
        self.root.title('Income Tax Calculator')
        self.root.geometry('700x700')
        self.root.config(bg='purple')
        self.a1= PanedWindow()
        self.a1.pack(side='bottom')
        #self.root.msg=Message(self.root,text='Income Tax Calculator')
        #self.root.msg.config(font=('callibri',16,'bold italic'))
        #self.root.msg.place(x=0,y=0)

    
        self.msg=Label(self.root, text='Income Tax Calculator',relief='sunken')
        self.msg.config(font=('callibri',25,'bold italic underline'))
        self.msg.place(x=160, y=10)

        self.msg=Label(self.root, text='2020-2021',relief='sunken')
        self.msg.config(font=('callibri',25,'bold italic underline'))
        self.msg.place(x=260, y=80)

        self.msg=Message(self.root,text='By using this calculator you can check the amount of income tax and education cess according to tax slabs of financial Year 2020-2021',width=710)
        self.msg.config(font=('callibri',16,'bold italic'))
        self.msg.place(x=12,y=550)

        self.l1=Label(self.root, text='Existing Users:',width=50)
        self.l1.place(x=160, y=170)
        self.b1=Button(self.root, text='Login',width=10,command=self.signin)
        self.b1.place(x=300, y=210)

        self.l2=Label(self.root, text='New Users:     ',width=50)
        self.l2.place(x=160, y=270)
        self.b2=Button(self.root, text='SignUp',width=10,command=self.signup)
        self.b2.place(x=300, y=310)

        self.load=Image.open('photo.png')
        self.photo=ImageTk.PhotoImage(self.load)
        self.login=Label(self.root,image=self.photo)
        self.login.place(x=180,y=350)
        

        mainloop()


    def signin(self):
        self.login=Toplevel()
        self.login.title('Login Page')
        self.login.geometry('700x700')
        self.login.config(bg='dark green')
        self.entry4=StringVar()
        
        self.login1=Label(self.login, text='Income Tax Calculator',relief='sunken')
        self.login1.config(font=('callibri',25,'bold italic underline'))
        self.login1.place(x=160, y=10)

        self.login1=Label(self.login, text='2020-2021',relief='sunken')
        self.login1.config(font=('callibri',25,'bold italic underline'))
        self.login1.place(x=260, y=60)

        self.msg1=Message(self.login,text='Sign In',width=500)
        self.msg1.config(font=('callibri',26,'bold italic'))
        self.msg1.place(x=280,y=150)

        self.c2=Label(self.login,text='Email Id: ')
        self.c2.config(font=('callibri',18,'bold italic underline'))
        self.c2.place(x=120,y=240)
        self.e1=Entry(self.login,width=60,bd=10)
        self.e1.place(x=260,y=240)

        self.c3=Label(self.login,text='Name:  ')
        self.c3.config(font=('callibri',18,'bold italic underline'))
        self.c3.place(x=120,y=290)
        self.e2=Entry(self.login,width=60,bd=10,textvariable=self.entry4)
        self.e2.place(x=260,y=290)

        self.c4=Label(self.login,text='Password: ')
        self.c4.config(font=('callibri',18,'bold italic underline'))
        self.c4.place(x=120,y=340)
        self.e3=Entry(self.login,width=60,bd=10,show="*")
        self.e3.place(x=260,y=340)

        self.b3=Button(self.login, text='Login',width=10,command=self.calculator)
        self.b3.place(x=300, y=450)

        self.load2=Image.open('photo.png')
        self.photo2=ImageTk.PhotoImage(self.load2)
        self.login2=Label(self.login,image=self.photo2)
        self.login2.place(x=180,y=500)
        
        mainloop()


    def signup(self):
        self.new=Toplevel()
        self.new.title('Register New User')
        self.new.geometry('700x700')
        self.new.config(bg='pink')
        self.entry4=StringVar()

        self.signup1=Label(self.new, text='Income Tax Calculator',relief='sunken')
        self.signup1.config(font=('callibri',25,'bold italic underline'))
        self.signup1.place(x=160, y=10)

        self.signup1=Label(self.new, text='2020-2021',relief='sunken')
        self.signup1.config(font=('callibri',25,'bold italic underline'))
        self.signup1.place(x=260, y=60)

        self.msg2=Message(self.new,text='Register New User',width=500)
        self.msg2.config(font=('callibri',26,'bold italic'))
        self.msg2.place(x=180,y=150)

        self.c5=Label(self.new,text='Email Id: ')
        self.c5.config(font=('callibri',18,'bold italic underline'))
        self.c5.place(x=120,y=290)
        self.e4=Entry(self.new,width=60,bd=10)
        self.e4.place(x=260,y=290)

        self.c6=Label(self.new,text='Name:  ')
        self.c6.config(font=('callibri',18,'bold italic underline'))
        self.c6.place(x=120,y=240)
        self.e5=Entry(self.new,width=60,bd=10,textvariable=self.entry4)
        self.e5.place(x=260,y=240)

        self.c7=Label(self.new,text='Password: ')
        self.c7.config(font=('callibri',18,'bold italic underline'))
        self.c7.place(x=120,y=340)
        self.e6=Entry(self.new,width=60,bd=10,show="*")
        self.e6.place(x=260,y=340)

        self.c8=Label(self.new,text='Phone No')
        self.c8.config(font=('callibri',18,'bold italic underline'))
        self.c8.place(x=120,y=390)
        self.e7=Entry(self.new,width=60,bd=10)
        self.e7.place(x=260,y=390)


        self.c9=Label(self.new,text='Gender:  ')
        self.c9.config(font=('callibri',18,'bold italic underline'))
        self.c9.place(x=120,y=440)
        self.v1=IntVar()
        self.r1=Radiobutton(self.new,text="Male",variable=self.v1,value=1,bd=8,relief='raised')
        self.r1.place(x=275,y=440)
        self.r2=Radiobutton(self.new,text="Female",variable=self.v1,value=2,bd=8,relief='raised')
        self.r2.place(x=355,y=440)

        self.b4=Button(self.new, text='SignUp',width=10,relief='groove',bd=8,command=self.calculator)
        self.b4.place(x=300, y=550)

        mainloop()
        
        

    def calculator(self):
        self.calci=Toplevel()
        self.calci.title('Calculator')
        self.calci.geometry('700x700')
        self.calci.config(bg='blue')

        self.entry1=IntVar()
        self.entry2=IntVar()
        self.entry3=IntVar()

        self.c10=Label(self.calci, text='Income Tax Calculator',relief='sunken')
        self.c10.config(font=('callibri',25,'bold italic underline'))
        self.c10.place(x=160, y=10)

        self.c100=Label(self.calci, text='2020-2021',relief='sunken')
        self.c100.config(font=('callibri',25,'bold italic underline'))
        self.c100.place(x=260, y=60)


        self.c11=Label(self.calci, text='Please Input the Details to calculate Tax Amount',relief='sunken')
        self.c11.config(font=('callibri',20,'bold underline'))
        self.c11.place(x=20, y=130)

        self.c12=Label(self.calci,text='Total Yearly Income:')
        self.c12.config(font=('callibri',18,'bold italic underline'))
        self.c12.place(x=120,y=220)
        self.e8=Entry(self.calci,width=30,bd=10,textvariable=self.entry1)
        self.e8.place(x=380,y=220)

        self.c13=Label(self.calci,text='Gender:  ')
        self.c13.config(font=('callibri',18,'bold italic underline'))
        self.c13.place(x=220,y=280)
        self.v11=IntVar()
        self.r5=Radiobutton(self.calci,text="Male",variable=self.v11,value=1,bd=8,relief='raised')
        self.r5.place(x=375,y=280)
        self.r6=Radiobutton(self.calci,text="Female",variable=self.v11,value=2,bd=8,relief='raised')
        self.r6.place(x=455,y=280)

        self.c14=Label(self.calci,text='Age:')
        self.c14.config(font=('callibri',18,'bold italic underline'))
        self.c14.place(x=260,y=340)
        self.e9=Entry(self.calci,width=10,bd=10,textvariable=self.entry2)
        self.e9.place(x=380,y=340)

        self.c15=Label(self.calci,text='Senior Citizen:  ')
        self.c15.config(font=('callibri',18,'bold italic underline'))
        self.c15.place(x=160,y=400)
        self.v12=IntVar()
        self.r7=Radiobutton(self.calci,text="Yes",variable=self.v12,value=1,bd=8,relief='raised')
        self.r7.place(x=375,y=400)
        self.r8=Radiobutton(self.calci,text="No",variable=self.v12,value=2,bd=8,relief='raised')
        self.r8.place(x=455,y=400)

        self.b5=Button(self.calci, text='Calculate Tax',width=20,relief='groove',bd=8,command=self.calculation)
        self.b5.place(x=180, y=500)

        self.b6=Button(self.calci, text='Check Tax Rates',width=20,relief='groove',bd=8,command=self.rates)
        self.b6.place(x=360, y=500)


    def rates(self):
        self.tax=Toplevel()
        self.tax.title('Tax Rates')
        self.tax.geometry('700x700')
        self.tax.config(bg='purple')
        
        self.loads=Image.open('rate.jpg')
        self.loads=self.loads.resize((650,650),Image.ANTIALIAS)
        self.photos=ImageTk.PhotoImage(self.loads)
        self.login5=Label(self.tax,image=self.photos)
        self.login5.place(x=0,y=0)

        mainloop()

    def calculation(self):
        tax=0
        cess=0
        self.final=Toplevel()
        self.final.title('Result')
        self.final.geometry('700x700')
        self.final.config(bg='green')

        self.msg12=Label(self.final, text='Income Tax Calculator',relief='sunken')
        self.msg12.config(font=('callibri',25,'bold italic underline'))
        self.msg12.place(x=160, y=10)

        self.msg13=Label(self.final, text='2020-2021',relief='sunken')
        self.msg13.config(font=('callibri',25,'bold italic underline'))
        self.msg13.place(x=260, y=80)

        if(int(self.entry2.get())<60):
            if(int(self.entry1.get())<=250000):
                tax=0
            elif((int(self.entry1.get())>250000) and (int(self.entry1.get())<=500000)):
                
                tax=((int(self.entry1.get()) - 250000)* 0.05)
            elif((int(self.entry1.get())>500000) and (int(self.entry1.get())<=1000000)):
                tax=12500+((int(self.entry1.get()) - 500000)* 0.20)
            elif(int(self.entry1.get())>1000000):
                tax=112500+((int(self.entry1.get()) - 1000000)* 0.30)
                 
            
            
            
        elif(int(self.entry2.get())>=60) and (int(self.entry2.get())<80):
            if(int(self.entry1.get())<=300000):
                tax=0
            elif((int(self.entry1.get())>300000) and (int(self.entry1.get())<=500000)):
                tax=((int(self.entry1.get()) - 300000)* 0.05)
            elif((int(self.entry1.get())>500000) and (int(self.entry1.get())<=1000000)):
                tax=10000+((int(self.entry1.get()) - 500000)* 0.20)
            elif(int(self.entry1.get())>1000000):
                tax=110000+((int(self.entry1.get()) - 1000000)* 0.30)

                
        elif(int(self.entry2.get())>=80):
            if(int(self.entry1.get())<=500000):
                tax=0
            elif((int(self.entry1.get())>500000) and (int(self.entry1.get())<=1000000)):
                tax=((int(self.entry1.get()) - 500000)* 0.20)
            elif(int(self.entry1.get())>1000000):
                tax=100000+((int(self.entry1.get()) - 1000000)* 0.30)

    
        cess=tax*0.04
        total=tax+cess
        print(tax)
        print(self.entry4.get())

        self.msg12=Message(self.final,text='Hello  '+str(self.entry4.get()),width=710)
        self.msg12.config(font=('callibri',16,'bold italic'))
        self.msg12.place(x=120,y=200)

        self.msg11=Message(self.final,text='Net Income Tax:'+str(tax),width=710)
        self.msg11.config(font=('callibri',16,'bold italic'))
        self.msg11.place(x=120,y=250)

        self.msg13=Message(self.final,text='Net Education and Health Cess:'+str(cess),width=710)
        self.msg13.config(font=('callibri',16,'bold italic'))
        self.msg13.place(x=120,y=300)

        self.msg14=Message(self.final,text='Total Tax Amount:'+str(total),width=710)
        self.msg14.config(font=('callibri',16,'bold italic'))
        self.msg14.place(x=120,y=350)

        self.msg15=Message(self.final,text='Thank You For Using Our Calculator. Visit Again',width=710)
        self.msg15.config(font=('callibri',16,'bold italic'))
        self.msg15.place(x=20,y=450)

        self.b7=Button(self.final, text='Calculate Again',width=20,relief='groove',bd=8,command=self.calculator)
        self.b7.place(x=250, y=550)


        

        







        
        
        


        
Roushan=main()

        
