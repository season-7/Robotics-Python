import RPi.GPIO as GPIO
from time import sleep
import datetime


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


pinA = pwmPin(forward)
pinB = pwmPin(reverse)


def current_time():
	return datetime.datetime.now().time()


def end_time(secs):
	tm = current_time()
	start_time = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.seconds)
	return sys_time + datetime.timedelta(seconds = secs)
