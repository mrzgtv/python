from time import sleep


class TrafficLight:
    __colors = ['red', 'yellow', 'green', 'yellow']

    def running(self):
        i = 0
        while i >= 0:
            for el in TrafficLight.__colors:
                print(el)
                i += 1
                sleep(3)


traffic = TrafficLight()
traffic.running()
