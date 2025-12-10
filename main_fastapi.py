'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from web.apis.base import api_router
from web.routers.base import web_router
from web.db.session import createSession, SessionError

class FastApiAppException(Exception):
    def __init__(self, message:str):
        self.message = message
        super().__init__(self.message)



class Config():
    
    def __init__(self):
        self.PROJ_TITLE = "Sailocus"
        self.PROJ_VERSION = "0.0.1"


def start_app() -> FastAPI:
    app = FastAPI(title=settings.PROJ_TITLE, version=settings.PROJ_VERSION)
    include_routers(app)
    return app

def include_routers(app):
    app.include_router(api_router)
    app.include_router(web_router, prefix="", tags=[""], include_in_schema=False)


settings = Config()

try:
    session = createSession()
except SessionError as e:
    raise FastApiAppException(message=f"Failure creating session: {e}")
    

app = start_app()

# This line is crucial!
app.mount("/static", StaticFiles(directory="web/static"), name="static")

# Create Jinja2 templates instance
# The directory where your template files are located
templates = Jinja2Templates(directory="web/templates")


# TODO: Remove
@app.get("/")
def index(request: Request):
    #return {"msg":"Hello.  This is Paul and at least the server is working"}
    context = {"request": request, "name": "FastAPI"}
    return templates.TemplateResponse("index.html", context)