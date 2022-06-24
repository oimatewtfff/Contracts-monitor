import pygsheets


def get_sheet(service_file, table_name):
    """
    Получение таблицы через GoogleAPI
    """
    google_connect = pygsheets.authorize(service_file=service_file)
    sheet = google_connect.open(table_name)
    wks = sheet[0]
    return wks.get_values(start=(2, 1), end=(100, 4), returnas='matrix')  # пропускаю первую строку с названием столбцов
