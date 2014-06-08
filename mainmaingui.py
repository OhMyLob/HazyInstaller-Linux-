import gtk
import os
import time

class GUI:


  def on_window1_destroy(self, object, data=None):
    print "Bye!"

  def __init__(self):
    self.gladefile = "mainmaingui.glade"
    self.builder = gtk.Builder()
    self.builder.add_from_file(self.gladefile)
    self.builder.connect_signals(self)
    self.window = self.builder.get_object("window1")
    self.window.show()


  def on_button1_clicked(self, object, data=None):
    self.window = self.builder.get_object("window1")
    self.window.destroy()
    os.system("python maingui.py")
     

if __name__ == "__main__":
  main = GUI()
  gtk.main()
