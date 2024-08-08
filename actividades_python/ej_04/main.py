from gpiozero import PWMLED
import ADS1x15
import time
import math

# Declara el pin de I2C y el registro
ADS = ADS1x15.ADS1115(1,0x48)
# Declara el modo a utilizar.
ADS.setMode(ADS.MODE_SINGLE)
# Hace que la ganancia del ADC sea de +-6,144V.
ADS.setGain(ADS.PGA_4_096V)
# Convierte el valor obtenido por el ADC a un valor de voltaje.
fact = ADS.toVoltage()

# Declara que los pines 26 y 19 corresponden al LED rojo y azul y permite variar su brillo usando PWM.
LEDa = PWMLED(26)
LEDr = PWMLED(19)

# Variables para el cálculo de la temperatura
Vcc = 3.3  # Voltaje de referencia (VCC)
R = 10000  # Resistencia fija en el divisor de tensión
beta = 3900  # Constante beta del termistor
T0 = 298.15  # Temperatura de referencia (25 °C en Kelvin)
T= 0 # Temperatura en grados Celsius
Rt = 0 # Resistencia del termistor


while True:
    # Lectura de los valores analógicos del potenciómetro y termistor
    LecturaPote = ADS.readADC(3)
    LecturaTerm = ADS.readADC(1)

    # Conversión de las lecturas a voltaje
    LecturaVPot = LecturaPote * fact
    LecturaVTerm = LecturaTerm * fact

    # Cálculo de la resistencia del termistor
    Rt = (R * LecturaVTerm) / (Vcc - LecturaVTerm)

    # Conversión a temperatura usando la ecuación de Steinhart-Hart
    T = beta / (math.log(Rt / R) + (beta / T0))
    T = T - 273.15  # Conversión a grados Celsius

    # Escalar el voltaje del potenciómetro a un rango de 0 a 30 grados Celsius
    TempPot = (LecturaVPot / 3.3) * 30

    # Calcular la diferencia entre la temperatura deseada y la medida
    dif = abs(TempPot - T)

    # Limitar la diferencia a un máximo de 5 grados
    if dif > 5:
        dif = 5

    # Control de los LEDs según la diferencia de temperatura
    if TempPot > T:
        LEDr.value = dif / 5  # Brillo proporcional a la diferencia
        LEDa.value = 0         # Apaga el LED Azul
    elif TempPot < T:
        LEDa.value = dif / 5  # Brillo proporcional a la diferencia
        LEDr.value = 0         # Apaga el LED Rojo
    else:
        LEDa.value = 0         # Apaga ambos LEDs si no hay diferencia
        LEDr.value = 0

    # Muestra los valores en la consola
    print("Termistor: {0:.3f} V, {1:.3f} °C".format(LecturaVTerm, T))
    print("Potenciómetro: {0:.2f} °C".format(TempPot))

    time.sleep(1)  # Pausa antes de la siguiente iteración
