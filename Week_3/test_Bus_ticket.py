import Bus_ticket
import pytest


def test_has_money_for_bus_fare():
    assert Bus_ticket.hasFareMoney(4) == True
