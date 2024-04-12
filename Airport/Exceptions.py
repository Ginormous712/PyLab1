class EnterIDException(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Invalid ID: {self.id}. Must be positive integer"


class EnterFlightIDException(EnterIDException):
    def __str__(self):
        return f"Invalid Flight ID: {self.id}. Must be positive integer"


class EnterAirlineIDException(EnterIDException):
    def __str__(self):
        return f"Invalid Airline ID: {self.id}. Must be positive integer"


class AirlineIDExistsException(EnterIDException):
    def __str__(self):
        return f"Invalid Airline ID: {self.id}. ID already exists"


class AirlineIDNotFoundException(EnterIDException):
    def __str__(self):
        return f"Invalid Airline ID: {self.id}. ID is not found"


class FlightIDExistsException(EnterIDException):
    def __str__(self):
        return f"Invalid Flight ID: {self.id}. ID already exists"


class FlightIDNotFoundException(EnterIDException):
    def __str__(self):
        return f"Invalid Flight ID: {self.id}. ID is not found"