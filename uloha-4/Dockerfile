FROM python:3.7.6-slim

WORKDIR /app

# Install dependencies only if they changed (leverage Docker layers)
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY czechitas .

# Flush buffer after every printed message
ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
