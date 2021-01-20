class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def descrition(self):
        print(f'Speed is - {self.speed}\nColor is - {self.color}\nName is - {self.name}\nIs police? - {self.is_police}')

    def go(self):
        print('Running')

    def stop(self):
        print('Stoped')

    def turn(self, direction):
        print(f'Car turned {direction}')

    def show_speed(self):
        print(f'Car speed is {self.speed}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Car speed is {self.speed}\n') if self.speed <= 60 else print('Over speed\n')

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Car speed is {self.speed}') if self.speed <= 40 else print('Over speed')

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

car_1 = WorkCar(50, 'blue', 'cat', False)
car_1.descrition()
car_1.show_speed()

car_2 = PoliceCar(120, 'white', 'daddy', True)
car_2.descrition()
car_2.show_speed()

car_3 = SportCar(250, 'red', 'zap', False)
car_3.descrition()
car_3.show_speed()

car_4 = TownCar(50, 'yellow', 'bee', False)
car_4.descrition()
car_4.show_speed()