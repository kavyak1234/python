from abc import abstractmethod,ABC

class vehicle(ABC):
    def gear(self):
        print('gears')

    @abstractmethod
    def tyre(self):
        print("tyresss")

class car(vehicle):
    def tyre(self):
        print('4tyre')

class bike(vehicle):
    def tyre(self):
        print("2tyre")

polo = car()
ns = bike()
polo.tyre()
ns.tyre()
