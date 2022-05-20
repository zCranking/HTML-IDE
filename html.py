from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
from tkinter import filedialog
import webbrowser
root = Tk()
root.minsize(650, 650)
root.maxsize(650,650)
exitImg = ImageTk.PhotoImage(Image.open("exit.jpg"))
openImg = ImageTk.PhotoImage(Image.open("open.png"))
saveImg = ImageTk.PhotoImage(Image.open("save.png"))
runImg = ImageTk.PhotoImage(Image.open("run.jpg"))

label_file_name = Label(root, text="File Name" , foreground="#FFC43D", font=("Comic Sans MS", "10", "bold"))
label_file_name.place(relx=0.28, rely=0.03, anchor=CENTER)

input_file_name = Entry(root, foreground="#FFC43D", font=("Comic Sans MS", "10", "bold"))
input_file_name.place(relx = 0.46, rely=0.03, anchor=CENTER)

my_text = Text(root, height=32, width = 80, foreground="#FFC43D", font=("Comic Sans MS", "10", "bold"))
my_text.place(relx=0.5, rely=0.55, anchor=CENTER)

name = ""
name1 = ""

def openfile():
    global name
    global name1
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    html_file = filedialog.askopenfilename(title = "hacking your html file",
                                           filetypes =(("html files", "*    ),))
    
    print(html_file)
    name = os.path.basename(html_file)
    name1 = os.path.abspath(html_file)
    formatted_name = name.split('.')[0]
    input_file_name.insert(END, formatted_name)
    root.title(formatted_name)
    html_file = open(html_file, 'r')
    paragraph = html_file.read()
    my_text.insert(END, paragraph)
    html_file.close

def save():
    file_name = input_file_name.get()
    print(file_name)
    html_file = open(file_name+".txt", 'w')
    data = my_text.get(1.0, END)
    print(data)
    html_file.write(data)
    messagebox.showinfo("Update", "Your work was saved succesfully!")

def close():
    close = messagebox.askquestion("Close", "Do you want to close the file?")
    if close == "yes":
        savework = messagebox.askquestion("Save", "Did you save your work?")
        print(savework)
        if savework == "yes":
            root.destroy()
        else:
            savethework = messagebox.askquestion("Save", "Do you want to save your work?")
        if savethework == "yes":
            save()
            root.destroy()
        else:
            root.destroy()

def run():
    global name1
    print(name1)
    webbrowser.open(name1)

open_button = Button(root, image=openImg, command=openfile)
open_button.place(relx=0.10, rely=0.03, anchor=CENTER)
exit_button = Button(root, image=exitImg, command=close)
exit_button.place(relx=0.20, rely=0.03, anchor=CENTER)
save_button = Button(root, image=saveImg, command=save)
save_button.place(relx=0.15, rely=0.03, anchor=CENTER)
run_button = Button(root, image=runImg, command=run)
run_button.place(relx=0.05, rely=0.03, anchor=CENTER)

root.mainloop()