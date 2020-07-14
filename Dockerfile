FROM python:3.8

WORKDIR /usr/src/app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

COPY . /usr/src/app

RUN /root/.poetry/bin/poetry install

CMD ["python", "/usr/src/app/contributor_list/main.py"]