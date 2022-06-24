import datetime

creds_file = "state/credentials.json"  # путь к файлу типа service_account для подключения к google sheets API

# Данные для подключения к базе данных
db_name = 'postgres'
db_user = 'postgres'
db_password = '9369'
db_host = 'localhost'
db_port = '5432'

# URL адрес к XML странице ЦБР с курсами валют на текущую дату
crb_url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={datetime.datetime.now().strftime("%d/%m/%Y")}'
