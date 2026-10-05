class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = (max_passengers)
        self.current_passengers = []

    def add_passenger(self, person):
        if len(self.current_passengers) < self.max_passengers:
            self.current_passengers.append(person)
            print(f"{person.passenger_name} has been added to the bus.")
        else:
            print(f"The bus is full. {person.passenger_name} cannot be added.")   

    def remove_passenger(self, person):
        if person in self.current_passengers:
            self.current_passengers.remove(person)
            print(f"{person.passenger_name} has been removed from the bus.")
        else:
            print(f"{person.passenger_name} is not on the bus.")
        
class Person:
    def __init__(self, passenger_name):
        self.passenger_name = passenger_name
        
bus1 = Bus(2)
person1 = Person("Carlos")
person2 = Person("Andres")
person3 = Person("Alma")

bus1.add_passenger(person1)
bus1.add_passenger(person2)
bus1.add_passenger(person3)

bus1.remove_passenger(person1)
bus1.remove_passenger(person2)
bus1.remove_passenger(person3)