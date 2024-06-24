FROM python:3.12.3-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app/

# RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

