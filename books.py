import time

def add_book(library):
    nameb = input("What is the name of the book: ")
    for i in library:
        if nameb.lower() == i['name'].lower():
            print('this book already exists! ')
            time.sleep(2)
            return
        
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


def find_book(library):
    if not library:
        print('\n The library is empty ')
        time.sleep(1)
        return
    found = False
    while not found:
        u_input = input('Enter the title of the book (enter quitx for quit): ').strip()
        if u_input.lower() == 'quitx':
            break
        if not u_input:
            print('Enter title of the book')
            continue
        else:
            try:
                for count, i in enumerate(library, start=1):
                    if u_input.lower() == i['name'].lower():
                        print(f'''
Search results:
The name of your book: {i['name']}
There are {i['page']} pages in searched book
The book has {'not ' if i['already read'].lower() == 'no' else ''}been read before
''')
                        found = True
                        time.sleep(3)
                        break
            except KeyError as e:
                print(f"Data error: missing key {e} in a book entry.")
                return

        if not found:
            print('Book not found in library!')
            time.sleep(1)

    input('\n Press enter key to continue')


def del_book(library):
    if not library:
        print("Library is empty! ")
        time.sleep(1)
        return
    Found = False
    while not Found:
        book = input("Enter the title of the book to be deleted: (enter quitx to quit) ")
        if book.lower() == 'quitx':
            break
        elif not book:
            print('Enter title of the book')
            continue
        else:
            for index, i in enumerate(library):
                if i['name'].lower() == book.lower():
                    library.pop(index)
                    print(f"{book} was removed successfully!")
                    Found = True
                    time.sleep(1)
                    break
        if not Found:
            print(f"There is no book named {book}.")
            break
    
    input('Press any key to continue')


def con_book(library):
    if not library:
        print("Your library is empty!")
        time.sleep(1)
        return
    found = False
    while not found:
        book = input('Enter the title of the book: (enter quitx for quit) ')
        if book.lower == 'quitx':
            break
        elif not book:
            print('Enter title of the book')
            continue
        else:
            for n, i in enumerate(library):
                if i['name'].lower() == book.lower():
                    found = True
                    while True:
                        read = input('Did you read this book? ')
                        if not read:
                            print('please enter something')
                            continue
                        elif read.lower() in ['yes', 'no']:
                            library[n]['already read'] = read.lower()
                            print('Your book succesfully updated')
                            break
                        else:
                            print('Please enter valid input! (yes or no) ')
                            continue
                    break
    if not found:
        print("Book isn't found in your library")
    input('press enter key to countinue')      


def main():
    library = []

    while True:
        print('''
    Welcome to book list app please choose the process
    press 1 for adding book to your library
    press 2 for listing books in your library
    press 3 for search book in library
    press 4 for deleting book from library
    press 5 for configuring your library
    click 0 to quit
        ''')
        try:
            uinput = int(input('    '))
            if uinput == 1:
                add_book(library)
            elif uinput == 2:
                list_book(library)
                input(f'\n Press enter key to contunie ')
            elif uinput == 3:
                find_book(library)
            elif uinput == 4:
                del_book(library)
            elif uinput == 5:
                con_book(library)
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