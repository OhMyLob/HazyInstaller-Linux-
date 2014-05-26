from Tkinter import * 
import os

class GUI(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.master.title("Hazy Installer - Bootloader")
		w = 800
		h= 310
		ws = self.master.winfo_screenwidth()
		hs = self.master.winfo_screenheight()
		x = (ws/2)-(w/2)
		y = (hs/2)-(h/2)
		
		self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))
		self.master.resizable(False, False)
		self.grid()
		self._button1 = Button(self, text = "Bootloader Unlocked", command = self._yes)
		self._button2 = Button(self, text = "Bootloader NOT Unlocked", command = self._no)
		self._image4 = PhotoImage(file = "bootloader-01.png")
		self._imageLabel4 = Label(self, image = self._image4)
		self._image = PhotoImage(file = "bootloader-01.png")
		self._imageLabel = Label(self, image = self._image)
		self._imageLabel.grid(row = 1, column = 1)
		self._imageLabel4.grid(row = 1, column = 0)
		self._button1.grid(row = 2, column = 0)
		self._button2.grid(row = 2, column = 1)

		self._imageup = PhotoImage(file = "UP.png")
		self._imageLabel = Label(self, image = self._imageup)
		self._imageLabel.grid(row = 0, column = 0)

		self._imageup2 = PhotoImage(file = "UP.png")
		self._imageLabel = Label(self, image = self._imageup2)
		self._imageLabel.grid(row = 0, column = 1)

		self._imagedown = PhotoImage(file = "DOWN.png")
		self._imageLabel = Label(self, image = self._imagedown)
		self._imageLabel.grid(row = 3, column = 0)

		self._imagedown2 = PhotoImage(file = "DOWN.png")
		self._imageLabel = Label(self, image = self._imagedown2)
		self._imageLabel.grid(row = 3, column = 1)
		
		self.master.bind("<KeyRelease-Right>", lambda event: self._no())
		self.master.bind("<KeyRelease-Left>", lambda event: self._yes())


	def _yes(self):
		self.master.destroy()
		os.system("python devicechoosergui.py")
		
	def _no(self):
		self.master.destroy()
		os.system("python noboot.py")    

def main():
	GUI().mainloop()

main()
