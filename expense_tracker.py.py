import sqlite3
from datetime import datetime
from prettytable import from_db_cursor

conn = sqlite3.connect('expenses.db')
c = conn.cursor()


def create():
    c.execute('CREATE TABLE IF NOT EXISTS spending(Date TEXT, spending TEXT, Amount REAL, Total REAL)' )
    conn.commit()


def data_entry():
    date = str(datetime.now().date())
    spending = input('Wetin you go buy?!!: ')
    amount = float(input('How much Wey you spend!!: '))

    c.execute('SELECT sum(Amount) from spending')
    total = c.fetchone() [0]
    if total == None:
        total = amount
    else:
        total += amount
    
    c.execute('INSERT INTO spending VALUES (?, ?, ?, ?)', (date,spending,amount,total))
    conn.commit()
def view_data():
    c.execute('SELECT * FROM spending')
    print(from_db_cursor(c))

def delete_data():
    spending = input('Enter the ROW ID (name of expense) to delete your desired expense: ').lower()
    c.execute('SELECT Amount from spending WHERE spending = ?',(spending,))
    temp = c.fetchone()
    c.execute('DELETE FROM spending WHERE spending = ?',(spending,))
    c.execute('UPDATE spending SET Total = Total - ? WHERE spending > ?',(temp[0],spending))
    conn.commit()

while True:
    try:
        entry = int(input('Choose your desired category by Entering any number between 1 to 4 \n\n1. Add Expense \n2. View data \n3. Delete Data \n4. Exit \n\nInput: '))

        if entry == 1:
            data_entry()
        if entry == 2:
            view_data()
        if entry == 3:
            delete_data()
        if entry >=5:
            print('Invalid Input Entered, Try Again Ode!!!')
        if entry == 4:
            break
    except:
        print('invalid parameter entered, Try again senior man!!!')


