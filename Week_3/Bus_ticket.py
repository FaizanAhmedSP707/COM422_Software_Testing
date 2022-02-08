"""
This program is concerned with the first Task from Week 3, which is about the fares that passengers
will pay to obtain a bus ticket (the fare amount). It involves using the TDD process to write tests for code
that will be run first, and then typing up the minimal amount of code that will pass that test
"""


def hasFareMoney(amt_available):
    if amt_available >= 4:
        return True
