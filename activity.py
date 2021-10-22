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
custTable = "cust"
    
#List To store all Member IDs
allCid = [] 

def issue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    cid = inf1.get()
    issuedto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    
    extractCid = "select cid from "+custTable
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
            messagebox.showinfo("Error","Member ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Member IDs")
    
    issueSql = "insert into "+issueTable+" values ('"+cid+"','"+issuedto+"')"
    show = "select * from "+issueTable
    
    updateStatus = "update "+custTable+" set status = 'active' where cid = '"+cid+"'"
    try:
        if cid in allCid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Member activated Successfully")
            root.destroy()
        else:
            allCid.clear()
            messagebox.showinfo('Message',"Member id inactive")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(cid)
    print(issuedto)
    
    allCid.clear()
    
def activity(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("COUNTY FLAIR")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#E30B5D")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="PEACHPUFF",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="MEMBER'S ACTIVITY", bg='#FFBB00', fg='#E30B5D', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='#FFBB00')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Member ID
    lb1 = Label(labelFrame,text="CUSTOMER ID : ", bg='#FFBB00', fg='#E30B5D')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="ACTIVITY: ", bg='#FFBB00', fg='#E30B5D')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Activate Button
    issueBtn = Button(root,text="Activate",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
