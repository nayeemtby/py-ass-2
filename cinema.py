class Hall:
    def __init__(self, hall_no: str, rows: int, cols: int) -> None:
        self.hall_no = hall_no
        self.__show_list = list[tuple[str, str, str]]()
        self.__rows = rows
        self.__cols = cols
        self.__seats = dict[str, list[tuple[int, int]]]()

    def entry_show(self, id: str, movie_name: str, time: str):
        self.__show_list.append((id, movie_name, time))

    def book_seats(self, id: str, requested_seats: list[tuple[int, int]]):
        for show in self.__show_list:
            if show[0] == id:
                if id not in self.__seats.keys():
                    self.__seats[id] = []
                for seat in requested_seats:
                    if seat[0] >= self.__rows or seat[0] < 1 or seat[1] >= self.__cols or seat[1] < 1:
                        print('Some of the requested seats are invalid')
                        return
                    if seat in self.__seats[id]:
                        print('Some of the requested seats are not available')
                        return
                if id in self.__seats.keys():
                    self.__seats[id].extend(requested_seats)
                else:
                    self.__seats[id] = list(requested_seats)
                print('The requested seats were booked successfully')
                return
        print(f'No show with id "{id}" was found')

    def view_show_list(self):
        if len(self.__show_list) == 0:
            print('No shows are available')
            return
        print('Available shows:')
        for show in self.__show_list:
            print(f'Show ID: {show[0]}')
            print(f'Show name: {show[1]}')
            print(f'Show at: {show[2]}')
            print()

    def view_available_seats(self, id: str):
        bookings = []
        if id in self.__seats.keys():
            bookings = self.__seats[id]

        print(
            '"." Indicates that the seat is available while "#" indicates that it is taken')
        print()

        for i in range(0, self.__rows+1):
            for j in range(0, self.__cols+1):
                if i == 0 and j == 0:
                    print(' \t', end='')
                    continue
                if i == 0:
                    print(f'{j} ', end='')
                    continue
                if j == 0:
                    print(f'{i}\t', end='')
                    continue

                if (i, j) in bookings:
                    print('# ', end='')
                else:
                    print('. ', end='')
            print()


class Star_Cinema:
    def __init__(self) -> None:
        self.__hall_list = list[Hall]()

    def entry_hall(self, hall: Hall):
        self.__hall_list.append(hall)

    @property
    def primaryHall(self):
        if len(self.__hall_list) > 0:
            return self.__hall_list[0]
