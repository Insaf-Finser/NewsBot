from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    telegram_bot_token: str  = ""
    telegram_chat_id: str = ""
    llm_api_key: str = ""
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")

settings = Settings()