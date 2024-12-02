import tkinter as tk
import mysql.connector 
window = tk.Tk()
mainFrame = tk.Frame(window,bg="#333333")
mainFrame.pack(expand=1,fill="both")
window.state("zoomed")
try:
    window.iconbitmap(r"Pic\Login.ico")
except:
    pass
window.title("Login In")
#---------------------------------------------------------------------------------------------------------------------Connecting database
conn = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="Tv.py@2005",
    database = "Pythondb"
)
cur = conn.cursor()
#----------------------------------------------------------------------------------------------------------------------Global var
showstatus = 1
#---------------------------------------------------------------------------------------------------------------------Functions
def userFocus(e):
    if userNameEntry.get()=="Username":
        userNameEntry.delete(0,tk.END)
def userFocusOff(e):
    if userNameEntry.get().strip()=="":
        userNameEntry.insert(0,"Username")
def passFocus(e):
    if passwordEntry.get()=="Password":
        passwordEntry.delete(0,tk.END)
        passwordEntry["show"]="*"
        global showstatus
        showstatus = 0
def passFocusOff(e):
    if passwordEntry.get().strip()=="":
        passwordEntry.insert(0,"Password")
        passwordEntry["show"]=""
        global showstatus
        showstatus = 1
def Login():
    #To complete

    
    #First get userName and password entered
    #Check if both are not null or default
    #Use mysql to check if the user name and password are correct or not
        #Side not the database i have is meant for userid (still going with username idea) , can create a new databse for name (can give unique names)
    
    if 1:
        print(userNameEntry.get())
        print(passwordEntry.get())
        print("Access Granted")
    else : 
        print("FuckOff")
def showPassword(e=None):
    global showstatus
    if showstatus  and passwordEntry.get().strip()!="Password":
        passwordEntry["show"]="*"
        showstatus = 0
    else : 
        passwordEntry["show"]=""
        showstatus = 1
x = 0.35
y=0.17
#Adding Sign Up frame--------------------------------------------------------------------------------------------------
widgetFrame = tk.Frame(mainFrame,bg="#333333")
widgetFrame.place(relx=x,rely=y,relwidth=1-2*x,relheight=1-2*y)
#-----------------------------------------------------------------------------------------------------------------------Adding Widgets
title = tk.Label(widgetFrame,text="Sign Up",fg="#ff3399",font="Aerial 40",bg="#333333")
title.place(relx=0.2,rely=0.2,relheight=0.15,relwidth=0.6)
#User name -------------------------------------------------------------------------------------------------------------
userNameEntry = tk.Entry(widgetFrame,bg="#333333",fg="#ffffff",border=0,relief="flat",font="Aerial 15")
userNameEntry.insert(0,"Username")
userNameEntry.place(relx=0.275,rely=0.41,relwidth=0.575,relheight=0.05)
tk.Label(widgetFrame,text="\U0001F464",bg="#333333",fg="#ffffff",font="Aerial 15").place(relx=0.20,rely=0.4)
tk.Label(widgetFrame,border=1).place(relx=0.2,rely=0.46 , relwidth=0.575,relheight=0.005)
#Password --------------------------------------------------------------------------------------------------------------
tk.Label(widgetFrame,text="\U0001F512",bg="#333333",fg="#ffffff",font="Aerial 15").place(relx=0.2,rely=0.5)
passwordEntry = tk.Entry(widgetFrame,bg="#333333",fg="#ffffff",border=0,relief="flat",font="Aerial 15")
passwordEntry.place(relx=0.275,rely=0.51,relwidth=0.5,relheight=0.05)
passwordEntry.insert(0,"Password")
tk.Label(widgetFrame,border=1).place(relx=0.2,rely=0.57 , relwidth=0.575,relheight=0.005)
eye = tk.Button(widgetFrame,text="\U0001F441\u200D\U0001F5E8" , bg="#333333",fg="#ffffff",font="Aerial 15",border=0,relief="flat",command=showPassword,activebackground="#333333",activeforeground="#ffffff")
eye.place(relx=0.712,rely=0.507)
#Log in ----------------------------------------------------------------------------------------------------------------
Loginbtn = tk.Button(widgetFrame,text="Login",fg="#ffffff",font="Aerial 20",bg="#333333",border=0,relief="flat",cursor="hand2",command=Login,activebackground="#333333",activeforeground="#ffffff")
Loginbtn.place(relx=0.2,rely=0.6,relwidth=0.50)
#Forgot Password -------------------------------------------------------------------------------------------------------
forgotPasswordLabel = tk.Label(widgetFrame,text="  Forgot password?",fg="#ffffff",font="Aerial 10",background="#333333",cursor="hand2")
forgotPasswordLabel.place(rely=0.585,relx=0.53)

#Events-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------Username
userNameEntry.bind("<FocusIn>",userFocus)
userNameEntry.bind("<FocusOut>",userFocusOff)
#-----------------------------------------------Password
passwordEntry.bind("<FocusIn>",passFocus)
passwordEntry.bind("<FocusOut>",passFocusOff)
#-----------------------------------------------Eye----

window.mainloop()



#user unicode ---  "\U0001F464"
#Lock unicode ---  "\U0001F512"
#eye   ---  "\U0001F441\u200D\U0001F5E8"
#Things to do
        #Forget password link
        #Link Database
        #Add further layers
        #Add a cross line over eye