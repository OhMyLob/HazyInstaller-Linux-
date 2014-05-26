import urllib
import os

print " "
print "Downloading recovery..."
urllib.urlretrieve("http://download2.clockworkmod.com/recoveries/recovery-clockwork-touch-6.0.4.7-mako.img", "recovery-clockwork-touch-6.0.4.7-mako.img")
print "Recovery downloaded..."			
os.system("./adb reboot-bootloader")
os.system("./fastboot flash recovery recovery-clockwork-touch-6.0.4.7-mako.img")
print "Recovery flashed!"
print "Downloading ROM..."
#### CHANGE DOWNLOAD LINK ####
urllib.urlretrieve("http://fs1.d-h.st/download/00113/qWJ/TwixKat_Alpha.zip", "TwixKat_Alpha.zip")
print "Done..."
os.system("./adb reboot-bootloader")
os.system("./fastboot flash system system.img")
os.system("./fastboot flash userdata userdata.img")
ex = raw_input("Press enter to continue...")
os.system("python n4ok.py")	

