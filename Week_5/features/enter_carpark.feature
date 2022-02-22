Feature: Vehicles entering the car park

    Scenario: A car tries to enter a car park
        Given an empty car park
        When a car with the reg plate "abc" enters the car park
        Then a car with the reg plate "abc" should be in the list of the cars