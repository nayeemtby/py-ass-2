from cinema import Star_Cinema


class Counter:
    def __init__(self, cinema: Star_Cinema) -> None:
        self.cinema = cinema

    def __showOptions(self):
        print('1. View Available Shows\n2. View Available Seats\n3. Book Tickets\n4.Exit')

    def __viewShows(self):
        hall = self.cinema.primaryHall
        if hall == None:
            print('No shows available')
            return
        hall.view_show_list()
        return

    def __viewSeats(self):
        hall = self.cinema.primaryHall
        if hall == None:
            print('No halls available')
            return
        id = input('Enter Show ID: ')
        hall.view_available_seats(id)

    def __bookTickets(self):
        hall = self.cinema.primaryHall
        if hall == None:
            print('No halls available')
            return
        id = input('Enter Show ID: ')
        count = int(input('Enter the number of tickets: '))
        seats = list[tuple[int, int]]()
        for i in range(count):
            [row, col] = input(
                'Enter seat row and column no separated by space: ').split(' ')
            seats.append((int(row), int(col)))
        hall.book_seats(id, seats)

    def serve(self):
        while True:
            self.__showOptions()
            inp = input('Enter Options: ')
            if inp == '4':
                break
            elif inp == '1':
                print('-------------------------------')
                self.__viewShows()
                print('-------------------------------')
            elif inp == '2':
                print('-------------------------------')
                self.__viewSeats()
                print('-------------------------------')
            elif inp == '3':
                print('-------------------------------')
                self.__bookTickets()
                print('-------------------------------')
            else:
                print('-------------------------------')
                print('Invalid Option')
                print('-------------------------------')
