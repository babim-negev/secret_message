import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from src.api.settings import Settings, DbSettings

settings = Settings()
db = DbSettings()

db_host = db.db_host
db_port = db.db_port
db_name = db.db_name
db_user = db.db_user
db_password = db.db_password

POSTGRES_URL = settings.db.POSTGRES_URL

engine = create_engine(
    POSTGRES_URL, echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ФУНЦИЦИЯ ДЛЯ ПОДКЛЮЧЕНИЯ
def connect_to_database():
    try:
        connection = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        print("Подключение к базе данных успешно выполнено")
        return connection
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None


# Используйте этот код для тестирования подключения к базе данных
if __name__ == "__main__":
    connection = connect_to_database()

    if connection:
        connection.close()
