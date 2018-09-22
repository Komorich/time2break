import notify2
import time
trew = int(1)
while (trew == 1):
	time.sleep(1199)
	#ICON_PATH = "/home/morllow/Documents/all/not.ico"
	notify2.init("Time to break")
	n = notify2.Notification("Time to break")#, icon = ICON_PATH)
	n.set_urgency(notify2.URGENCY_CRITICAL)
	n.set_timeout(1)
	n.show()
