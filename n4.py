import os

print " "
#### CHANGE DOWNLOAD LINK ####
if os.path.exists("HazyROM.zip"):
	os.remove("HazyROM.zip", "openrecovery-twrp-2.7.1.0-mako.img")
	os.system("wget http://fs1.d-h.st/HazyROM.zip")
	os.system("wget http://techerrata.com/file/twrp2/mako/openrecovery-twrp-2.7.1.0-mako.img")
	print "Done..."
	print " "
	print "Rebooting to bootloader..."
	os.system("./adb reboot-bootloader")
	print "Booting TWRP..."
	os.system("./fastboot boot recovery openrecovery*.img")
	print "Done..."
	print " "
	print "Now go to: Advanced -> ADB Sideload"
	print "Press Enter when you have done this..."
	waiter = raw_input(" ")
	print "Flashing Hazy..."
	os.system("./adb sideload HazyROM.zip")
	print "Done..."	
	ex = raw_input("Press enter...")
	os.system("python done.py")
elif os.path.exists("openrecovery-twrp-2.7.1.0-mako.img"):
	os.remove("openrecovery-twrp-2.7.1.0-mako.img")
	os.system("wget http://fs1.d-h.st/HazyROM.zip")
	os.system("wget http://techerrata.com/file/twrp2/mako/openrecovery-twrp-2.7.1.0-mako.img")
	print "Done..."
	print " "
	print "Rebooting to bootloader..."
	os.system("./adb reboot-bootloader")
	print "Booting TWRP..."
	os.system("./fastboot boot recovery openrecovery*.img")
	print "Done..."
	print " "
	print "Now go to: Advanced -> ADB Sideload"
	print "Press Enter when you have done this..."
	waiter = raw_input(" ")
	print "Flashing Hazy..."
	os.system("./adb sideload HazyROM.zip")
	print "Done..."	
	ex = raw_input("Press enter...")
	os.system("python done.py")

else:   
	os.system("wget http://fs1.d-h.st/HazyROM.zip")
	os.system("wget http://techerrata.com/file/twrp2/mako/openrecovery-twrp-2.7.1.0-mako.img")
	print "Done..."
	print " "
	print "Rebooting to bootloader..."
	os.system("./adb reboot-bootloader")
	print "Booting TWRP..."
	os.system("./fastboot boot recovery openrecovery*.img")
	print "Done..."
	print " "
	print "Now go to: Advanced -> ADB Sideload"	
	print "Press Enter when you have done this..."
	waiter = raw_input(" ")
	print "Flashing Hazy..."
	os.system("./adb sideload HazyROM.zip")
	print "Done..."	
	ex = raw_input("Press enter...")		
	os.system("python done.py")

