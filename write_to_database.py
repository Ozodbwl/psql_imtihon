import json
from typing import List

import psycopg2
from tabulate import tabulate


def connect():
    return psycopg2.connect(
        database='dvdrental',
        user='postgres',
        password='1234',
        host='localhost',
        port=5432
    )


def insert_data(data: dict):
    data_json = json.dumps(data)
    con = connect()
    cur = con.cursor()
    query = '''
        insert into data_b(data_b) values (%s)
    '''
    values = (data_json,)
    cur.execute(query, values)
    con.commit()


def get_data(age__gte: int, age__lte: int):
    con = connect()
    cur = con.cursor()
    query = '''
            select id,
                   data_b ->> 'name' as name,
                   data_b ->> 'age' as age,
                   data_b ->> 'height' as height,
                   data_b ->> 'weight' as weight
            from data_b
            where (data_b ->> 'age')::int between %s and %s
        '''
    values = (age__gte, age__lte)
    cur.execute(query, values)
    result = cur.fetchall()
    return result


def tabulate_print(arr: List):
    header = ('ID', 'name', 'age', 'height', 'weight')
    table = tabulate(arr, headers=header, tablefmt='grid')
    print(table)


age__gte = int(input("from: "))
age__lte = int(input("to: "))

# f = open('data.json', 'rb')
# data = json.load(f)

try:
    # for line in data:
    #     insert_data(line)
    result = get_data(age__gte, age__lte)
    tabulate_print(result)
except Exception as e:
    print(str(e))
