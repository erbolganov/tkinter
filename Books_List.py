# from tkinter import *
# from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title("Book list")
root.geometry("1100x500+200+100")
root['bg'] = '#00FFFF'
def header(head):
    return tk.Label(text=head, font="Arial, 20")

def book_info(info):
    return tk.Label(text=info, font="Arial, 15")

def author_info(info):
    return tk.Label(text=info, font="Arial, 15")

def entery_book(info):
    return tk.Entry(font="Arial, 15")

def entery_author(info):
    return tk.Entry(font="Arial, 15")

def entery_renter(info):
    return tk.Entry(font="Arial, 15")

'''Label header'''
header("Book").grid(row=0, column=0, columnspan=2,)
header("Author").grid(row=0, column=3, columnspan=2)
header("Renter").grid(row=0, column=6, columnspan=2)

'''Label book_info'''
book_info("Name:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
book_info("Volume:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
book_info("Year:").grid(row=3, column=0, sticky='w', padx=5, pady=5)
book_info("Eddition:").grid(row=4, column=0, sticky='w', padx=5, pady=5)
book_info("Polygraph:").grid(row=5, column=0, sticky='w', padx=5, pady=5)

'''Label author_info'''
author_info("Name:").grid(row=1, column=3, sticky='w', padx=5, pady=5)
author_info("Surname:").grid(row=2, column=3, sticky='w', padx=5, pady=5)
author_info("Country:").grid(row=3, column=3, sticky='w', padx=5, pady=5)

'''Label renter_info'''
book_info("Name:").grid(row=1, column=5, sticky='w', padx=5, pady=5)
book_info("Surname:").grid(row=2, column=5, sticky='w', padx=5, pady=5)
book_info("Date").grid(row=3, column=5, sticky='w', padx=5, pady=5)
book_info("Phone:").grid(row=4, column=5, sticky='w', padx=5, pady=5)

'''Entery_book info'''
entery_book("").grid(row=1, column=1, sticky='ns', padx=5, pady=5)
entery_book("").grid(row=2, column=1, sticky='ns', padx=5, pady=5)
entery_book("").grid(row=3, column=1, sticky='ns', padx=5, pady=5)
entery_book("").grid(row=4, column=1, sticky='ns', padx=5, pady=5)
entery_book("").grid(row=5, column=1, sticky='ns', padx=5, pady=5)

'''Entery_author info'''
entery_author("").grid(row=1, column=4, sticky='ns', padx=5, pady=5)
entery_author("").grid(row=2, column=4, sticky='ns', padx=5, pady=5)
entery_author("").grid(row=3, column=4, sticky='ns', padx=5, pady=5)

'''Entery_renter info'''
entery_renter("").grid(row=1, column=6, sticky='ns', padx=5, pady=5)
entery_renter("").grid(row=2, column=6, sticky='ns', padx=5, pady=5)
entery_renter("").grid(row=3, column=6, sticky='ns', padx=5, pady=5)
entery_renter("").grid(row=4, column=6, sticky='ns', padx=5, pady=5)

'''Button save'''
btn = tk.Button(text='Save', bg='#1fff57', fg="#ebf2e6", font='Arial, 15')
btn.grid(row=6, column=6, columnspan=6, sticky='e')



root.mainloop()