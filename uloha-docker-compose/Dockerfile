FROM python:3.7.6-slim

WORKDIR /srv/petvet

# Install dependencies only if they changed (leverage Docker layers)
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY clinic clinic

# Flush buffer after every printed message to see all messages
ENV PYTHONUNBUFFERED=1

# Prepare entrypoint script, make sure it's executable
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT [ "./docker-entrypoint.sh" ]

# We need to listen on all networks interfaces to be able to connect from outside of the container
CMD ["python", "clinic/manage.py", "runserver", "0.0.0.0:8000"]
