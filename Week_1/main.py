# This is the main file for Task 1

from Car import Car

car1 = Car('Toyota', 'Camry', 'SE', 2.0, 'Silver', 'FWD', 'Automatic',
           46, 220, 64)
car2 = Car('Honda', 'Accord', 'Limited', 3.5, 'Beige', 'RWD', 'Manual',
           100, 260, 87)

print(f"Car 1 is moving at {car1.currentSpeed}kph with {car1.fuelLevel}% fuel left in the tank.")
print(f"Car 2 is moving at {car2.currentSpeed}kph with {car2.fuelLevel}% fuel left in the tank.")
