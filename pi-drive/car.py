import json

class Car:

    def __init__(self, started="", direction="", speed="" ):
        self.__started = started
        self.__speed = speed
        self.__direction = direction


    def car_properties(self):
        with open('properties.json', 'r') as jsonFile:
            car_data = json.load(jsonFile)

            self.__started = car_data['started']
            self.__speed = car_data['speed']
            self.__direction = car_data['direction']


    def set_car_properties(self, speed=None, direction=None, started=None):
        with open('properties.json', 'r+') as jsonFile:
            car_data = json.load(jsonFile)

            if speed is not None:
                tmp = car_data['speed']
                car_data['speed'] = speed

                jsonFile.seek(0)
                jsonFile.write(json.dumps(car_data))
                jsonFile.truncate()

        self.car_properties()


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
    x = Car()

    x.car_properties()
    print(x.started)
    print(x.direction)
    print(x.speed)

    x.set_car_properties(60)
    print(x.started)
    print(x.direction)
    print(x.speed)
