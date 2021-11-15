FROM python:3.7.6-slim

WORKDIR /srv/petvet

# Install dependencies only if they changed (leverage Docker layers)
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY clinic .

# Prepare entrypoint script, make sure it's executable
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]

# We need to listen on all networks interfaces to be able to connect from outside of the container
CMD ["gunicorn", "-b", "0.0.0.0:8000", "clinic.wsgi"]
