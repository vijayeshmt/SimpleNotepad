"""
Written by Vijayesh M T
Date:29/05/21
Python-Tkinter
"""

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
	global file
	root.title("Untiled - Notepad")
	file= None
	TextArea.delete(1.0,END)
	pass
def openFile():
	global file
	file = askopenfilename(defaultextension=".txt",
	                       filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
	if file == "":
		file = None
	else:
		root.title(os.path.basename(file)+ "- Notepad")
		TextArea.delete(1.0,END)
		f = open(file,"r")
		TextArea.insert(1.0,f.read())
		f.close()
	pass
def saveFile():
	global file
	if file == None:
		file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
	                       filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
		if file =="":
			file = None
		else:
			f = open(file,"w")
			f.write(TextArea.get(1.0,END))
			f.close()
			root.title(os.path.basename(file)+ "-Notepad")

	else:
		f = open(file, "w")
		f.write(TextArea.get(1.0, END))
		f.close()

	pass
def quitApp():
	root.destroy()
	pass
def cut():
	TextArea.event_generate(("<<Cut>>"))
	pass
def copy():
	TextArea.event_generate(("<<Copy>>"))
	pass
def paste():
	TextArea.event_generate(("<<Paste>>"))
	pass
def about():
	showinfo("Notepad","Notepad by Vijayesh M T")
	pass

if __name__ == '__main__':
	root = Tk()
	root.title("Untitled - Notepad")
	# root.wm_iconbitmap("filename.ico")
	root.geometry("720x520+100+100")
	root.wm_iconbitmap("Note.ico")
	#adding text area
	TextArea = Text(root,font="lucida,13",bg="white",padx=3,pady=3,borderwidth=5,)
	file = None
	TextArea.pack(fill=BOTH,expand=True)
	#Menu bar
	Menubar = Menu(root)
	#file menu starts here
	Filemenu = Menu(Menubar,
	                tearoff = 0,
	                )
	#open new file
	Filemenu.add_command(label="New",command=newFile)

	#To open existing file
	Filemenu.add_command(label="Open",command=openFile)

	#To save current file
	Filemenu.add_command(label="Save",command= saveFile)
	Filemenu.add_separator()
	Filemenu.add_command(label="Exit",command=quitApp)
	Menubar.add_cascade(label="File",menu=Filemenu)
	#file menu ends

	#Edit menu starts
	EditMenu = Menu(Menubar,tearoff=0)
	#cut,copy and paste
	EditMenu.add_command(label="Cut",command=cut)
	EditMenu.add_command(label="Copy",command=copy)
	EditMenu.add_command(label="Paste",command=paste)

	Menubar.add_cascade(label="Edit",menu=EditMenu)
	#edit menu ends

	# help menu starts
	HelpMenu = Menu(Menubar,tearoff=0)
	HelpMenu.add_command(label="About Notepad",command=about)
	Menubar.add_cascade(label="Help",menu=HelpMenu)


	#help ,menu ends

	root.config(menu=Menubar)

	#adding scrollbar
	Scrollbar  = Scrollbar(TextArea,)
	Scrollbar.pack(side=RIGHT,fill=Y,)
	Scrollbar.config(command=TextArea.yview)
	TextArea.config(yscrollcommand=Scrollbar.set)
	root.mainloop()