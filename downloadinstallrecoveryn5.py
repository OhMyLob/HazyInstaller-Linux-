import os
import urllib

print " "
print "Downloading recovery..."
urllib.urlretrieve("http://download2.clockworkmod.com/recoveries/recovery-clockwork-touch-6.0.4.5-hammerhead.img", "recovery-clockwork-touch-6.0.4.5-hammerhead.img")
print "Recovery downloaded..."			
os.system("./adb reboot-bootloader")
os.system("./fastboot flash recovery recovery-clockwork-touch-6.0.4.7-mako.img")
print "Recovery flashed!"
print "Downloading ROM..."
urllib.urlretrieve("https://drive.google.com/uc?export=download&confirm=tZlg&id=0B2moooVKpajoR2FoaUJic01TTXM", "TwixKat-alpha1-hammerhead.zip")
print "Done..."
os.system("./adb reboot-bootloader")
os.system("./fastboot flash system system.img")
os.system("./fastboot flash userdata userdata.img")
ex = raw_input("Press enter to continue...")
os.system("python n5ok.py")	

