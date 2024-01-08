from tkinter import *

TIMER = None
USER_TEXT = ""


def timer(event):
    global TIMER, USER_TEXT
    if TIMER is not None:
        window.after_cancel(TIMER)
    if event.keysym == 'BackSpace':
        USER_TEXT = USER_TEXT[0:len(USER_TEXT) - 1]
    elif event.char:
        USER_TEXT += event.char
        TIMER = window.after(5000, reset)


def reset():
    global TIMER, USER_TEXT
    text_area.delete(1.0, END)
    TIMER = None
    USER_TEXT = ""


def save():
    global USER_TEXT
    if USER_TEXT == '':
        return
    with open('written_text.txt', 'w') as save_text:
        save_text.write(text_area.get("1.0", END))
        USER_TEXT = ""


window = Tk()
window.title("Disappearing Text Desktop App")

title = Label(window, text="WRITE WITH MAGICAL INK", font=('Calibri', 24, 'normal'))
title.grid(row=0, column=0, columnspan=3)

instruction = Label(window, text="If you don't press any key for 5 seconds, the text you have written will disappear")
instruction.grid(row=2, column=0, columnspan=3)

text_area = Text(font=('Times New Roman', 14, 'bold'), fg='white', bg='black',
                 width=100, height=15,
                 highlightcolor='blue', highlightthickness=2, wrap='word',
                 padx=5, pady=5)
text_area.grid(row=3, column=0, columnspan=3, padx=15, pady=15)
text_area.bind('<KeyPress>', timer)

reset_btn = Button(window, text='Reset', fg='black', command=reset, border=3, width=50)
reset_btn.grid(row=4, column=0)

save = Button(window, text='save', command=save, border=3, width=50)
save.grid(row=4, column=2)
window.mainloop()