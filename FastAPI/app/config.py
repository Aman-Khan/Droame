from pydantic import BaseSettings

class Setting(BaseSettings):
    database_name: str
    database_user: str
    database_port: int
    database_pwd: str
    database_host: str

    secret_key : str
    algorithm: str
    token_expire_time: int
    
    class Config:
        env_file = '.env'

setting = Setting()