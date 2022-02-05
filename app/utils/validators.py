def url_validator(url: str) -> bool:
    github_base_urls = ['https://github.com', 'http://github.com']

    if any(github_url in url for github_url in github_base_urls):
        return True

    return False
