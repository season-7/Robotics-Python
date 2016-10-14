class Car:

    def __init__(self, started, direction, speed = 50 ):
        self.__started = started
        self.__speed = speed
        self.__direction = direction

    @property
    def started(self):
        return self.__started

    @property
    def direction(self):
        return self.__direction

    @property
    def speed(self):
        return self.__speed
  
if __name__ == "__main__":
    x = Car("True", "Forward-Left", 60 )
    print(x.started)
    print(x.direction)
    print(x.speed)
