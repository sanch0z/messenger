import tkinter as tk
from importlib.metadata import entry_points
from tkinter import Listbox
from tkinter.ttk import Button, Labelframe, Label, Entry

def send_message():
    pass

def on_contact_select():
    pass

def clear_chat():
    pass
root = tk.Tk()
root.title("Мессенджер")
root.geometry("600x600")



send_btn = tk.Button(root,text="Отправить")
chat = tk.Text(root,height=30,width=35)
contact_list = tk.Listbox(root,width=20,height=25)
contact_list.insert(tk.END,"Пользователь 1","Тони Старк")
contact_list.bind("<<ListboxSelect>>" , on_contact_select())
send_at_label = tk.Label(root,text="Выбирете пользователя")
entry = tk.Entry(root,width=40)
bottom_frame = tk.Frame(root)



#Разметка

chat.grid(row=0,column=1)
contact_list.grid(row = 0,column = 0)
bottom_frame.grid(row=1,column=1)
entry.pack()
send_btn.pack()
entry.focus()
root.grid












root.mainloop()