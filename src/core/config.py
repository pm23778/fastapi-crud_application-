from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Keep both a full DATABASE_URL and individual DB_* values
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int  

    # Pydantic V2 config
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow"  # extra fields ignore karo
    )

settings = Settings()
