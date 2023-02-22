import time
class TrafficLight:
    __color = ['red', 'yellow', 'green']
    def running(self):
        i = 0
        print(self.__color[i])
        time.sleep(7)
        print(self.__color[i + 1])
        time.sleep(2)
        print(self.__color[i + 2])
        time.sleep(7)

traffic_light = TrafficLight()
traffic_light.running()
