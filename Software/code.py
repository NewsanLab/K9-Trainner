import digitalio
import board
import busio
import time
import simpleio
import analogio
#bluetooth
bt = busio.UART(board.GP16, board.GP17, baudrate = 9600, timeout=0.1) 
bateria = analogio.AnalogIn(board.A0)

def read_voltage():
    return (bateria.value * (3.3 / 65535))

def main():
  fire = digitalio.DigitalInOut(board.GP18)
  fire.direction = digitalio.Direction.OUTPUT
  fire.value = False

  sensor_infrarojo = digitalio.DigitalInOut(board.GP15)
  sensor_infrarojo.direction = digitalio.Direction.INPUT
  estado_previo_infrarojo = True  # estado inicial del sensor infrarojo
  contador = 0  # contador de engranaje
  estado_actual_infrarojo = True

  while True:
    bt.reset_input_buffer()
    buzzer = board.BUZZER
    if((bt.read(1) == b"1")):
        if (read_voltage() >= 2):
            fire.value = True
            while (contador < 3):
                estado_actual_infrarojo = sensor_infrarojo.value
                if ((not estado_actual_infrarojo) and (estado_previo_infrarojo)):
                    contador += 1
                estado_previo_infrarojo = estado_actual_infrarojo
            time.sleep(0.8)
            fire.value = False
            contador = 0
        else:
            simpleio.tone(buzzer, 440, duration = 1)

main()
