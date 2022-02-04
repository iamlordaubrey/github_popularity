FROM python:3.10-slim

COPY requirements.txt /git_pop/requirements.txt
RUN pip3 install -r /git_pop/requirements.txt

WORKDIR /git_pop

COPY .env /git_pop/.env
COPY app /git_pop/app

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--reload"]
