import httpx
import logging

from pathlib import Path

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.constants import GET_REPO_URL
from app.schemas.response_schema import ResponseSchema
from app.settings import settings
from app.schemas.form_schema import URLSchema
from app.utils.helpers import validate_url, calculate_score, validate_operands

router = APIRouter()
templates = Jinja2Templates(directory=Path(settings.root_dir, "templates"))

logger = logging.getLogger(__name__)
logger.setLevel(settings.log_level)


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
    response = ResponseSchema
    context = {'request': request, 'response': response, 'errors': errors}

    repository_url = repository.url
    is_url_valid, owner_repo = validate_url(repository_url)

    if not is_url_valid:
        errors['invalid_url'] = f'The URL {repository_url} is invalid. Sample URL: https://github.com/vuejs/vue'
        logger.warning('The URL is invalid', extra=dict(
            type='invalid_url',
            url=repository_url,
        ))
        return templates.TemplateResponse('index.html', context, status_code=200)

    response.repo = owner_repo[1]

    async with httpx.AsyncClient() as client:
        raw_response = await client.get(f'{GET_REPO_URL}/{owner_repo[0]}/{owner_repo[1]}')

    if raw_response.status_code != 200:
        errors['invalid_response'] = 'Call to GitHub API failed: An error occurred'
        logger.warning(f'Call to GitHub API failed: {raw_response.reason_phrase}', extra=dict(
            type='invalid_response',
            url=repository_url,
            status_code=raw_response.status_code,
            raw_response=raw_response,
        ))
        return templates.TemplateResponse('index.html', context)

    json_response = raw_response.json()
    num_stars = json_response.get('watchers')
    num_forks = json_response.get('forks')

    if not validate_operands((num_stars, num_forks)):
        errors['invalid_response'] = 'Cannot compute popularity'
        logger.warning('Cannot compute popularity', extra=dict(
            type='invalid_response',
            url=repository_url,
            num_stars=num_stars,
            num_forks=num_forks,
            raw_response=raw_response,
        ))
        return templates.TemplateResponse('index.html', context)

    score, message = calculate_score(num_stars, num_forks)
    response.score = score
    response.message = message

    logger.info('Popularity score compute successful', extra=dict(
        type='compute_success',
        url=repository_url,
        raw_response=raw_response,
        response=response,
    ))
    return templates.TemplateResponse('index.html', context)
