import os

os.system("./adb reboot-bootloader")
os.system("./fastboot oem unlock")
print "Select yes..."
print "...and then your bootloader will be unlocked!"
finished = input("Press a key to install Hazy ROM...")
os.system("python devicechoosergui.py")	
