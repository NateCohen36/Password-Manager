import tkinter as tk
from tkinter import ttk
from passwords import Password
import json
class Application:


    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x500")
        self.window.title("Password Manager")

        self.lowercase = False
        self.capital = False
        self.symbol = False
        self.number = False

        self.checkVarLowercase = tk.BooleanVar()
        self.checkVarCapital = tk.BooleanVar()
        self.checkVarSymbol = tk.BooleanVar()
        self.checkVarNumber = tk.BooleanVar()

        self.hidden = False

        self.filepath = "PasswordGenerator/files/passwords.txt"

        self.createGUI()

        self.window.mainloop()


    def createGUI(self):
        #Title
        titleLabel = tk.Label(self.window, text = "Password Generator", font=("impact", 20, "bold"))
        titleLabel.pack()

        #Check Buttons
        self.chkLowercase = tk.Checkbutton(self.window, text="Lowercase Letters", width=17, height=1,font=("impact", 15, "bold"),  variable = self.checkVarLowercase)
        self.chkCapital = tk.Checkbutton(self.window, text="Capital Letters       ", width=17, height=1,font=("impact", 15, "bold"), variable = self.checkVarCapital)
        self.chkSymbol = tk.Checkbutton(self.window, text="Symbols                    ", width=17, height=1,font=("impact", 15, "bold"), variable = self.checkVarSymbol)
        self.chkNumber = tk.Checkbutton(self.window, text="Numbers                  ", width=17, height=1,font=("impact", 15, "bold"), variable = self.checkVarNumber)

        self.chkLowercase.place(x=25,y=100)
        self.chkCapital.place(x=25,y=150)
        self.chkSymbol.place(x=25,y=200)
        self.chkNumber.place(x=25,y=250)

        #Entrybox
        self.lengthLable = tk.Label(text = "Desired Length", font = ("Impact", 15, "bold"))
        self.lengthLable.place(x=36, y =290)

        self.lengthEntry = tk.Scale(self.window, from_=1, to=30, length=250, orient=tk.HORIZONTAL)
        self.lengthEntry.place(x=36,y=315)
    
        #Buttons
        self.btGenerate = tk.Button(self.window, text="Generate", width=17, height=1,font=("impact", 15, "bold"), command = self.generateCommand)
        self.btGenerate.place(x=36, y= 360)

        self.btHide = tk.Button(self.window, text="Hide Password", width=17, height=1,font=("impact", 15, "bold"), command = self.hidePassword)
        self.btHide.place(x=36, y= 400)

        self.btCopy = tk.Button(self.window, text="Copy", width=5, height=1,font=("impact", 10, "bold"), command = self.copyPaste)
        self.btCopy.place(x=662,y=120)

        self.btScramble = tk.Button(self.window, text="Scramble", width=17, height=1,font=("impact", 15, "bold"), command = self.scrambleCommand)
        self.btScramble.place(x=36,y=440)

        #Password Box
        self.passwordLabel = tk.Label(text = "Password", font = ("Impact", 15, "bold"))
        self.passwordLabel.place(x=360,y=160)
        
        self.passwordBox = tk.Entry(self.window)
        self.passwordBox.place(x=360,y=195, width=300)

        #Email Entry Box
        self.emailLabel = tk.Label(text = "Email/Username", font = ("Impact", 15, "bold"))
        self.emailLabel.place(x=360, y=100)

        self.emailEntry = tk.Entry(self.window)
        self.emailEntry.place(x=360, y=130, width = 300)


        #PasswordStrength
        self.strengthLabel = tk.Label(self.window, text = "Strength: ", font = ("Impact", 15, "bold"))
        self.strengthLabel.place(x=360, y=230)

        self.passwordStrength = ttk.Progressbar(self.window, length = 300, orient=tk.HORIZONTAL, max=101)
        self.passwordStrength.place(x=360,y=260)

        #Save Password
        self.btSave = tk.Button(self.window, text = "Save", font = ('Impact', 10, "bold"), command = self.savePassword)
        self.btSave.place(x=662, y=155)

        #Load Password
        self.btLoad = tk.Button(self.window, text = "Load", font = ("Impact", 10, "bold"), command = self.loadPassword)
        self.btLoad.place(x=662, y=190)

        #File Path
        self.filePathLabel = tk.Label(self.window, text = "File Path", font = ("Impact", 15, "bold"))
        self.filePathLabel.place(x=330, y = 280)

        self.filePathEntry = tk.Entry(width = 25)
        self.filePathEntry.place(x=330, y = 310)

        self.fileNameLabel = tk.Label(self.window, text = "File Name", font = ("Impact", 15, "bold"))
        self.fileNameLabel.place(x=550, y = 280)

        self.fileNameEntry = tk.Entry(width = 25)
        self.fileNameEntry.place(x=550, y= 310)

        
        #CreditLabels
        """
        self.creditLabel = tk.Label(text = "Password Generator v1.0.0 - Nathan Cohen", font = ("Impact", 10, "bold"))
        self.creditLabel.place(x=509, y = 480)
        """

        #Feedback Label
        self.feedbackLabel = tk.Label(self.window)
        self.feedbackLabel.place(x = 330, y = 340)


        #Logo
        """
        self.logo = tk.PhotoImage(file="PasswordGenerator/images/logo.png")
        self.logo = self.logo.subsample(2,2)
        self.logoLabel = tk.Label(self.window, image = self.logo)
        self.logoLabel.place(x=375,y=250)
        """
        


    def generateCommand(self):
        self.hidden = False
        self.passwordBox.delete(0, len(self.passwordBox.get()))
        self.password = Password.generatePassword(self.lengthEntry.get(), self.checkVarLowercase.get(), self.checkVarCapital.get(), self.checkVarSymbol.get(), self.checkVarNumber.get())
    
        self.passwordStrength['value'] = Password.calculatePasswordStrength(self.lengthEntry.get(), self.checkVarLowercase.get(), self.checkVarCapital.get(), self.checkVarSymbol.get(), self.checkVarNumber.get())
        self.passwordBox.insert(0, self.password)

        if self.passwordStrength['value'] <= 40:
            self.strengthLabel.config(text="Strength: Weak")
        elif self.passwordStrength['value'] > 40 and self.passwordStrength['value'] <= 60:
            self.strengthLabel.config(text="Strength: Okay")
        elif self.passwordStrength['value'] > 60 and self.passwordStrength['value'] <= 80:
            self.strengthLabel.config(text="Strength: Good")
        elif self.passwordStrength['value'] >80 and self.passwordStrength['value'] <= 99:
            self.strengthLabel.config(text="Strength: Strong")
        elif self.passwordStrength['value'] >99:
            self.strengthLabel.config(text="Strength: Perfect")


    
    def hidePassword(self):
        if self.hidden == False:
            hiddenText = "" 

            for i in range(len(self.password)):
                hiddenText += "*"

            self.passwordBox.delete(0, len(self.passwordBox.get()))
            self.passwordBox.insert(0,hiddenText)
            self.hidden = True
        else:
            self.hidden=False
            self.passwordBox.delete(0, len(self.passwordBox.get()))
            self.passwordBox.insert(0,self.password)
    
    def scrambleCommand(self):
        password = Password.scramblePassword(self.passwordBox.get())
        self.passwordBox.delete(0, len(self.passwordBox.get()))
        self.passwordBox.insert(0, password)

    def copyPaste(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.passwordBox.get())
        self.feedbackLabel.config(text="Password Copied To Clipboard", font = ("Impact", 15, "bold"), fg="green")

    def savePassword(self):
        password = self.passwordBox.get()
        encryptedPassword = Password.encryptPassword(password)
        email = self.emailEntry.get()
        filePath = self.filePathEntry.get() + self.fileNameEntry.get() + ".json"
        info = {
            "Email/Username": email,
            "Password": encryptedPassword
        }

        try:
            with open(filePath, "w") as file:
                json.dump(info, file)
                self.feedbackLabel.config(text=("Password successfly saved to " + filePath), font = ("Impact", 7, "bold"), fg="green")
        except FileExistsError:
            self.feedbackLabel.config(text="That File Already Exists", font = ("Impact", 15, "bold"), fg="red")
        except OSError:
            self.feedbackLabel.config(text="Invalid File Path", font = ("Impact", 15, "bold"), fg="red")
        

    def loadPassword(self):
        filePath = self.filePathEntry.get() + self.fileNameEntry.get() + ".json"
        try:
            with open(filePath, "r") as file:
                content = json.load(file)
                password = Password.decryptPassword(content["Password"])
                email = content["Email/Username"]
                self.passwordBox.delete(0, len(self.passwordBox.get()))
                self.passwordBox.insert(0, password)

                self.emailEntry.delete(0, len(self.emailEntry.get()))
                self.emailEntry.insert(0,email)
                self.feedbackLabel.config(text="Password Loaded Successfuly", font = ("Impact", 15, "bold"), fg="green")
        except FileNotFoundError:
            self.feedbackLabel.config(text="File Not Found", font = ("Impact", 15, "bold"), fg="red")
        except PermissionError:
            self.feedbackLabel.config(text="Permission Error", font = ("Impact", 15, "bold"), fg="red")

        


        


    

    



        

    








