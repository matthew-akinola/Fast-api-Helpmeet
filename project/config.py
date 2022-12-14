"""
This module handles application configurations
"""

from starlette.config import Config
from starlette.datastructures import Secret
from fastapi_mail import ConnectionConfig

config = Config(".env")


api_secret=config("api_secret",  cast=Secret)
TESTING=config("TESTING", cast=bool, default=False)
DEBUG=config("DEBUG", cast=bool, default=False)
LIVE=config("LIVE", cast=bool, default=False)
POSTGRES_USER=config("POSTGRES_USER", cast=Secret)
POSTGRES_PASSWORD=config("POSTGRES_PASSWORD", cast=Secret)
POSTGRES_SERVER=config("POSTGRES_SERVER", cast=Secret)
POSTGRES_PORT=config("POSTGRES_PORT", cast=Secret)
POSTGRES_DB=config("POSTGRES_DB", cast=Secret)
cloud_name=config("cloudinary_name",  cast=Secret)
api_key=config("api_key",  cast=Secret)
DATABASE_URL=config(
    "DATABASE_URL",
    default=f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}",  # noqa
)

SECRET_KEY=config("SECRET_KEY", cast=str)
ALGORITHM=config("ALGORITHM", cast=str)



conf = ConnectionConfig(
    MAIL_USERNAME=config("EMAIL_HOST_USER",cast=str),
    MAIL_PASSWORD=config("EMAIL_HOST_PASSWORD",cast=str),
    MAIL_FROM=config("EMAIL_HOST_USER",cast=str),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="HELPMEET",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)
