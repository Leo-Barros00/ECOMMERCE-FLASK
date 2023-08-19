from decouple import config

def getDataBaseConnectionString():
    DB_USER = config('DATABASE_USER')
    DB_PASSWORD = config('DATABASE_PASSWORD')
    DB_HOST = config('DATABASE_HOST')
    DB_PORT = config('DATABASE_PORT')
    DB_NAME = config('DATABASE_NAME')

    return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"