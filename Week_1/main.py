# This is the main file for Task 1

from Car import Car

if __name__ == '__main__':
    car1 = Car('Toyota', 'Camry', 'SE', 2.0, 'Silver', 'FWD', 'Automatic', 46, 220, 64)
    car2 = Car('Honda', 'Accord', 'Limited', 3.5, 'Beige', 'RWD', 'Manual', 100, 260, 87)

    print(f"Car 1 is moving at {car1.currentSpeed}kph with {car1.fuelLevel}% fuel left in the tank.")
    print(f"Car 2 is moving at {car2.currentSpeed}kph with {car2.fuelLevel}% fuel left in the tank.\n")

    # EARLIER DEBUGGING PURPOSE, COMMENTED OUT RIGHT NOW
    # car1.accelerate(26)
    # car2.brake(27)

    print(f"Car 1 is moving at this speed now: {car1.currentSpeed}kph with fuel qty: {car1.fuelLevel}%.")
    print(f"Car 2 is moving at this speed now: {car2.currentSpeed}kph with fuel qty: {car2.fuelLevel}%.\n")

    # Q1, Q3 and Q5 of improving the methods
    while True:
        car_select_opt = input("Please select either car1 (type '1') to increase its' speed, or car 2 (type '2'): ")
        if car_select_opt == '1':
            accelerate_by = int(input("Please enter a value for which the speed of the car will increase by:\n"))
            car1.accelerate(accelerate_by)
            print(f"Car 1's current speed is : {car1.currentSpeed}kph.")
            break
        elif car_select_opt == '2':
            accelerate_by = int(input("Please enter a value for which the speed of the car will increase by:\n"))
            car2.accelerate(accelerate_by)
            print(f"Car 2's current speed is : {car2.currentSpeed}kph.")
            break
        else:
            print("Exiting loop, returning....")
            break

    while True:
        user_select_opt = input("Please select either car1 (type '1') to decrease its' speed, or car 2 (type '2'): ")
        if user_select_opt == '1':
            decelerate_by = int(input("Please enter a value for which the speed of the car will decrease by:\n"))
            car1.brake(decelerate_by)
            print(f"Car 1's current speed is {car1.currentSpeed}kph.")
            break
        elif user_select_opt == '2':
            decelerate_by = int(input("Please enter a value for which the speed of the car will decrease by:\n"))
            car2.brake(decelerate_by)
            print(f"Car 2's current speed is {car2.currentSpeed}kph.")
            break
        else:
            print("Exiting loop, returning....")
            break

    while True:
        user_select_opt = input("Please select either car1 (type '1'), or car 2 (type '2') for refueling: ")
        if user_select_opt == '1':
            refuel_fuel_val_by = int(input("Please enter a value for which the speed of the car will decrease by:\n"))
            car1.refuel(refuel_fuel_val_by)
            print(f"Car 1's fuel quantity is {car1.fuelLevel} litres.")
            break
        elif user_select_opt == '2':
            refuel_fuel_val_by = int(input("Please enter a value for which the speed of the car will decrease by:\n"))
            car2.refuel(refuel_fuel_val_by)
            print(f"Car 2's fuel quantity is {car2.fuelLevel} litres.")
            break
        else:
            print("Exiting loop, returning....")
            break
