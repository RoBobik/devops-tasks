# Řešení úloh

## Úloha 1

Pouze postupujeme podle kroků v `README.md`

## Úloha 2

1. V adresáři `uloha-2` vytvoříme soubor `Dockerfile`:

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

2. Provedeme build image (musíme být v adresáři `uloha-2`):

   ```
   docker build -t uloha-2 .
   ```

3. Vytvoříme a spustíme kontejner na pozadí:

   ```
   docker run -d --rm -p 8000:8000 --name app-2 uloha-2
   ```

4. Spustíme požadované příkazy v běžícím kontejneru:

   ```
   docker exec app-2 python manage.py migrate
   docker exec -it app-2 python manage.py createsuperuser
   ```

5. Otevřeme stránku `http://localhost:8000/nasi-veterinari/` a zkontrolujeme, že obsahuje seznam veterinářů načítaný z databáze a že nezobrazuje chybu.

6. Otevřeme administraci aplikace na `http://localhost:8000/admin/` a přihlásíme se uživatelem, kterého jsme dříve vytvořili příkazem `createsuperuser`.

7. Zastavíme kontejner s aplikací: (Docker ho sám navíc odstraní, protože jsme použili parametr `--rm`.)

   ```
   docker stop app-2
   ```

## Úloha 3

1. V adresáři `uloha-3` vytvoříme soubor `docker-compose.yml`:

   ```yml
   version: "3"

   services:
   app:
     build: .
     ports:
       - 8000:8000
     environment:
       - DB_ENGINE=django.db.backends.postgresql
       - DB_NAME=petvet
       - DB_USER=petvet
       - DB_PASSWORD=petvet
       - DB_HOST=db
       - DB_PORT=5432
   db:
     image: postgres
     environment:
       - POSTGRES_USER=petvet
       - POSTGRES_DB=petvet
       - POSTGRES_PASSWORD=petvet
   ```

2. Z adresáře `uloha-3` spustíme služby aplikace (`app`) a databáze (`db`) na pozadí:

   ```
   docker-compose up -d
   ```

3. Může se stát, že aplikace naběhne dříve než databáze. Za normálních okolností by na to měla aplikace umět zareagovat a buď se pokusit o připojení znovu nebo skončit. Zde bohužel vývojář pochybil, nic z toho se neděje a aplikace se zasekne, ale nespadne. Proto pár sekund po prvním spuštění aplikaci restartujeme: (A následně vývojáři chybu nahlásíme :)

   ```
   docker-compose restart app
   ```

4. Spustíme požadované příkazy v běžícím kontejneru aplikace:

   ```
   docker-compose exec app python manage.py migrate
   docker-compose exec app python manage.py createsuperuser
   ```

5. Otevřeme stránku `http://localhost:8000/nasi-veterinari/` a zkontrolujeme, že obsahuje seznam veterinářů načítaný z databáze a že nezobrazuje chybu.

6. Otevřeme administraci aplikace na `http://localhost:8000/admin/` a přihlásíme se uživatelem, kterého jsme dříve vytvořili příkazem `createsuperuser`.

7. Zastavíme a odstraníme všechny kontejnery služeb:

   ```
   docker-compose down
   ```

## Úloha 4

1. V adresáři `uloha-4` upravíme existující soubor `docker-compose.yml` tak, aby obsahoval:

   ```yml
   version: "3"

   services:
   app:
     build: .
     ports:
       - 8000:8000
     environment:
       - DB_ENGINE=django.db.backends.postgresql
       - DB_NAME=petvet
       - DB_USER=petvet
       - DB_PASSWORD=petvet
       - DB_HOST=db
       - DB_PORT=5432
   db:
     image: postgres
     environment:
       - POSTGRES_USER=petvet
       - POSTGRES_DB=petvet
       - POSTGRES_PASSWORD=petvet
     volumes:
       - data:/var/lib/postgresql/data

   volumes:
   data:
   ```

2. Z adresáře `uloha-4` spustíme služby aplikace (`app`) a databáze (`db`) na pozadí:

   ```
   docker-compose up -d
   ```

3. Může se stát, že aplikace naběhne dříve než databáze. Za normálních okolností by na to měla aplikace umět zareagovat a buď se pokusit o připojení znovu nebo skončit. Zde bohužel vývojář pochybil, nic z toho se neděje a aplikace se zasekne, ale nespadne. Proto pár sekund po prvním spuštění aplikaci restartujeme: (A následně vývojáři chybu nahlásíme :)

   ```
   docker-compose restart app
   ```

4. Spustíme požadované příkazy v běžícím kontejneru aplikace:

   ```
   docker-compose exec app python manage.py migrate
   docker-compose exec app python manage.py createsuperuser
   ```

5. Otevřeme stránku `http://localhost:8000/nasi-veterinari/` a zkontrolujeme, že obsahuje seznam veterinářů načítaný z databáze a že nezobrazuje chybu.

6. Otevřeme administraci aplikace na `http://localhost:8000/admin/` a přihlásíme se uživatelem, kterého jsme dříve vytvořili příkazem `createsuperuser`.

7. Zastavíme a odstraníme všechny kontejnery služeb:

   ```
   docker-compose down
   ```

8. Znovu vytovříme kontejnery služeb

   ```
   docker-compose up -d
   ```

9. Ověříme, že data přežila odstranění kontejneru s databází, např. opětovnou kontrolou zobrazení seznamu veterinářů: `http://localhost:8000/nasi-veterinari/`
