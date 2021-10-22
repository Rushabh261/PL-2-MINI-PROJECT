from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "root"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password="",database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "cust_issued" #Issue Table
custTable = "cust" #Cust Table


allCid = [] #List To store all Cust IDs

def returnn():
    
    global SubmitBtn,labelFrame,lb1,custInfo1,quitBtn,root,Canvas1,status
    
    cid = custInfo1.get()

    extractCid = "select cid from "+issueTable
    try:
        cur.execute(extractCid)
        con.commit()
        for i in cur:
            allCid.append(i[0])
        
        if cid in allCid:
            checkAvail = "select status from "+custTable+" where cid = '"+cid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'active':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Customer ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Cust IDs")
    
    
    issueSql = "delete from "+issueTable+" where cid = '"+cid+"'"
  
    print(cid in allCid)
    print(status)
    updateStatus = "update "+custTable+" set status = 'active' where cid = '"+cid+"'"
    try:
        if cid in allCid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Cust Returned Successfully")
        else:
            allCid.clear()
            messagebox.showinfo('Message',"Please check the cust ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allCid.clear()
    root.destroy()
    
def Exit(): 
    
    global custInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("COUNTY FLAIR")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#E30B5D")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="PEACHPUFF",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="EXIT CLUB", bg='#FFBB00', fg='#E30B5D', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='#FFBB00')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Cust ID to Delete
    lb1 = Label(labelFrame,text="CUSTOMER ID : ", bg='#FFBB00', fg='#E30B5D')
    lb1.place(relx=0.05,rely=0.5)
        
    custInfo1 = Entry(labelFrame)
    custInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
