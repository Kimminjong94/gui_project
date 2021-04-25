from tkinter import*

root = Tk()
root.title("nado gui")
root.geometry("640x480")

def create_new_file():
    print("새파일을 만듭니다.")

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open file...")
menu_file.add_separator()
menu_file.add_command(label= "Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)


menu.add_cascade(label="File", menu=menu_file)

# edit 메뉴
menu.add_cascade(label="edit")

#language meny
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="python")
menu_lang.add_radiobutton(label="java")
menu_lang.add_radiobutton(label="c++")
menu.add_cascade(label="Language", menu=menu_lang)

#체크박스
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="show mimimap")
menu.add_cascade(label="View", menu=menu_view)





root.config(menu=menu)
root.mainloop()