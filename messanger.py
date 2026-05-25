import tkinter as tk
from tkinter.constants import NORMAL, DISABLED

from pyexpat.errors import messages


class MessangerApp:
    WINDOW_WIDHT = 600
    WINDOW_HEIGHT = 600
    def __init__(self,root):
        self.root = root
        self.root.title("Мессенджер")
        self.root.geometry(f"{self.WINDOW_WIDHT}x{self.WINDOW_HEIGHT}")
        # Виджеты
        self.left_frame = tk.Frame(self.root,width=150)
        self.left_frame.pack(side=tk.LEFT,fill=tk.Y,padx=5,pady=5)
        tk.Label(self.left_frame,text="Контакты",font="Arial").pack()
        # Список контактов
        self.contacts_listbox = tk.Listbox(self.left_frame,height=20,width=20)
        self.contacts_listbox.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        # Полоса прокрутки
        scroll_contacts = tk.Scrollbar(self.left_frame,orient=tk.VERTICAL,command=self.contacts_listbox.yview)
        scroll_contacts.pack(side=tk.RIGHT,fill = tk.Y)
        self.contacts_listbox.config(yscrollcommand=scroll_contacts.set)
        for contact in ["Sasha","Bob","Alice"]:
            self.contacts_listbox.insert(tk.END,contact)
        #Правая сторона
        self.right_frame = tk.Frame(self.root,bg="white")
        self.right_frame.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=5,pady=5)

        self.chat_area = tk.Text(self.right_frame,state=tk.DISABLED,wrap=tk.WORD)
        self.chat_area.pack(fill=tk.BOTH,expand=True)

        scroll_chat = tk.Scrollbar(self.right_frame,orient=tk.VERTICAL,command=self.chat_area.yview)
        scroll_chat.pack(side=tk.RIGHT,fill=tk.Y)
        self.chat_area.config(yscrollcommand=scroll_chat.set)

        input_frame = tk.Frame(self.right_frame)
        input_frame.pack(fill=tk.X)
        self.message_entry = tk.Entry(input_frame)
        self.message_entry.pack(side=tk.LEFT,fill=tk.X,expand=True)

        send_button = tk.Button(input_frame,text="Отправить",command=self.send_message)
        clear_button = tk.Button(input_frame,text="Очистить",command=self.clear_chat)
        send_button.pack(side=tk.RIGHT)
        clear_button.pack(side=tk.RIGHT)


        self.contacts_listbox.bind('<<ListboxSelect>>',self.on_contact_select)
        self.message_entry.bind('<Return>',lambda event: self.send_message())






    def send_message(self):
        message = self.message_entry.get().strip()
        if message:
            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.insert(tk.END,f"Я: {message}")
            self.chat_area.see(tk.END)
            self.chat_area.config(state=tk.DISABLED)
            self.message_entry.delete(0,tk.END)



    def on_contact_select(self):
        pass

    def clear_chat(self):
        self.chat_area.config(state=NORMAL)
        self.chat_area.delete(1.0,tk.END)
        self.chat_area.config(state=DISABLED)







if __name__ == "__main__":
    root = tk.Tk()
    App = MessangerApp(root)
    root.mainloop()




