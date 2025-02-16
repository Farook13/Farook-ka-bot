import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('17264725', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('e7c6c1e727962d2ade50ba1d7f4fac8a', None)
    BOT_TOKEN = os.environ.get('7955983025:AAFqrIti8CrhCvPTY0IKV2qu4xnxF96sL40', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 17264725
    API_HASH = "e7c6c1e727962d2ade50ba1d7f4fac8a"
    BOT_TOKEN = "7955983025:AAFqrIti8CrhCvPTY0IKV2qu4xnxF96sL40"
    DATABASE_URL = "mongodb+srv://farook:farook@cluster0.dmaou.mongodb.net/"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "StarkBots"
    if MUST_JOIN.startswith("@Faroo_bruh"):
        MUST_JOIN = MUST_JOIN[1:]

DEVS = [1744109441, 1946995626]