FROM python:3.11

WORKDIR opt/api_tests

RUN pip install --no-cache-dir pytest requests jsonschema

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

CMD ["pytest", "test.py"]