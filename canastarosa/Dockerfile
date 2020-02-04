FROM python:3.8.0-alpine
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTCODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY . /usr/src/app/
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
