import gtk
import os

class GUI:


  def on_window1_destroy(self, object, data=None):
    print "Bye!"

  def __init__(self):
    
    self.gladefile1 = "OTA.glade"
    self.builder = gtk.Builder()
    self.builder.add_from_file(self.gladefile1)
    self.builder.connect_signals(self)
    self.window1 = self.builder.get_object("window1")
    self.window1.show()

 
  ### UPDATE ###
  def on_button1_clicked(self, object, data=None):
    	print "There is a new update! Press Enter to upgrade!"
	waiter = raw_input(" ")
	os.system("wget http://hazy.altervista.org/HazyInstallerLinux.zip") #CHANGE LINK
        os.system("unzip -o HazyInstallerLinux.zip")
	print "Update completed!"
	print "Press enter to continue..."
	waiter2 = raw_input(" ")
	os.system("./runme.sh")
    
if __name__ == "__main__":
  main = GUI()
  gtk.main()
