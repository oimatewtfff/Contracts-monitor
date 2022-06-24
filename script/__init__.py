import signal
import psycopg2
import requests
import lxml
from time import sleep
from psycopg2 import OperationalError, Error
from bs4 import BeautifulSoup
from config import *
from querys import *
from googleAPI import *


def current_rate(url) -> float:
    """
    Парсинг страницы с курсами валют на текущую дату
    """
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    valute = soup.find('valute', id='R01235')  # тег с данными о курсе доллара
    return float(valute.find('value').get_text().replace(',', '.'))
    # получил значение из тега value, заменил запятую на точку и преобразовал в float


def create_connection(name, user, password, host, port) -> object:
    """
    Подключение к базе данных с параметрами заданными в config.py
    """
    connection = None
    try:
        connection = psycopg2.connect(
            database=name,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(
            f"The error '{e}' occurred")
    return connection


def execute_query(connection, query) -> None:
    """
    Выполнение SQL запроса
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


if __name__ == '__main__':

    con = create_connection(
        db_name, db_user, db_password, db_host, db_port
    )

    signal.signal(signal.SIGINT, signal_handler)

    interrupted = False
    print("Use CTRL-C to exit")
    while True:
        print("Updating the database...")
        execute_query(con, create_test_table)
        execute_query(con, clear_all_rows)
        execute_query(con, create_query())
        sleep(10)
        print("Database update completed!")

        if interrupted:
            print("Script execution interrupted")
            break
