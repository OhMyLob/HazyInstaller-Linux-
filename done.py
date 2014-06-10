import gtk
import os

class GUI:


  def on_window1_destroy(self, object, data=None):
    print "Bye!"

  def __init__(self):
    self.gladefile1 = "done.glade"
    self.builder = gtk.Builder()
    self.builder.add_from_file(self.gladefile1)
    self.builder.connect_signals(self)
    self.window1 = self.builder.get_object("window1")
    self.window1.show()

  ### NEXT ###
  def on_button1_clicked(self, object, data=None):
    self.window1.destroy()

    
if __name__ == "__main__":
  main = GUI()
  gtk.main()
