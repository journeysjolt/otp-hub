from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    env: str = "dev"
    port: int = 8000
    otp_ttl_seconds: int = 300
    otp_provider: str = "console"

    twilio_account_sid: str = ""
    twilio_auth_token: str = ""
    twilio_phone_number: str = ""

    firebase_project_id: str = ""
    firebase_service_account_json: str = ""

    allowed_origins: str = "*"


settings = Settings()
