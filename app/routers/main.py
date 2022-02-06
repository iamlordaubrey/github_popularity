import httpx

from pathlib import Path

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.settings import settings
from app.schemas.form_schema import URLSchema
from app.utils.helpers import validate_url, calculate_score, validate_operands

router = APIRouter()
templates = Jinja2Templates(directory=Path(settings.root_dir, "templates"))

# ToDo: Move to constants folder?
GITHUB_CLIENT_ID='60085f3d56fdc34bb6b4'
GITHUB_CLIENT_SECRET='c44fc16a990319b3632c708be48c528faa8b55de'
ACCESS_TOKEN = 'https://github.com/login/oauth/access_token'
GET_REPO_URL = 'https://api.github.com/repos'


@router.get('/', response_class=HTMLResponse)
def index(request: Request):
    """
    Display the input field and submit button
    :param request: N/A
    :return: Renders a page
    """
    return templates.TemplateResponse('index.html', {'request': request})


@router.post('/', response_class=HTMLResponse)
async def index(request: Request, repository: URLSchema = Depends(URLSchema.as_form)):
    """
    Makes a POST request with a GitHub repository link
    :param request:
    :param repository: A GitHub repository link
    :return: Renders a page with the repository's popularity status
    """
    errors = {}
    response = {'repo': None, 'score': None, 'message': None}
    context = {'request': request, 'response': response, 'errors': errors}

    repository_url = repository.url
    is_url_valid, owner_repo = validate_url(repository_url)

    if not is_url_valid:
        errors['invalid_url'] = f'The URL {repository.url} is invalid. Sample URL: https://github.com/vuejs/vue'
        # ToDo: Log errors
        return templates.TemplateResponse('index.html', context)

    response['repo'] = owner_repo[1]  # ToDo: Create a response schema

    async with httpx.AsyncClient() as client:
        raw_response = await client.get(f'{GET_REPO_URL}/{owner_repo[0]}/{owner_repo[1]}')

    if raw_response.status_code != 200:
        errors['invalid_response'] = 'Call to GitHub API failed: An error occurred'
        # ToDo: Add logs with status_code, reason: {raw_response.reason_phrase}
        return templates.TemplateResponse('index.html', context)

    json_response = raw_response.json()
    num_stars = json_response.get('watchers')
    num_forks = json_response.get('forks')

    if not validate_operands((num_stars, num_forks)):
        errors['invalid_response'] = 'Cannot compute popularity'
        return templates.TemplateResponse('index.html', context)

    score, message = calculate_score(num_stars, num_forks)
    response['score'] = score
    response['message'] = message

    return templates.TemplateResponse('index.html', context)
