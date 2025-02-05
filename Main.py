from Vehicle import FourWheels, Bus, Car

class Main:
    @staticmethod
    def main():
        bus1 = Bus("Dave", 500000)
        car1 = Car("Gray", 1000000)
        print(FourWheels.getVehicleCount())
        print(car1.getVehicleType())
        print(bus1.getVehicleType())
        print(car1.getLastOwner())
        print(bus1.getLastOwner())
        print(car1.getPrice())
        print(bus1.getPrice())
        print(car1.getName())
        print(bus1.getName())

if __name__ == '__main__':
    Main.main()