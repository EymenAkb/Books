library = [{'Name': '1984', 'Page': 182, 'Already read? ': True},
           {'Name': 'Çocuklar', 'Page': 176, 'Already read? ': False}
           ]

def add_book():
    nameb = input("What is the name of the book: ")
    pageb = (input("How many pages are there: ")) 
    try:
        int(pageb)
    except ValueError:
        print("Please enter a number!")
        exit()

    readb = input("did you read this book (yes / no)").lower()
    if readb in ['yes', 'no']:
        book = {'Name': nameb, 'Page': pageb, 'Already read? ': True if 'yes' else False}
        library.append(book)
        return library
    else:
        print("Please follow the instructions")
        return library

def list_book(library):
    count = 1
    for i in library:
        print(f'\n')
        print(f'{count}' + ':')
        count = count + 1
        print('Name:' + i['Name'])
        print('Page:' + str(i['Page']))
        print('Already read: ' + ('yes' if i['Already read? '] is True else 'no'))


def main():
    while True:
        print('''
            Welcome to book list app please choose the process
            click 1 for adding book
            click 2 for listing book
            click 0 to quit
        ''')
        try:
            uinput = int(input(''))
            if uinput == 1:
                add_book()
            if uinput == 2:
                list_book(library)
            if uinput == 0:
                print('Have a great day! ')
                break
            else:
                break
        except ValueError:
            print('Please enter a number')
            exit()

if __name__ == '__main__':
    main()