from tkinter import *
from tkinter import font

import custom_button
import password

def load_password(window, menu_frame):
    menu_frame.pack_forget()
    password.start(window)


def start(win):
    win.geometry("1280x600")
    win.title("Graphical Authentication System")

    menu_frame = Frame(win, height=600, width=1280)
    menu_frame.pack(fill='both', expand=1)

    label = Label(menu_frame, text="Graphical Authentication System", font=('Arial', 30))
    label.pack(padx=40, pady=30)

    btn_height = 90
    btn_width = 450
    btn_font = ('Trebuchet MS', 14)
    btn4 = custom_button.TkinterCustomButton(master=menu_frame, text="Select Gaphical Password Authentication",
                                             text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=10,
                                             command=lambda: load_password(win, menu_frame)).place(relx=0.5,
                                                                                                   rely=0.5,
                                                                                                   anchor=CENTER)

    win.mainloop()


if __name__ == "__main__":
    win = Tk()
    start(win)






