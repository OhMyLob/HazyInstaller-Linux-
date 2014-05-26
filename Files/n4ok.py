from Tkinter import *
import os

class GUI(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.master.title("Hazy Installer - Done!")
		w = 400
		h = 310
		ws = self.master.winfo_screenwidth()
		hs = self.master.winfo_screenheight()
		x = (ws/2)-(w/2)
		y = (hs/2)-(h/2)
		self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))
		self.master.resizable(False, False)
		self.grid()
		self._button1 = Button(self, text = "Bye!", command = self._yes)
		self._imageup = PhotoImage(file = "UP.png")
		self._imageLabel = Label(self, image = self._imageup)
		self._imageLabel.grid(row = 0, column = 0)
		self._image = PhotoImage(file = "n4_happy-01.png")
		self._imageLabel = Label(self, image = self._image)
		self._imageLabel.grid(row = 1, column = 0)
		self._button1.grid(row = 2, column = 0)
		self._imagedown = PhotoImage(file = "DOWN.png")
		self._imageLabel = Label(self, image = self._imagedown)
		self._imageLabel.grid(row = 3, column = 0)
	
	def _yes(self):
		self.master.destroy() 

def main():
	GUI().mainloop()

main()
