import gtk
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.Utils import COMMASPACE
from email.MIMEBase import MIMEBase
from email.parser import Parser
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
import mimetypes
import email


class GUI:


  def on_window1_destroy(self, object, data=None):
    print "Bye!"

  def __init__(self):
    
    self.gladefile1 = "mainmaingui.glade"
    self.builder = gtk.Builder()
    self.builder.add_from_file(self.gladefile1)
    self.builder.connect_signals(self)
    self.window1 = self.builder.get_object("window1")
    self.window1.show()

  ### OTA ###
  def on_buttonOTA_clicked(self, object, data=None):
    print "Checking for updates..."
    print " " 
    print " "
    if os.path.exists(".hazyinstallerlinuxlastvers.ion"):
        print "..."
	os.remove(".hazyinstallerlinuxlastvers.ion")
        os.system("wget http://hazy.altervista.org/download/rom/installer/.hazyinstallerlinuxlastvers.ion")
        lastf = open(".hazyinstallerlinuxlastvers.ion", 'r')
        f = open(".vers.ion", 'r')
        currentversion = f.read()
        lastversion = lastf.read()
        if currentversion < lastversion:
              os.system("python ota.py")
        else:
              print "There are no updates!"
	      print "You can go back to the User Interface of the installer ;)" 
    else:
    	os.system("wget http://hazy.altervista.org/download/rom/installer/.hazyinstallerlinuxlastvers.ion")
        lastf = open(".hazyinstallerlinuxlastvers.ion", 'r')
        lastversion = lastf.read()
        f = open(".vers.ion", 'r')
        currentversion = f.read()
        if currentversion < lastversion:
                      os.system("python ota.py")
        else:
		      print "There are no updates!"
	              print "You can go back to the User Interface of the installer! ;)" 
	
  ### NEXT ###
  def on_button1_clicked(self, object, data=None):
    self.gladefile = "maingui.glade"
    self.builder = gtk.Builder()
    self.builder.add_from_file(self.gladefile)
    self.builder.connect_signals(self)
    self.window2 = self.builder.get_object("window2")
    self.window2.show()
    self.window1.destroy()

  ### NO ###
  def on_button2_clicked(self, object, data=None):
    os.system("python noboot.py")
    self.window2.destroy()


  ### YES ###
  def on_button3_clicked(self, object, data=None):
    self.gladefile = "devicegui.glade"
    self.builder = gtk.Builder()
    self.builder.add_from_file(self.gladefile)
    self.builder.connect_signals(self)
    self.window3 = self.builder.get_object("window1")
    self.window3.show()
    self.window2.destroy()

  ### NEXUS 4 ###
  def on_button4_clicked(self, object, data=None):
    os.system("python n4.py")
    self.window3.destroy()

  ### NEXUS 5 ###
  def on_button5_clicked(self, object, data=None):
    os.system("python n5.py")
    self.window3.destroy()

  ### MAIL ###
  def on_buttonemail_clicked(self, object, data=None):
     print " "
     print "Send an E-Mail to the Developer."
     print " "
     smtp_host = 'smtp.gmail.com'
     smtp_port = 587
     server = smtplib.SMTP()
     server.connect(smtp_host,smtp_port)
     server.ehlo()
     server.starttls()
     fromaddr = raw_input('Your E-Mail: ')
     passw = input("Your Password: ")
     server.login(fromaddr, passw)

     tolist = "matteolob1704@gmail.com"
     sub = raw_input('Subject: ')

     msg = email.MIMEMultipart.MIMEMultipart()
     msg['From'] = fromaddr
     msg['To'] = email.Utils.COMMASPACE.join(tolist)
     msg['Subject'] = sub  
     msg.attach(MIMEText(raw_input('Message: ')))
     msg.attach(MIMEText('\nSent via HazyInstaller', 'plain'))
     server.sendmail(fromaddr, tolist,msg.as_string())
     print "Done...thanks for the feedback.\nNow You can go back to the User Interface."

  ### 1+1 ###
  def on_button1plus1_clicked(self, object, data=None):
    os.system("python 1plus1.py")
    self.window3.destroy()

    
if __name__ == "__main__":
  main = GUI()
  gtk.main()
