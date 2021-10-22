from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from member import *
from delete import *
from view import *
from activity import *
from Exit import *

mypass = "root"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password="",database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("COUNTY FLAIR CLUB")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=0.25

# Adding a background image
background_image =Image.open("lib.png")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFDAB9",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n COUNTY FlAIR ", bg='#A80000', fg='PEACHPUFF', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="ADD MEMBER DETAILS",bg='#A80000', fg='PEACHPUFF', command=member)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="DELETE MEMBER",bg='#A80000', fg='PEACHPUFF', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="VIEW MEMBER'S LIST",bg='#A80000', fg='PEACHPUFF', command=view)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="MEMBER ACTIVITY",bg='#A80000', fg='PEACHPUFF', command=activity)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="EXIT ACTIVITY",bg='#A80000', fg='PEACHPUFF', command = Exit)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()
