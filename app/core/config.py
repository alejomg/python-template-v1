# Pydantic Settings

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Definimos las variables y sus tipos (validación automática)
    PROJECT_NAME: str
    DEBUG: bool = False
    DATABASE_URL: str
    SECRET_KEY: str

    # Configuración para leer el archivo .env
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore" # Ignora variables extra en el .env que no estén aquí
    )

# Instanciamos para usarlo en toda la app
settings = Settings()
