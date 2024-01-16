import os

from dotenv import load_dotenv

# ЗАГРУЖАЕМ ДАННЫЕ ИЗ .ENV
load_dotenv()

# ИЗВЛЕКАЕМ ДАННЫЕ
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")
db_name = os.getenv("POSTGRES_DB")
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")

POSTGRES_URL = "postgresql://" + db_user + ":" + db_password + "@" + db_host + ":" + db_port + "/" + db_name
