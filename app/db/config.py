from pydantic_settings import BaseSettings, SettingsConfigDict


# Simple method to use .env file credentials when connecting to the database
class Settings(BaseSettings):

    # Specifing the file that we're getting the credentials from
    model_config = SettingsConfigDict(env_file=".env")

    db_hostname: str
    db_port: str
    db_password: str
    db_name: str
    db_username: str


settings = Settings()  # pyright: ignore
