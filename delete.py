from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


mypass = "root"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password="",database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "cust_issued" 
custTable = "cust" #Cust Table


def deleteCust():
    
    cid = custInfo1.get()
    
    deleteSql = "delete from "+custTable+" where cid = '"+cid+"'"
    deleteIssue = "delete from "+issueTable+" where cid = '"+cid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success',"Member Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Member ID")
    

    print(cid)

    custInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global custInfo1,custInfo2,custInfo3,custInfo4,Canvas1,con,cur,custTable,root
    
    root = Tk()
    root.title("COUNTY FLAIR")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#E30B5D")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="PEACHPUFF",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="DELETE MEMBER", bg='#FFBB00', fg='#E30B5D', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='#FFBB00')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Cust ID to Delete
    lb2 = Label(labelFrame,text="CUSTOMER ID : ", bg='#FFBB00', fg='#E30B5D')
    lb2.place(relx=0.05,rely=0.5)
        
    custInfo1 = Entry(labelFrame)
    custInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteCust)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
