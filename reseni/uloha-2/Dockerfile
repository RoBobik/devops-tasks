FROM python:3.10.5-slim

WORKDIR /app

# Install dependencies only if they changed (leverage Docker layers)
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY czechitas .

# We need to listen on all networks interfaces to be able to connect from outside of the container
CMD ["gunicorn", "-b", "0.0.0.0:8000", "czechitas.wsgi"]
