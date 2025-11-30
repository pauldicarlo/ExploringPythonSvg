'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''


from fastapi import APIRouter, Request
from fastapi.responses import  HTMLResponse
from fastapi.templating import Jinja2Templates


import logging

router = APIRouter()


# TODO: setup better logging using extra(s) and a safe formatter 
# Basic configuration
logging.basicConfig(
    level=logging.INFO,  # Set the minimum level to log
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# Create loggers
logger = logging.getLogger(__name__)

# Create Jinja2 templates instance
# The directory where your template files are located
templates = Jinja2Templates(directory="web/templates")

@router.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    """
    Render the form template when accessing the root path
    """
    return templates.TemplateResponse("sailocus_fastapi.html", {"request": request})
