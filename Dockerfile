FROM python:3.8

WORKDIR /usr/src/app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"

COPY . /usr/src/app

RUN poetry install

CMD ["poetry", "run", "python", "/usr/src/app/contributor_list/main.py"]