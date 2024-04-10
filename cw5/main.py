from fleet.ambulance import Ambulance
from operations import *
from personnel import *
from fleet.station import Station
import time


def run_application():

    #deklarowanie danych
    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance("Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])
    employee1 = Employee("John", "Doe", 12000.0)
    employee2 = Employee("Jane", "Smith", 8000.0)
    driver1 = Driver("Mike", "Johnson", 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 11500.0, "DL12346", ["ALS", "PHTLS"])

    #zad1
    print(ambulance1.id)
    print(ambulance2.id)
    print(employee1.employee_id)
    print(employee2.employee_id)
    print(driver1.employee_id)
    print(driver2.employee_id)

    #zad2
    queue = IncidentQueue()
    incident1 = Incident("Power outage in sector 4", 3, 'Jan Janowski', (30.095340, 19.920282))
    incident2 = Incident("Fire alarm in building 21", 2, 'Adam Adamski', (56.095340, 28.920282))
    queue += incident1
    queue += incident2
    print(incident1.id)
    print(incident2.id)

    #zad3
    station1=Station((50.095340, 18.920282), ambulance1, driver1, employee1)
    station1.check_ambulance()

    #zad4
    ambulance1.show_status()
    incident1.send_ambulance(ambulance1)
    ambulance1.show_status()
    incident1.send_ambulance(ambulance2)
    ambulance2.show_status()
    #a
    incident1.show_priority()
    print(incident1.time)
    time.sleep(20)
    incident1.time_since_incident()
    #b
    ambulance1.show_status()
    #c
    ambulance1.distance_to_incident(incident2)

if __name__ == "__main__":
    run_application()