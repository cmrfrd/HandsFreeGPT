from handsfreegpt.server.config import Settings
from handsfreegpt.server.fastapi import FastAPI

settings = Settings()
server = FastAPI(settings)
app = server.app()
