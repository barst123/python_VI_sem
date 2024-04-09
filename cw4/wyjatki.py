class ReservationError(Exception):
    pass

class CancelError(Exception):
    pass

class ScreeningRoom:
    def __init__(self, row, column):
        self.column=column
        self.row=row
        self.room=[]
        self.empty_seats=row*column
        self.name_seats=[]

    def create_room(self):
        self.room=[[col+1 for col in range(self.column)] for row in range(self.row)]
        self.name_seats=[[col+1 for col in range(self.column)] for row in range(self.row)]

    def room_schema(self):
        print(self.room)
    
    def name_schema(self):
        print(self.name_seats)
    
    def check_name(self, seat_name):
        for i in range(self.row):
            for j in range(self.column):
                if self.name_seats[i][j]==seat_name:
                    raise ReservationError('Uzytkownik ma zarezerwowane miejsce')

    def check_name_res(self, seat_name, row_res, col_res):
        if self.name_seats[row_res-1][col_res-1]!=seat_name:
            raise CancelError('Uzytkownik nie ma zarezerwowanego tego miejsca')
                                
    def check_empty(self):
        if self.empty_seats==0:
            raise ReservationError('Brak miejsc')
    
    def check_seat(self, row_res, col_res):
        if self.room[row_res-1][col_res-1]=='X':
            raise ReservationError('Miejsce zarezerwowane')
    
    def check_seat_res(self, row_res, col_res):
        if self.room[row_res-1][col_res-1]!='X':
            raise CancelError('Uzytkownik nie ma zarezerwowanego tego miejsca')
    
    def reserve_seat(self, row_res, col_res, seat_name):
        self.room[row_res-1][col_res-1]='X'
        self.empty_seats-=1
        self.name_seats[row_res-1][col_res-1]=seat_name

    def reserve(self):
        name=str(input('Podaj imie: '))
        surname=str(input('Podaj nazwisko: '))
        seat_name=name+surname
        try:
            self.check_name(seat_name)
        except ReservationError as error1:
            print(str(error1))
            return
        try:
            self.check_empty()
        except ReservationError as error2:
            print(str(error2))
            return
        
        row_res=int(input('Wybierz rzad: '))
        col_res=int(input('Wybierz miejsce: '))

        try:
            self.check_seat(row_res, col_res)
        except ReservationError as error3:
            print(str(error3))
            return
        
        self.reserve_seat(row_res, col_res, seat_name)
        print('Zarezerwowano miejsce')

    def cancel_res(self):
        name=str(input('Podaj imie: '))
        surname=str(input('Podaj nazwisko: '))
        row_res=int(input('Wybierz rzad: '))
        col_res=int(input('Wybierz miejsce: '))
        seat_name=name+surname
        
        try:
            self.check_seat_res(row_res, col_res)
        except CancelError as error1:
            print(str(error1))
            return
        
        try:
            self.check_name_res(seat_name, row_res, col_res)
        except CancelError as error2:
            print(str(error2))
            return
        
        self.room[row_res-1][col_res-1]=col_res
        print('Anulowano rezerwacje')
        


cinema=ScreeningRoom(5, 5)
cinema.create_room()

cinema.room_schema()
cinema.reserve()
cinema.room_schema()
cinema.reserve()
cinema.room_schema()
cinema.cancel_res()
cinema.room_schema()