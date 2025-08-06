import sqlite3
import time

conn = sqlite3.connect('Name.db')
cursor = conn.cursor()

def empty_ch():
    cursor.execute('SELECT * FROM library')
    return bool(cursor.fetchall())

def en_con():
    input('Press enter key to continue')

def em_mes():
    print('\nYour library is empty')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS library(
        id INTEGER PRIMARY KEY,
        name TEXT,
        page INTEGER,
        read TEXT
    )
''')

def check_ex(a):
    cursor.execute('SELECT * FROM library WHERE name = ?', (a,))
    if cursor.fetchone():
        print('This book already exists in your library.')
        en_con()
        return None
    return a


def get_name():
    a = input('Please enter the name of the book (press enter to quit): ').strip()
    if a == '':
        print('Quitting')
        en_con()
        return None
    return a.lower()

def get_page():
    while True:
        b = input('Please enter the page of the book (press enter to quit)')
        if b == '':
            print('Quitting')
            en_con()
            return None
        try :
            num = int(b)
            if num == 0:
                print('Please enter a number greater than zero')
                continue
            return num
        except ValueError:
            print('Please enter any number')

def get_read():
    while True:
        c = input('Did you read this book (yes or no only, press enter to quit): ').strip().lower()
        if c == '':
            print('Quitting')
            en_con()
            return None
        elif c == 'yes' or c == 'no':
            return c
        else:
            print('Please enter valid input!')
            continue

def add_book():
    a = get_name()
    a = check_ex(a)
    if a is None:
        return
    b = get_page()
    if b is None:
        return
    c = get_read()
    if c is None:
        return
    cursor.execute('INSERT INTO library (name, page, read) VALUES (?, ?, ?)',
                   (a.lower(), b, c.lower()))
    conn.commit()
    cursor.execute('SELECT * FROM library WHERE name = ?', (a,))
    ab = cursor.fetchone()
    print(f'Your book have successfully added to your library')
    print('\n')
    en_con()

def list_book():
    if not empty_ch():
        em_mes()
        en_con()
        return
    cursor.execute('SELECT * FROM library')
    allb = cursor.fetchall()
    for i in allb:
        a = ('not ' if i[3].lower() == 'no' else '')
        print(f'\nSequence number: {i[0]}\nName of the book: {i[1].title()}\nPage number of the book: {i[2]}\nThe book has {a}been read before')
        time.sleep(0.1)
    print('')
    en_con()

def con_book():
    if not empty_ch():
        em_mes()
        en_con()
        return
    allc = input('Do you wish to change name also? (page and read are not optional, yes / no, leave blank to quit)').lower().strip()
    if allc == '':
        print('Quitting')
        return
    print('Please enter the old name of the book')
    a = get_name()
    if a is None:
        return
    cursor.execute('SELECT * FROM library WHERE name = ?', (a,))
    conf = cursor.fetchone()
    if not conf:
        print(f'There is no book named {a}')
        en_con()
        return
    print('Please enter the new information for the book')
    b = get_page()
    c = get_read()
    if allc == 'no':
        cursor.execute('''
            UPDATE library
            SET page = ?, read = ?
            WHERE name = ?
        ''', (b, c, a))
        conn.commit()
        en_con()

    elif allc == 'yes':
        d = get_name()
        cursor.execute('SELECT * FROM library WHERE name = ?', (d,))

        if cursor.fetchone():
            print('A book with that name already exists.')
            en_con()
            return
        
        cursor.execute('''
            UPDATE library
            SET name = ?, page = ?, read = ?
            WHERE name = ?
        ''', (d, b, c, a))
        conn.commit()
        en_con()

    else:
        en_con()
        return
    
def del_book():
    a = get_name()
    if a == '':
        return
    cursor.execute('SELECT * FROM library WHERE name = ?', (a,))
    if cursor.fetchone():
        while True:
            agree = input(f'Are you sure about deleting book named {a} (yes / no): ').strip().lower()
            if agree == 'yes':
                cursor.execute('DELETE FROM library WHERE name = ?', (a,))
                conn.commit()
                print('Your book has been successfully deleted!')
                en_con()
                return
            elif agree == 'no':
                en_con()
                return
            else:
                print('Please enter valid input!')
                continue
    print(f'There is no book named: {a}')
    en_con()
    return

def find_book():
    if not empty_ch():
        em_mes()
        en_con()
        return
    a = get_name()
    cursor.execute('SELECT * FROM library WHERE name = ?', (a,))
    i = cursor.fetchone()
    if i:
        b = ('not' if i[3].lower() == 'no' else '')
        print(f'\nSequence number: {i[0]}\nName of the book: {i[1].title()}\nPage number of the book: {i[2]}\nThe book has {b} been read before')
        print('')
        en_con()
        return
    print(f'There is no book named {a}\n')
    en_con()
    return


def main():
    while True:
        print('''
Welcome to the Book Library App!
Please choose an option:
1 - Add a book to your library
2 - List all books
3 - Configure your book
4 - Delete your books
5 - Search book by its name
0 - Quit
        ''')
        try:
            uinput = int(input('Your choice: '))
            if uinput == 1:
                add_book()
            elif uinput == 2:
                list_book()
            elif uinput == 3:
                con_book()
            elif uinput == 4:
                del_book()
            elif uinput == 5:
                find_book()
            elif uinput == 0:
                print('Have a great day!')
                break
            else:
                print('Invalid input. Please choose a valid option.')
                time.sleep(1)
        except ValueError:
            print('Please enter a number.')
            time.sleep(1)

if __name__ == '__main__':
    main()