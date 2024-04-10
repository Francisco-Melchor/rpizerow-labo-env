from gpiozero import LED
from time import sleep
from signal import pause

ledG = LED(19)
ledR = LED(13)
ledB = LED(26)

while True:
	ledG.on()
	sleep(0.25)
	ledB.off()

	ledR.on()
	sleep(1)
	ledG.off()

	ledB.on()
	sleep(0.5)
	ledR.off()
