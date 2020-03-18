# Řešení úloh

## Úloha 2

V adresáři `uloha-2` vytvoříme soubor `Dockerfile`:

```dockerfile
FROM python:3.7.6-slim

WORKDIR /app

# Install dependencies only if they changed (leverage Docker layers)
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY czechitas .

# Flush buffer after every printed message to see all messages
ENV PYTHONUNBUFFERED=1

# We need to listen on all networks interfaces to be able to connect from outside of the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

Provedeme build image:

```
docker build -t uloha-2 .
```

Vytvoříme a spustíme kontejner na pozadí:

```
docker run -d --rm -p 8000:8000 --name app-2 uloha-2
```

Spustíme požadované příkazy v běžícím kontejneru:

```
docker exec app-2 python manage.py migrate
docker exec -it app-2 python manage.py createsuperuser
```

Otevřeme stránku `http://localhost:8000/nasi-veterinari/` a zkontrolujeme, že nezobrazuje chybu.

Otevřeme administraci aplikace na `http://localhost:8000/admin/` a přihlásíme se uživatelem, dříve vytvořeným příkazem `createsuperuser`.

## Úloha 3

## Úloha 4
