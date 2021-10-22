from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def Custregister():

    cid = custInfo1.get()
    name = custInfo2.get()
    contact = custInfo3.get()
    status = custInfo4.get()
    status = status.lower()

    insertCust = "insert into "+custTable+" values('"+cid+"','"+name+"','"+contact+"','"+status+"')"
    try:
        cur.execute(insertCust)
        con.commit()
        messagebox.showinfo('Success',"Member added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(cid)
    print(name)
    print(contact)
    print(status)
   


    root.destroy()
    
def member(): 
    
    global custInfo1,custInfo2,custInfo3,custInfo4,Canvas1,con,cur,custTable,root
    
    root = Tk()
    root.title("COUNTY FLAIR")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

   
    mypass = "root"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password="",database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    custTable = "cust" # Cust Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#E30B5D")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="PEACHPUFF",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="MEMBER", bg='#FFBB00', fg='#E30B5D', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='#FFBB00')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # CUSTOMER ID
    lb1 = Label(labelFrame,text="CUSTOMER ID : ", bg='#FFBB00', fg='#E30B5D')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    custInfo1 = Entry(labelFrame)
    custInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # FULL NAME
    lb2 = Label(labelFrame,text="FULL NAME : ", bg='#FFBB00', fg='#E30B5D')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    custInfo2 = Entry(labelFrame)
    custInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # CONTACT NUMBER
    lb3 = Label(labelFrame,text="CONTACT NUMBER: ", bg='#FFBB00', fg='#E30B5D')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    custInfo3 = Entry(labelFrame)
    custInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    # MEMBER Status
    lb4 = Label(labelFrame,text="Status(active/inact) : ", bg='#FFBB00', fg='#E30B5D')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    custInfo4 = Entry(labelFrame)
    custInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

     #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=Custregister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
