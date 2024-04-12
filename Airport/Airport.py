from xml.dom import minidom
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

from Airport.Airline import Airline
from Airport.Flight import Flight
from Airport.Exceptions import *


class Airport:
    def __init__(self, xml_path: str):
        self.__airlines = []
        self.__flights = []
        self.__xml_path = xml_path

        domtree = minidom.parse(self.__xml_path)
        collection = domtree.documentElement
        airlines = collection.getElementsByTagName('Airline')
        flights = collection.getElementsByTagName('Flight')

        for airline in airlines:
            airline_id = int(airline.getAttribute('id'))
            name = airline.getAttribute('name')
            self.__airlines.append(Airline(airline_id, name))

        for flight in flights:
            flight_id = int(flight.getAttribute('id'))
            airline_id = int(flight.getAttribute('airline_id'))
            destination = flight.getAttribute('destination')
            departure_time = flight.getAttribute('departure_time')
            arrival_time = flight.getAttribute('arrival_time')
            """
            departure_time = datetime.strptime(flight.getAttribute('departure_time'),
                                               '%Y-%m-%dT%H:%M:%S')

            arrival_time = datetime.strptime(flight.getAttribute('arrival_time'),
                                             '%Y-%m-%dT%H:%M:%S')
            """
            self.__flights.append(Flight(flight_id, airline_id, destination, departure_time, arrival_time))

    def get_airline(self, airline_id):
        try:
            for airline in self.__airlines:
                if airline.id == airline_id:
                    return airline
            raise AirlineIDNotFoundException(airline_id)
        except AirlineIDNotFoundException as e:
            print(e)

    def get_flight(self, flight_id):
        try:
            for flight in self.__flights:
                if flight.id == flight_id:
                    return flight
            raise FlightIDNotFoundException(flight_id)
        except FlightIDNotFoundException as e:
            print(e)

    def get_airline_by_index(self, index):
        try:
            return self.__airlines[index]
        except IndexError:
            print("Index out of range")
    """
    def get_airline_index(self, airline_id):
        for i in range(len(self.__airlines)):
            if airline_id == self.__airlines[i].id:
                return i
    
    def get_flight_index(self, flight_id):
        for i in range(len(self.__flights)):
            if flight_id == self.__flights[i].id:
                return i
    """
    def get_flight_by_index(self, index):
        try:
            return self.__flights[index]
        except IndexError:
            print("Index out of range")

    def count_airlines(self):
        return len(self.__airlines)

    def count_flights(self):
        return len(self.__flights)

    def add_airline(self, airline_id, name):
        try:
            for airline in self.__airlines:
                if airline.id == airline_id:
                    raise AirlineIDExistsException(airline_id)
            airline = Airline(airline_id, name)
            self.__airlines.append(airline)
            return True
        except AirlineIDExistsException as e:
            print(e)
        except EnterAirlineIDException as e:
            print(e)

    def def_flights_for_airline(self, airline_id):
        flights = []
        for flight in self.__flights:
            if flight.airline == airline_id:
                flights.append(flight)
        return flights

    def delete_flight(self, flight_id):
        flight = self.get_flight(flight_id)
        if flight:
            self.__flights.remove(flight)
            return True

    def delete_airline(self, airline_id):
        airline = self.get_airline(airline_id)
        if airline:
            self.__airlines.remove(airline)
            flights = self.def_flights_for_airline(airline_id)
            for flight in flights:
                self.__flights.remove(flight)
            return True
        else:
            return False

    def add_flight(self, flight_id, airline_id, destination, departure_time, arrival_time):
        try:
            for flight in self.__flights:
                if flight.id == flight_id:
                    raise FlightIDExistsException(flight_id)
            if self.get_airline(airline_id):
                flight = Flight(flight_id, airline_id, destination, departure_time, arrival_time)
                self.__flights.append(flight)
                return True
        except FlightIDExistsException as e:
            print(e)
        except AirlineIDNotFoundException as e:
            print(e)
        except EnterFlightIDException as e:
            print(e)

    def print_flights(self):
        i = 1
        for flight in self.__flights:
            print(f'Flight # {i}')
            print(flight)
            i += 1

    def print_airlines(self):
        i = 1
        for airline in self.__airlines:
            print(f'Airline # {i}')
            print(airline)
            i += 1

    def print_flights_for_airline(self, airline_id):
        flights_copy = self.__flights
        self.__flights = self.def_flights_for_airline(airline_id)
        self.print_flights()
        self.__flights = flights_copy

    def edit_airline(self, airline_id, name):
        airline_to_edit = self.get_airline(airline_id)

        if airline_to_edit:
            airline_to_edit.airline_name = name
            self.__airlines[self.__airlines.index(airline_to_edit)] = airline_to_edit
            return True
        else:
            return False

    def edit_flight(self, flight_id, airline_id=None, destination=None, departure_time=None, arrival_time=None):
        flight_to_edit = self.get_flight(flight_id)

        if flight_to_edit:
            if airline_id is not None:
                try:
                    if self.get_airline(airline_id) is not None:
                        flight_to_edit.airline = airline_id
                except AirlineIDNotFoundException as e:
                    print(e)
            if destination is not None:
                flight_to_edit.destination = destination
            if departure_time is not None:
                flight_to_edit.departure_time = departure_time
            if arrival_time is not None:
                flight_to_edit.arrival_time = arrival_time
            self.__flights[self.__flights.index(flight_to_edit)] = flight_to_edit
            return True
        else:
            return False

    def search_airline(self, airline_id=None, name=None):
        if airline_id is not None:
            return self.get_airline(airline_id)
        if name is not None:
            airlines = []
            for airline in self.__airlines:
                if airline.airline_name == name:
                    airlines.append(airline)
            return airlines

    def search_flight(self, flight_id=None, airline_id=None, destination=None, departure_time=None, arrival_time=None):
        if flight_id is not None:
            return self.get_flight(flight_id)
        if airline_id is not None:
            airline = self.get_airline(airline_id)
            return self.def_flights_for_airline(airline_id)
        flights = []
        if destination is not None:
            for flight in self.__flights:
                if flight.destination == destination:
                    flights.append(flight)
        if departure_time is not None:
            for flight in self.__flights:
                if flight.departure_time == departure_time:
                    flights.append(flight)
        if arrival_time is not None:
            for flight in self.__flights:
                if flight.arrival_time == arrival_time:
                    flights.append(flight)
        return flights

    def save_to_file(self, filename=None):
        if filename is None:
            filename = self.__xml_path

        doc = minidom.Document()

        root = doc.createElement('Airport')
        doc.appendChild(root)

        for airline in self.__airlines:
            airline_element = doc.createElement('Airline')
            airline_element.setAttribute('id', str(airline.id))
            airline_element.setAttribute('name', airline.airline_name)
            root.appendChild(airline_element)

        for flight in self.__flights:
            flight_element = doc.createElement('Flight')
            flight_element.setAttribute('id', str(flight.id))
            flight_element.setAttribute('airline_id', str(flight.airline))
            flight_element.setAttribute('destination', flight.destination)
            flight_element.setAttribute('departure_time', flight.departure_time)
            flight_element.setAttribute('arrival_time', flight.arrival_time)
            root.appendChild(flight_element)

        try:
            existing_tree = minidom.parse(filename)
            existing_root = existing_tree.documentElement

            for child in existing_root.getElementsByTagName('Airline'):
                existing_root.removeChild(child)
            for child in existing_root.getElementsByTagName('Flight'):
                existing_root.removeChild(child)

            for child in existing_root.childNodes:
                root.appendChild(child)
        except FileNotFoundError:
            print("File not found")

        with open(filename, "w") as file:
            doc.writexml(file, indent="\n", addindent="\t")