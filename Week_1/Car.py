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

    def accelerate(self, accel_by):
        if self.fuelLevel > 0:
            # Above: Check related to Q5 of the Task for Week 1
            if self.currentSpeed + accel_by <= self.maxSpeed:
                # Above: Check related to Q3 of the Task for Week 1
                self.currentSpeed += accel_by
                self.fuelLevel -= 1
            else:
                self.currentSpeed = self.maxSpeed
            # Exit clause, returns from function when action above successfully completed
            return True
        print("Fuel level is at empty! Refuel first!")
        return False

    def brake(self, decel_by):
        if self.currentSpeed > 0:
            # Above: Check related to Q4 of the Task for Week 1
            if self.currentSpeed - decel_by >= 0:
                # Above: Check for Q2 of the Task for Week 1
                self.currentSpeed -= decel_by
            else:
                print("The speed of the car cannot go below zero!")
                self.currentSpeed = 0
            # Exit clause, returns from function when action above successfully completed
            return True
        print("The speed of the car is already at zero!")
        return False

    def refuel(self):
        self.fuelLevel += 1
