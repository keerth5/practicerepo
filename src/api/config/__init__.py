import os
from src.api.config import default, local, qa, prod

def get_settings():
    """
    Returns a Settings object populated from the default settings and
    overridden with environment-specific settings from local.py, qa.py, or
    prod.py if they exist.

    The environment is determined by the APP_ENV environment variable, which
    defaults to "local" if not set.

    The settings are loaded as follows:

    1. The default settings are loaded from default.py.
    2. If the environment is "local", the settings are overridden with values
       from local.py if they exist.
    3. If the environment is "qa", the settings are overridden with values
       from qa.py if they exist.
    4. If the environment is "prod", the settings are overridden with values
       from prod.py if they exist.

    The final Settings object is then returned.
    """
    env = os.environ.get("APP_ENV", "local")

    # Load general settings first
    settings = default.Settings()

    # Override settings from environment-specific files if they exist
    if env == "local" and hasattr(local, "Settings"):
        for key, value in local.Settings().__dict__.items():
            if value is not None:
                setattr(settings, key, value)
    elif env == "qa" and hasattr(qa, "Settings"):
        for key, value in qa.Settings().__dict__.items():
            if value is not None:
                setattr(settings, key, value)
    elif env == "prod" and hasattr(prod, "Settings"):
        for key, value in prod.Settings().__dict__.items():
            if value is not None:
                setattr(settings, key, value)

    return settings

settings = get_settings()

# def get_db_connection():
#     """
#     Establishes a connection to the database, using the DATABASE_URL environment
#     variable or the default setting for the current environment.

#     Yields a psycopg2 connection object.
#     """
#     with psycopg2.connect(settings.DATABASE_URL) as conn:
#         yield conn
