from Vehicle import Vehicle


class Carpark:

    def __init__(self, capacity):
        self.spaces = []
        self.capacity = capacity

    def add_car(self, car):
        if len(self.spaces) < self.capacity and car.kind == "Car" and not self.is_duplicate(car.reg):
            self.spaces.append(car)
            return True
        return False

    def is_duplicate(self, reg_num):
        for car in self.spaces:
            if car.reg == reg_num:
                return True
        return False
