from Airport.Exceptions import EnterFlightIDException
from Airport.Exceptions import EnterAirlineIDException

class Flight:
    def __init__(self, id, airline, destination, departure_time, arrival_time):
        if isinstance(id, int) and id > 0:
            self.__id = id
            if airline > 0 and isinstance(airline, int):
                self.__airline = int(airline)
                self.__destination = destination
                self.__departure_time = departure_time
                self.__arrival_time = arrival_time
            else:
                raise EnterAirlineIDException(airline)
        else:
            raise EnterFlightIDException(id)


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def airline(self):
        return self.__airline

    @airline.setter
    def airline(self, airline):
        self.__airline = airline

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, destination):
        self.__destination = destination

    @property
    def departure_time(self):
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, departure_time):
        self.__departure_time = departure_time

    @property
    def arrival_time(self):
        return self.__arrival_time

    @arrival_time.setter
    def arrival_time(self, arrival_time):
        self.__arrival_time = arrival_time

    def __str__(self):
        return (f"ID: {self.__id}\n"
                f"Airline: {self.__airline}\n"
                f"Destination: {self.__destination}\n"
                f"Departure Time: {self.__departure_time}\n"
                f"Arrival Time: {self.__arrival_time}\n")

    def __repr__(self):
        return self.__str__()
