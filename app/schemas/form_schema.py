from fastapi import Form
from pydantic.main import BaseModel


class RepositoryURLSchema(BaseModel):
    url: str

    @classmethod
    def as_form(cls, url: str = Form(...)):
        return cls(url=url)
