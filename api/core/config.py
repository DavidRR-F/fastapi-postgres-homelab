from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    KEYCLOAK_URL: str
    KEYCLOAK_REALM: str
    CLIENT_ID: str
    CLIENT_SECRET: str
    ADMIN_CLIENT_SECRET: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
