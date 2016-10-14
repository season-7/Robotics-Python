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


def forwardCar():
	GPIO.output(enableA, True)
	GPIO.output(enableA, False)
	GPIO.output(enableA, True)

	pinB.stop()
	pinA.start(50)


def reverseCar():
	GPIO.output(enableA, True)
	GPIO.output(enableA, False)
	GPIO.output(enableA, True)

	pinB.stop()
	pinA.start(50)


def carSteer(steer):
	if steer == "Left":
		pwm = GPIO.PWM(left, 1000)
		pwm.start(100)

		GPIO.output(enableB, True)
		GPIO.output(right, False)

		sleep(0.3)

		pwm.stop()

		# setCarSteering("")

	elif steer == "Right":
		pwm = GPIO.PWM(left, 1000)
		pwm.start(100)

		GPIO.output(enableB, True)
		GPIO.output(right, False)

		sleep(0.3)

		pwm.stop()

		# setCarSteering("")

	else:
		pass


def changeSpeed(gear, speed):
	if gear is not 0:
		pinA.ChangeDutyCycle(speed)
		return

	pinB.ChangeDutyCycle(speed)

	sleep(0.1)


def carSpeed(gear, car_direction()):
	global speed
	if gear == 1:
		if speed < 69:
			speed = 70
		
		end_time = end_time(30)

		while current_time() < end_time:
			changeSpeed(gear, speed)

			if speed < 80:
				speed += 2
			else:
				speed -= 2

			sleep(2)

	elif gear == 2:
		if speed < 79:
			speed = 80
		
		end_time = end_time(30)

		while current_time() < end_time:
			changeSpeed(gear, speed)

			if speed < 90:
				speed += 2
			else:
				speed -= 2

			sleep(2)

	elif gear == 3:
		if speed < 80:
			speed = 50
		
		end_time = end_time(60)

		while current_time() < end_time:
			changeSpeed(gear, speed)

			if speed < 100:
				speed += 5

			sleep(1)

	elif gear == 4:
		if speed < 90:
			speed = 70
		
		end_time = end_time(60)

		while current_time() < end_time:
			changeSpeed(gear, speed)

			if speed < 100:
				speed += 5

			sleep(1)

	elif gear == 0:
		speed = 70
		changeSpeed(gear, speed)

	else:
		pass
	