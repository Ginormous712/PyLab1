from Airport.Exceptions import EnterAirlineIDException


class Airline:
    def __init__(self, airline_id, airline_name):
        if isinstance(airline_id, int) and airline_id > 0:
            self.__id = airline_id
            self.__airline_name = airline_name
        else:
            raise EnterAirlineIDException(airline_id)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def airline_name(self):
        return self.__airline_name

    @airline_name.setter
    def airline_name(self, airline_name):
        self.__airline_name = airline_name

    def __str__(self):
        return (f'ID: {self.__id}\n'
                f'Name: {self.__airline_name}\n')

    def __repr__(self):
        return self.__str__()
