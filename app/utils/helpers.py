from typing import Tuple, List, Iterable

from app.constants import GITHUB_BASE_URLS
from app.enums import Message


def validate_url(url: str) -> Tuple[bool, List | None]:
    if any(github_url in url for github_url in GITHUB_BASE_URLS):
        owner_repo = url.split('/')[-2:]

        red_flags = [*GITHUB_BASE_URLS, '']

        if len(owner_repo) == 2 and set(owner_repo).isdisjoint(red_flags):
            return True, owner_repo

    return False, None


def validate_operands(operands: Iterable[int]) -> bool:
    if any(type(variable) != int for variable in operands):
        return False

    return True


def calculate_score(num_stars: int, num_forks: int) -> Tuple:
    score = (num_stars * 1) + (num_forks * 2)

    message = Message.UNPOPULAR.value
    if score >= 500:
        message = Message.POPULAR.value

    return score, message
