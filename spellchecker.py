import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("spell checker")
root.geometry("500x400")
root.config(background="#7D1038")
def check_spelling():
    word = enter_text.get()
    a = TextBlob (word)
    right = str(a.correct())
    
    cs = Label(root, text = "Correct spelling is :", font=("Calisto MT", 20, "bold"), bg="black", fg="#9caf88")
    cs.place(x=100, y=250)
    spell.config(text=right)

heading = Label(root, text = "spell checker", font = ("Calisto MT", 20, "bold"), background="#7D1038", fg="#9caf88")
heading.pack(pady= (50, 0))
enter_text = Entry(root, justify="center", width=30, font=("Calisto MT", 20, "bold"), background="white", border=2)
enter_text.pack(pady= 10)
enter_text.focus()

Button=Button(root, text = "Check", font=("Calisto MT", 20, "bold"), fg="green", background="black", command=check_spelling)
Button.pack()

spell = Label(root,font=("Comic Sans MS", 20), bg= "#91D8E4", fg="#460C68")
spell.place(x=350, y=250)
root.mainloop()





