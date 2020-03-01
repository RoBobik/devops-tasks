FROM python:3.7.6-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY czechitas .

ENV PYTHONUNBUFFERED=1
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
