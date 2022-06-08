# Řešení úlohy 4

1. V adresáři `uloha-4` upravíme existující soubor `docker-compose.yml` tak, aby obsahoval `volumes:`:

   ```yml
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
   docker compose up -d
   ```

3. Spustíme požadované příkazy v běžícím kontejneru aplikace:

   ```
   docker compose exec app python manage.py migrate
   docker compose exec app python manage.py createsuperuser
   ```

4. Otevřeme stránku `http://localhost:8000/nasi-veterinari/` a zkontrolujeme, že obsahuje seznam veterinářů načítaný z databáze a že nezobrazuje chybu.

5. Otevřeme administraci aplikace na `http://localhost:8000/admin/` a přihlásíme se uživatelem, kterého jsme dříve vytvořili příkazem `createsuperuser`.

6. Zastavíme a odstraníme všechny kontejnery služeb:

   ```
   docker compose down
   ```

7. Znovu vytovříme kontejnery služeb (na pozadí):

   ```
   docker compose up -d
   ```

8. Ověříme, že data přežila odstranění kontejneru s databází, např. opětovnou kontrolou zobrazení seznamu veterinářů: `http://localhost:8000/nasi-veterinari/`
