# Řešení úloh

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
