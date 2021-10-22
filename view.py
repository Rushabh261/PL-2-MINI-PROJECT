from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


mypass = "root"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password="",database=mydatabase)
cur = con.cursor()

# Enter Table Names here
custTable = "cust" 
    
def view(): 
    
    root = Tk()
    root.title("COUNTY FLAIR")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#E30B5D")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="PEACHPUFF",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="VIEW", bg='#FFBB00', fg='#E30B5D', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='#FFBB00')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-30s%-20s%-20s%-30s"%('CUSTOMER ID','NAME','CONTACT NUMBER','STATUS'),bg='#FFBB00',fg='#E30B5D').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",bg='#FFBB00',fg='#E30B5D').place(relx=0.05,rely=0.2)
    getCust = "select * from "+custTable
    try:
        cur.execute(getCust)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
