import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('sample.env')
load_dotenv(dotenv_path=dotenv_path)


class Config:
    def __init__(self) -> None:
        self.api_id: str = os.environ.get("api_id", None)
        self.api_hash: str = os.environ.get("api_hash", None)
        self.session: str = os.environ.get("session", None)
        self.bot_token: str = os.environ.get("bot_token", None)
        

config = Config()
