import time

def add_book(library):
    nameb = input("What is the name of the book: ")
    while True:
        pageb = input("How many pages are there: ")
        try:
            pageb = int(pageb)
            break
        except ValueError:
            print("Please enter a number!")
            time.sleep(0.5)

    while True:
        readb = input("did you read this book (yes / no)").lower()
        if readb in ['yes', 'no']:
            book = {'name': nameb, 'page': pageb, 'already read': readb}
            library.append(book)
            return library
        else:
            print("Please follow the instructions")

def list_book(library):
    if not library:
        print('\n Your library is empty')
        time.sleep(1)
    else:
        for count, i in enumerate(library, start=1):
            time.sleep(0.5)
            print(f'\n')
            print(f'{count}' + ':')
            print('Name:' + i['name'])
            print('Page:', i['page'])
            print('Already read: ' + i['already read'])


def main():
    library = []

    while True:
        print('''
    Welcome to book list app please choose the process
    click 1 for adding book
    click 2 for listing book
    click 0 to quit
        ''')
        try:
            uinput = int(input('    '))
            if uinput == 1:
                add_book(library)
            elif uinput == 2:
                list_book(library)
                input(f'\n Press enter key to contunie ')
            elif uinput == 0:
                print('Have a great day! ')
                break
            else:
                print('Please enter valid input!')
                time.sleep(2)
        except ValueError:
            print('Please enter a valid number')
            time.sleep(2)

if __name__ == '__main__':
    main()