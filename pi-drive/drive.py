try:
	current_direction = direction

	while started == "True":
		getCarSettings()

		if current_direction != direction and direction == "Forward":
			forwardDrive()
			current_direction = direction

		elif current_direction != direction and direction == "Reverse":
			reverseDrive()
			current_direction = direction

		changeSpeed(speed)
		carSteer(steer)

		sleep(0.01)

except KeyboardInterrupt:
	stopCar()
	GPIO.cleanup()