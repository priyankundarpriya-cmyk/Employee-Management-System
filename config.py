import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-key-change-later")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:password@localhost/employee_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
