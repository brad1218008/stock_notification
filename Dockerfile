FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install poetry
RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]