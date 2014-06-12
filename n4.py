import os

print " "
os.system("./adb reboot-recovery")
#### CHANGE DOWNLOAD LINK ####
os.system("wget http://fs1.d-h.st/download")
print "Done..."
os.system("./adb reboot-bootloader")
os.system("./fastboot flash system system.img")
os.system("./fastboot flash userdata userdata.img")	
ex = raw_input("Press enter to continue...")
os.system("python done.py")

