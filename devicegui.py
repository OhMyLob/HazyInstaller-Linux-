import gtk
import os

class GUI3:


  def on_window1_destroy(self, object, data=None):
    print "Bye!"

  def __init__(self):
    self.gladefile1 = "devicegui.glade"
    self.builder = gtk.Builder()
    self.builder.add_from_file(self.gladefile1)
    self.builder.connect_signals(self)
    self.window1 = self.builder.get_object("window1")
    self.window1.show()


  ### NEXUS 4 ###
  def on_button4_clicked(self, object, data=None):
    os.system("python n4.py")
    self.window1.destroy()

  ### NEXUS 5 ###
  def on_button5_clicked(self, object, data=None):
    os.system("python n5.py")
    self.window1.destroy()

     

if __name__ == "__main__":
  main = GUI3()
  gtk.main()

