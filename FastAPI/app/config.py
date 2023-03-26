from pydantic import BaseSettings

class Setting(BaseSettings):
    database_name: str
    database_user: str
    database_port: int
    database_pwd: str
    database_host: str

    class Config:
        env_file = '.env'

setting = Setting()