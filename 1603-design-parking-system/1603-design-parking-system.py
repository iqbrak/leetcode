class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        result = []
        if carType == 1:
            if self.big > 0:
                result.append(True)
                self.big -= 1
            else:
                result.append(False)
        if carType == 2:
            if self.medium> 0:
                result.append(True)
                self.medium-= 1
            else:
                result.append(False)
        else:
            if self.small > 0:
                result.append(True)
                self.small -= 1
            else:
                result.append(False)

        return result

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)