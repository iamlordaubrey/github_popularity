from pydantic.main import BaseModel


class ResponseSchema(BaseModel):
    repo: str | None = None
    score: int | None = None
    message: str | None = None
