import os

class Settings:
    DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:admin@qa:port/user")
