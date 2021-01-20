class Road:

    def __init__(self, __length, __width):
        self.__length = int(__length)
        self.__width = int(__width)

    def weight(self):
        return f'Масса асфальта - {self.__length * self.__width * 25 * 5} тонн'

road_1 = Road(200, 20)
print(road_1.weight())