import psycopg2
from tabulate import tabulate


def connect():
    return psycopg2.connect(
        database='farmacy',
        user='postgres',
        password='1234',
        host='localhost',
        port=5432
    )


con = connect()
cur = con.cursor()


def tabulate_print(arr: list):
    header = ('ID', 'P_name', 'Price', 'Amount', 'Date', 'Total_price')
    table = tabulate(arr, headers=header, tablefmt='grid')
    print(table)


def check():
    print('1: January\n2: February\n3: March\n4: April\n5: May\n6: June\n7: July\n8: August\n9: September\n10: '
          'October\n11: November\n12: December\n')
    month = int(input('Enter month: '))
    year = int(input('Enter year: '))
    query1 = f'''SELECT id, p_name, price, amount, time_date, (price * amount) AS total_price
                FROM product1 
                WHERE EXTRACT(MONTH FROM time_date) = {month} and EXTRACT(year FROM time_date) = {year};'''
    cur.execute(query1)
    res1 = cur.fetchall()
    tabulate_print(res1)


check()

cur.close()
con.close()
