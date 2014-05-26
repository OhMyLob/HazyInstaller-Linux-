import urllib
import os

print " "
os.system("./adb reboot-recovery")
print "Downloading..."
#### CHANGE DOWNLOAD LINK ####
urllib.urlretrieve("http://fs1.d-h.st/download/00113/qWJ/TwixKat_Alpha.zip", "TwixKat_Alpha.zip")
print "Done..."
os.system("./adb reboot-bootloader")
os.system("./fastboot flash system system.img")
os.system("./fastboot flash userdata userdata.img")	
ex = raw_input("Press enter to continue...")
os.system("python n4ok.py")

