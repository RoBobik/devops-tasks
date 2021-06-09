# Řešení úloh

## Úloha 2

1. V adresáři `uloha-2` vytvoříme soubor `Dockerfile`:

   ```dockerfile
   FROM python:3.7.6-slim

   WORKDIR /app

   # Install dependencies only if they changed (leverage Docker layers)
   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY czechitas .

   # We need to listen on all networks interfaces to be able to connect from outside of the container
   CMD ["gunicorn", "-b", "0.0.0.0:8000", "czechitas.wsgi"]
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
