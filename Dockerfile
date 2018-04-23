FROM python:3.5-alpine

WORKDIR /app
RUN apk add build-base --update \
    && apk add postgresql-dev
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "manager.py", "runserver"]