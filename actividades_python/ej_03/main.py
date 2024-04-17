from gpiozero import LED, Buzzer
from time import sleep

ledG = LED(13)
ledR = LED(19)
ledB = LED(26)

buzzer = Buzzer(22)

buzz_on = "buzz on"
buzz_off = "buzz off"

rgb_red = "rgb red"
rgb_blue = "rgb blue"
rgb_green = "rgb green"

while True:

        Comando = input("prompt:")

        if Comando == buzz_on:
                buzzer.on()

        if Comando == buzz_off:
                buzzer.off()

        if Comando == rgb_red:
                ledR.toggle()

        if Comando == rgb_green:
                ledG.toggle()

        if Comando == rgb_blue:
                ledB.toggle()

        sleep(0.5)

