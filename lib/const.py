from enum import Enum

class Type(Enum):
    REQ = 1
    ACK = 3
    TKN = 2
    VAL = 6
    DON = 7

    BAD = 0

    def __str__(self):
        return "'" + self.name + "'"


class Address:
    BROADCAST = ("40.20.11.255", 6561)
    VALIDATOR = "40.20.11.243"
    WALLET    = "40.20.11.29"
