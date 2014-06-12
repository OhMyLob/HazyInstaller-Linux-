import os

print " "
os.system("./adb reboot-recovery")
#### CHANGE DOWNLOAD LINK ####
os.system("wget http://drive.google.com/uc?export=download&confirm=tZlg&id=0B2moooVKpajoR2FoaUJic01TTXM")
print "Done..."
os.system("./adb reboot-bootloader")
os.system("./fastboot flash system system.img")
os.system("./fastboot flash userdata userdata.img")	
ex = raw_input("Press a key to continue...")
os.system("python done.py")
