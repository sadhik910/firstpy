import datetime
from datetime import datetime,timedelta
import tkinter as tk
from PIL import Image,ImageTk

# window creation
window = tk.Tk()
window.geometry("400x350")
window.title("Age Calculator App")

# labels
name = tk.Label(text="Name")
name.grid(column=0,row=1)
year = tk.Label(text="Year")
year.grid(column=0,row=2)
month = tk.Label(text="Month")
month.grid(column=0,row=3)
date = tk.Label(text="Day")
date.grid(column=0,row=4)

# entery fields
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)

# geting user inputs
def getInput():
    name = nameEntry.get()
    monkey = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    textArea = tk.Text(master=window,height=1.5,width=40)
    textArea.grid(column=1,row=6)
    answer = "Heyy {monkey}!!!. You are {age} years old!!! ".format(monkey=name,age=monkey.age())
    textArea.insert(tk.END,answer)

# submit button
button = tk.Button(window,text="Calculate Age",command=getInput,bg="blue")
button.grid(column=1,row=6)

# date calculating class 
class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        # age = datetime.today() - self.birthdate
        return age

# image
image = Image.open('age.png')
image.thumbnail((300,800),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1,row=0)

window.mainloop()