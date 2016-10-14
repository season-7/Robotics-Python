import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

enableA = 12
reverse = 38
forward = 40

enableB = 33
left = 37
right = 35


def gpioInit():
	GPIO.setup(enableA, GPIO.OUT)
	GPIO.setup(enableA, GPIO.OUT)
	GPIO.setup(enableA, GPIO.OUT)

	GPIO.setup(enableA, GPIO.OUT)
	GPIO.setup(enableA, GPIO.OUT)
	GPIO.setup(enableA, GPIO.OUT)


def pwmPin(gpioPin):
	return GPIO.PWM(pwmPin, 1000)


