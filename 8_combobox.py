import tkinter.ttk as ttk
from tkinter import*

root = Tk()
root.title("nado gui")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1, 32)] 
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")


combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")

def btncmd():
    print(combobox.get())


btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()