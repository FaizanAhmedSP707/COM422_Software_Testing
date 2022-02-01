import pytest
from Car import Car


def test_create_car():
    # Testing the initialiser function to check everything is working A-ok.
    c1 = Car('Toyota', 'Corolla', 'SE', 1.8, 'Red', 'RWD', 'Automatic', 60, 200, 85)
    assert c1.manufacturer == 'Toyota'
    assert c1.make == 'Corolla'
    assert c1.model == 'SE'
    assert c1.engine_size == 1.8
    assert c1.colour == 'Red'
    assert c1.drivetrain == 'RWD'
    assert c1.transmission == 'Automatic'
    assert c1.currentSpeed == 60
    assert c1.maxSpeed == 200
    assert c1.fuelLevel == 85


"""Testing for the positive cases, along with the test cases"""


def test_car_acceleration_pass():
    # Testing with normal data
    c1 = Car('Toyota', 'Corolla', 'SE', 1.8, 'Red', 'RWD', 'Automatic', 120, 200, 85)
    assert c1.accelerate(36)
    assert c1.currentSpeed == 156


def test_car_speed_accel_boundary():
    # Testing the current speed is at the boundary value
    c1 = Car('Toyota', 'Corolla', 'SE', 1.8, 'Red', 'RWD', 'Automatic', 120, 200, 85)
    assert c1.accelerate(80)
    assert c1.currentSpeed == 200
