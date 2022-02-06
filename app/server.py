from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from uvicorn import Server, Config

from app.routers import main, health_check
from app.settings import settings

app = FastAPI()

app.include_router(main.router)
app.include_router(health_check.router)

app.mount('/static', StaticFiles(directory=Path(settings.root_dir, "static")), name='static')


if __name__ == '__main__':
    server = Server(
        Config(
            'server:app',
            host='0.0.0.0',
            port=int(settings.port),
            log_level=settings.log_level.lower(),
        )
    )
    server.run()
