from time import sleep

class Trafficlight:

    __color = ['Red', 'Yellow', 'Green']

    def running(self):

        i = 0

        while i < 3:
            print(f'Trafficlight is switching to {Trafficlight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1

traffic_light_1 = Trafficlight()
traffic_light_1.running()
