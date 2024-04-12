from Airport.Airport import Airport
from Airport.Exceptions import EnterIDException


def input_id(text):
    try:
        id = input(text)
        id = int(id)
        if id > 0:
            return id
        else:
            raise EnterIDException(id)
    except ValueError:
        raise EnterIDException(id)


class UI:
    def __init__(self, xml_path):
        self.__airport = Airport(xml_path)

    def menu(self):
        while True:
            print("=== Main Menu ===")
            print("1. Print Airlines")
            print("2. Print Flights")
            print("3. Print Flights for Airline with ID")
            print("4. Add Airline")
            print("5. Add Flight")
            print("6. Delete Airline")
            print("7. Delete Flight")
            print("8. Edit Airline")
            print("9. Edit Flight")
            print("A. Search Airline")
            print("B. Search Flight")
            print("C. Count Airlines")
            print("D. Count Flights")
            print("E. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.print_airlines()
            elif choice == "2":
                self.print_flights()
            elif choice == "3":
                self.print_flights_for_airline()
            elif choice == "4":
                self.add_airline()
            elif choice == "5":
                self.add_flight()
            elif choice == "6":
                self.delete_airline()
            elif choice == "7":
                self.delete_flight()
            elif choice == "8":
                self.edit_airline()
            elif choice == "9":
                self.edit_flight()
            elif choice == "A":
                self.search_airline()
            elif choice == "B":
                self.search_flight()
            elif choice == "C":
                self.count_airlines()
            elif choice == "D":
                self.count_flights()
            elif choice == "E":
                self.exit()
                break
            else:
                print("Invalid choice")
                continue

    def print_airlines(self):
        print("=== Airlines ===")
        self.__airport.print_airlines()

    def print_flights(self):
        print("=== Flights ===")
        self.__airport.print_flights()

    def print_flights_for_airline(self):
        print("=== Flights for Airline with ID ===")
        while True:
            try:
                airline_id = input_id("Enter Airline ID: ")
                airline = self.__airport.get_airline(airline_id)
                if airline:
                    print(airline)
                    self.__airport.print_flights_for_airline(airline_id)
                    break
            except EnterIDException as e:
                print(e)

    def add_airline(self):
        print("=== Add Airline ===")
        while True:
            try:
                airline_id = input_id("Enter Airline ID: ")
                name = input("Enter Airline name: ")
                if self.__airport.add_airline(airline_id, name):
                    print("Airline added successfully")
                    break
            except EnterIDException as e:
                print(e)
                continue

    def add_flight(self):
        print("=== Add Flight ===")
        while True:
            try:
                flight_id = input_id("Enter Flight ID: ")
                airline_id = input_id("Enter Airline ID: ")
                destination = input("Enter Destination: ")
                departure_time = input("Enter Departure time: ")
                arrival_time = input("Enter Arrival time: ")
                if self.__airport.add_flight(flight_id, airline_id, destination, departure_time, arrival_time):
                    print("Flight added successfully")
                    break
            except EnterIDException as e:
                print(e)
                continue

    def delete_airline(self):
        print("=== Delete Airline ===")
        while True:
            try:
                airline_id = input_id("Enter Airline ID: ")
                if self.__airport.delete_airline(airline_id):
                    print("Airline deleted successfully")
                    break
            except EnterIDException as e:
                print(e)
                continue

    def delete_flight(self):
        print("=== Delete Flight ===")
        while True:
            try:
                flight_id = input_id("Enter Flight ID: ")
                if self.__airport.delete_flight(flight_id):
                    print("Flight deleted successfully")
                    break
            except EnterIDException as e:
                print(e)
                continue

    def edit_airline(self):
        print("=== Edit Airline ===")
        while True:
            try:
                airline_id = input_id("Enter Airline ID: ")
                if self.__airport.get_airline(airline_id):
                    while True:
                        print("Select fields to edit: ")
                        print("1. Airline Name")
                        print("2. Back to Main Menu")
                        choice = input("Enter your choice: ")
                        if choice == "1":
                            name = input("Enter new Airline name: ")
                            self.__airport.edit_airline(airline_id, name)
                            print("Airline edited successfully")
                        elif choice == "2":
                            break
                        else:
                            print("Invalid choice")
                            continue
                    break
            except EnterIDException as e:
                print(e)
                continue

    def edit_flight(self):
        print("=== Edit Flight ===")
        while True:
            try:
                flight_id = input_id("Enter Flight ID: ")
                if self.__airport.get_flight(flight_id):
                    while True:
                        print("Select fields to edit: ")
                        print("1. Airline ID")
                        print("2. Destination")
                        print("3. Departure Time")
                        print("4. Arrival Time")
                        print("5. Back to main menu")

                        choice = input("Enter your choice: ")
                        if choice == "1":
                            airline_id = input_id("Enter Airline ID: ")
                            self.__airport.edit_flight(flight_id, airline_id=airline_id)
                        elif choice == "2":
                            destination = input("Enter Destination: ")
                            self.__airport.edit_flight(flight_id, destination=destination)
                        elif choice == "3":
                            departure_time = input("Enter Departure time: ")
                            self.__airport.edit_flight(flight_id, departure_time=departure_time)
                        elif choice == "4":
                            arrival_time = input("Enter Arrival time: ")
                            self.__airport.edit_flight(flight_id, arrival_time=arrival_time)
                        elif choice == "5":
                            break
                        else:
                            continue
                        print("Flight edited successfully")
                        continue
                break
            except EnterIDException as e:
                print(e)
                continue

    def search_airline(self):
        print("=== Search Airline ===")
        while True:
            print("Select fields to search: ")
            print("1. Airline ID")
            print("2. Airline Name")
            choice = input("Enter your choice: ")
            if choice == "1":
                while True:
                    try:
                        airline_id = input_id("Enter Airline ID: ")
                        print(self.__airport.search_airline(airline_id=airline_id))
                        break
                    except EnterIDException as e:
                        print(e)
                break
            elif choice == "2":
                airline_name = input("Enter Airline Name: ")
                airlines = self.__airport.search_airline(name=airline_name)
                if len(airlines) == 0:
                    print("Airline not found")
                else:
                    print(airlines)
                break
            else:
                print("Invalid choice")
                continue

    def search_flight(self):
        print("=== Search Flight ===")
        while True:
            print("Select fields to search: ")
            print("1. Flight ID")
            print("2. Airline ID")
            print("3. Destination")
            print("4. Departure Time")
            print("5. Arrival Time")
            choice = input("Enter your choice: ")
            if choice == "1":
                while True:
                    try:
                        flight_id = input_id("Enter Flight ID: ")
                        print(self.__airport.search_flight(flight_id=flight_id))
                        break
                    except EnterIDException as e:
                        print(e)
                break
            elif choice == "2":
                while True:
                    try:
                        airline_id = input_id("Enter Airline ID: ")
                        flights = self.__airport.search_flight(airline_id=airline_id)
                        if len(flights) == 0:
                            print("Flight not found")
                        else:
                            print(flights)
                        break
                    except EnterIDException as e:
                        print(e)
                break
            elif choice == "3":
                destination = input("Enter Flight Destination: ")
                flights = self.__airport.search_flight(destination=destination)
                if len(flights) == 0:
                    print("Flight not found")
                else:
                    print(flights)
                break
            elif choice == "4":
                departure_time = input("Enter Flight Departure Time: ")
                flights = self.__airport.search_flight(departure_time=departure_time)
                if len(flights) == 0:
                    print("Flight not found")
                else:
                    print(flights)
                break
            elif choice == "5":
                arrival_time = input("Enter Flight Arrival Time: ")
                flights = self.__airport.search_flight(arrival_time=arrival_time)
                if len(flights) == 0:
                    print("Flight not found")
                else:
                    print(flights)
                break
            else:
                print("Invalid choice")
                continue

    def count_airlines(self):
        print("=== Count Airlines ===")
        print("Number of airlines: ", self.__airport.count_airlines())

    def count_flights(self):
        print("=== Count Flights ===")
        print("Number of flights: ", self.__airport.count_flights())

    def exit(self):
        print("=== Exit ===")
        while True:
            print("Do you want to save the changes?")
            print("1. Yes")
            print("2. No")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.__airport.save_to_file()
                break
            elif choice == "2":
                break
            else:
                print("Invalid choice")
                continue
