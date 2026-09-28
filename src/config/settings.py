from pydantic_settings import BaseSettings , SettingsConfigDict

from pydantic import Field


class Settings(BaseSettings):
    
    embedding_model : str Field(min_length=1,validation_alias='EMBEDDING_MODEL')


    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()