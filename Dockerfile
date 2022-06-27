FROM python:3.7.13-slim

WORKDIR /srv/petvet

# Install dependencies only if they changed (leverage Docker layers)
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY clinic .

# Prepare entrypoint script
COPY docker-entrypoint.sh .
ENTRYPOINT ["./docker-entrypoint.sh"]

# We need to listen on all networks interfaces to be able to connect from outside of the container
CMD ["gunicorn", "-b", "0.0.0.0:8000", "clinic.wsgi"]

# Tell users on which port the container listens
EXPOSE 8000
