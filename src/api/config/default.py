import os

class Settings:
    DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:admin@localhost:5342/user")
    DEBUG = True
