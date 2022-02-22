from behave import *
from Week_5.Carpark import Carpark
from Week_5.Vehicle import Vehicle


@given(u'an empty car park')
def step_impl(context):
    cp = Carpark(15)
    context.carpark = cp
    # The 'context' thing here allows us to pass along variables between our
    # tests. First you put the word 'context', then put the name of the variable
    # and assign to it whatever your variables/objects are.


@when(u'a car with the reg plate "abc" enters the car park')
def step_impl(context):
    car = Vehicle("abc", "Car")
    context.carpark.add_car(car)


@then(u'a car with the reg plate "abc" should be in the list of the cars')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a car with the reg plate "abc" should be in the list of the cars')
