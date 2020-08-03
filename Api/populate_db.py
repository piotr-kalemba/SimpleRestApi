from .models import Book
from random import choice


first_name = ['Liam',	'Emma', 'Noah',	'Olivia', 'William', 'Ava', 'James',	'Isabella', 'Oliver', 'Sophia']
last_name = ['Murphy', 	'Smith', 'Jones', 	"O'Kelly", 	'Johnson', 'Williams', 	"O'Sullivan", 'Williams', 'Brown',
             'Walsh']
authors = []
titles = []
isbns = []
beginning = ['The story of ', 'The trials and tribulations of ', 'The great ']
tail = '-148410-3'


for _ in range(50):
    author = choice(first_name) + ' ' + choice(last_name)
    title = choice(beginning) + choice(first_name) + ' ' + choice(last_name) + '.'
    isbn = str(choice(range(100, 1000))) + '-' + str(choice(range(10))) + '-' + str(choice(range(10, 100))) + tail
    authors.append(author)
    titles.append(title)
    while isbn in isbns:
        isbn = str(choice(range(100, 1000))) + '-' + str(choice(range(10))) + '-' + str(choice(range(10, 100))) + tail
    isbns.append(isbn)


def return_data():
    data = zip(titles, authors, isbns)
    return data


def populate():
    data = return_data()
    for item in data:
        book = Book.objects.create(title=item[0], author=item[1], isbn=item[2])
        book.save()
