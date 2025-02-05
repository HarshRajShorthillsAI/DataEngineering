from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def getVehicleCount(cls)->int:
        pass

    @abstractmethod
    def getVehicleType(self):
        pass

    @abstractmethod
    def getName(self):
        pass

class Owner(ABC):
    @abstractmethod
    def getLastOwner(self):
        pass

    @abstractmethod
    def getPrice(self):
        pass

    @abstractmethod
    def getName(self):
        pass

class FourWheels(Vehicle, Owner): #abstract class
    __count = 0
    
    def __init__(self, lastOwner, price):
        self.lastOwner = lastOwner
        self.price = price
        self.vehicleType = None

    def getLastOwner(self):
        return self.lastOwner

    def getPrice(self):
        return self.price

    def getVehicleType(self):
        return self.vehicleType
    
    @classmethod
    def getVehicleCount(cls)->int:
        return cls.__count
    
    @classmethod
    def incrementVehicleCount(cls):
        cls.__count+=1

    def getName(self):
        return self.__class__
    
class Car(FourWheels):
    def __init__(self, lastOwner, price):
        FourWheels.incrementVehicleCount()
        super().__init__(lastOwner=lastOwner, price=price)
        self.vehicleType='Car'

    def getVehicleCount(self):
        return super().getVehicleCount()
    
class Bus(FourWheels):
    def __init__(self, lastOwner, price):
        super().__init__(lastOwner=lastOwner, price=price)
        FourWheels.incrementVehicleCount()
        self.vehicleType = 'Bus'

    def getVehicleCount(self):
        return super().getVehicleCount()