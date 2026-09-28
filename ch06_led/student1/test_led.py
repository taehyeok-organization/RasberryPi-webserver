import time
import RPi.GPIO as GPIO
import config

LED = config.LED_PIN
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
t = 0.1
try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(t)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(t)
except KeyboardInterrupt:
    GPIO.output(LED, GPIO.LOW)
