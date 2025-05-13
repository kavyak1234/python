#single inheritance
class vehicle:
    def engine(self):
        print("engine")
    def key(self):
        print("key")
    def wheels(self):
        print("wheels")
    def seat(self):
        print("seat")

class car(vehicle):
    def engine(self):
        print("engine")
    def key(self):
        print("key")
    def wheels(self):
        print("4wheels")
    def seat(self):
        print("5seat")

swift=car()
swift.engine()
swift.key()
swift.seat()
swift.wheels()
