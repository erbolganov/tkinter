from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My App")
root.geometry("250x200")
def select():
    result = "Выбрано: "
    if python.get() == 'Yes': result = result + python_checkbutton.cget('text')
    if javascript.get() == 1: result = result + javascript_checkbutton.cget('text')
    if java.get() == 1: result = result + javascript_checkbutton.cget('text')
    languages.set(result)


position = {"padx": 6, "pady": 6, "anchor": NW}

languages = StringVar()
languages_label = ttk.Label(textvariable=languages)
languages_label.pack(**position)

python = IntVar()
python_checkbutton = ttk.Checkbutton(text="Python", variable=python, command=select)
python_checkbutton.pack(**position)

javascript = IntVar()
javascript_checkbutton = ttk.Checkbutton(text="JavaScript", variable=javascript, command=select)
javascript_checkbutton.pack(**position)

java = IntVar()
java_checkbutton = ttk.Checkbutton(text="Java", variable=java, command=select)
java_checkbutton.pack(**position)

root.mainloop()