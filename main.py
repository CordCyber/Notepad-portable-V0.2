import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox
from tkinter.colorchooser import askcolor

FILE_NAME = tkinter.NONE

def fgColorChooser():
	result = askcolor(title = "Foreground Color Chooser")
	text.configure(fg = result[1])
	print(result[1])

def bgColorChooser():
	result = askcolor(title = "Background Color Chooser")
	text.configure(bg = result[1])
	print(result[1])

def new_file():
	global FILE_NAME
	FILE_NAME = "Untitled"
	text.delete('1.0', tkinter.END)

def save_file():
	data = text.get('0.1', tkinter.END)
	out = open(FILE_NAME, 'w')
	out.write(data)
	out.close()

def save_as():
	out = asksaveasfile(mode='w', defaultextension='txt')
	data = text.get('1.0', tkinter.END)
	try:
		out.write(data.rstrip())
	except Exception:
		showerror(title="Error", message="Save file error")

def open_file():
	global FILE_NAME
	inp = askopenfile(mode="r")
	if inp is None:
		return
	FILE_NAME = inp.name
	data = inp.read()
	text.delete('1.0', tkinter.END)
	text.insert('1.0', data)

def infos():
	messagebox.showinfo("Information", "New = Новый файл\n Open = Открыть\n Save = Сохранить\n Save as = Сохранить как")

def infoBar():
	messagebox.showinfo("Information", "Notepad v.0.1\nby D4RS, CordCyber\nhttps://www.youtube.com/channel/UCPG6ppFkrHi7vzn6xZfISlA")

def infoBarr():
	messagebox.showinfo("Обновление", "V0.1 - Создание Notepad\nV0.2 - Добавлени несколько кнопок для удобного пользования!\nV0.3 - Добавлена возможность изменения цвета фона и цвета текста, так-же обновлена иконка программы.")

root = tkinter.Tk()
root.title("Notepad v.0.3")
root.iconbitmap('icon.ico')

root.minsize(width=600, height=600)
root.maxsize(width=600, height=600)

text = tkinter.Text(root, width=400, height=400, wrap="word")
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)

text.pack()
menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save as", command=save_as)
fileMenu.add_command(label="Color Text", command=fgColorChooser)
fileMenu.add_command(label="Color BackGround", command=bgColorChooser)
fileMenu.add_command(label="What?", command=infos)

menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Save", command=save_file)
menuBar.add_cascade(label="Info", command=infoBar)
menuBar.add_cascade(label="Обновление", command=infoBarr)
menuBar.add_cascade(label="Exit", command=root.quit)

root.config(menu=menuBar)
root.mainloop()