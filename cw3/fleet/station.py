class Station:
    __slots__ = ['id', 'location', 'ambulance', 'driver', 'employee']
    __instances_count = 0
    __max_id=1

    def __init__(self, location, ambulance, driver, employee):
        self.id=Station.__max_id
        Station.__max_id+=1
        self.location=location
        self.ambulance=ambulance
        self.driver=driver
        self.employee=employee
        
    def check_ambulance(self):
        if self.location==self.ambulance.location:
            print('Ambulance is here')
        else:
            print('Ambulance is not here')