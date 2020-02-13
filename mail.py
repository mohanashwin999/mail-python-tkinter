from tkinter import *
import smtplib

mail=Tk()
mail.geometry('640x640+0+0')

sender=StringVar()
password=StringVar()
receiver=StringVar()
message=StringVar()

sender2=Label(mail,text='Sender').place(x=20,y=50)
password2=Label(mail,text='Password').place(x=20,y=90)
receiver2=Label(mail,text='Receiver').place(x=20,y=130)
message2=Label(mail,text='Message').place(x=20,y=170)


sender1=Entry(mail,textvariable=sender).place(x=130,y=50)
password1=Entry(mail,textvariable=password,show='*').place(x=130,y=90)
receiver1=Entry(mail,textvariable=receiver).place(x=130,y=130)
message1=Text(mail,width=20, height=10)
message1.place(x=130,y=170)

def event():
        s1=sender.get()
        p=password.get()
        r=receiver.get()
        m=message1.get(1.0,END)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(s1,p) 
        s.sendmail(s1,r,m) 
        s.quit()



B = Button(mail, text ='Submit', command = lambda : event()).place(x=70,y=400)

mail.mainloop()