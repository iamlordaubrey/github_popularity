from pathlib import Path

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.settings import settings
from app.schemas.form_schema import RepositoryURLSchema
from app.utils.validators import url_validator

router = APIRouter()
templates = Jinja2Templates(directory=Path(settings.root_dir, "templates"))


@router.get('/', response_class=HTMLResponse)
def index(request: Request):
    """
    Display the input field and submit button
    :param request: N/A
    :return: Renders a page
    """
    return templates.TemplateResponse('index.html', {'request': request})


@router.post('/', response_class=HTMLResponse)
def index(request: Request, repository: RepositoryURLSchema = Depends(RepositoryURLSchema.as_form)):
    """
    Makes a POST request with a GitHub repository link
    :param request:
    :param repository: A GitHub repository link
    :return: Renders a page with the repository's popularity status
    """
    errors = {}
    response = 'Placeholder'
    if not url_validator(repository.url):
        errors['invalid_url'] = f'The URL {repository.url} is invalid. Sample URL: https://github.com/vuejs/vue'

    context = {'request': request, 'response': response, 'errors': errors}
    return templates.TemplateResponse('index.html', context)
