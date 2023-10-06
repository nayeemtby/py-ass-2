from cinema import Star_Cinema, Hall
from counter import Counter


def main():
    hall = Hall('1', 10, 10)
    hall.entry_show('waku', 'SpyxFamily', '07:00 PM')
    hall.entry_show('asian', 'How To American', '10:00 PM')
    cinema = Star_Cinema()
    cinema.entry_hall(hall)
    counter = Counter(cinema)
    counter.serve()


main()
