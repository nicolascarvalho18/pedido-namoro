import tkinter as tk
import random

def move_button_no(event):
    """Move the 'Não' button to a random position."""
    btn_no.place(x=random.randint(0, 300), y=random.randint(0, 300))

def confirm_love():
    """Show a message when 'Sim' is clicked."""
    lbl_question.config(text="Eu sabia que você diria sim! ❤️")
    btn_yes.destroy()
    btn_no.destroy()


root = tk.Tk()
root.title("Pedido Especial")

lbl_question = tk.Label(root, text="Quer namorar comigo?", font=("Arial", 16))
lbl_question.pack(pady=50)

btn_yes = tk.Button(root, text="Sim", font=("Arial", 14), bg="lightgreen", command=confirm_love)
btn_yes.place(x=100, y=200)


btn_no = tk.Button(root, text="Não", font=("Arial", 14), bg="lightcoral")
btn_no.place(x=200, y=200)
btn_no.bind("<Enter>", move_button_no)

root.mainloop()
