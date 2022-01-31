# This file contains a class blueprint that will be used in another file in the same directory

class Car:
    def __init__(self, manufacturer_name, make_name, model_name, Engine_CC, car_colour, drivetrain_config,
                 transmission_type, inst_speed, speed_lim_val, cur_fuel_qty):
        self.manufacturer = manufacturer_name
        self.make = make_name
        self.model = model_name
        self.engine_size = Engine_CC
        self.colour = car_colour
        self.drivetrain = drivetrain_config
        self.transmission = transmission_type
        self.currentSpeed = inst_speed
        self.maxSpeed = speed_lim_val
        self.fuelLevel = cur_fuel_qty

    def accelerate(self):
        self.currentSpeed += 1
        self.fuelLevel -= 1

    def brake(self):
        self.currentSpeed -= 1

    def refuel(self):
        self.fuelLevel += 1

