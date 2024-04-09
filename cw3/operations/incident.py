from datetime import datetime
class Incident:
    __slots__ = ['id', 'description', 'priority', 'time', 'call_info', 'ambulance', 'location']
    __instances_count = 0
    __max_id=1
    
    def __init__(self, description, priority, call_info, location):
        self.id = Incident.__max_id
        Incident.__max_id+=1
        self.description = description
        self.priority=priority
        self.time=datetime.now()
        self.call_info=call_info
        self.location=location

    def show_priority(self):
        print(f'Incident {self.id} ({self.description}) priority: {self.priority}')

    def time_since_incident(self):
        print(f'Time since incident {self.id} ({self.description}): {datetime.now()-self.time}')

    def send_ambulance(self, ambulance):
        self.ambulance=ambulance
        if self.ambulance.status=='available':
            self.ambulance.status='on mission'
            print('Ambulance is comming')
        else:
            print('Ambulance is not available')

    def __repr__(self):
        return f"Incident(id={self.id!r}, description={self.description!r}, priority={self.priority!r}, time={self.time!r}, info={self.call_info!r})"

    def __str__(self):
        return f"Incident {self.id}: {self.description}, {self.priority}, {self.time}, {self.call_info}"