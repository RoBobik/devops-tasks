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

3. Vytvoříme a spustíme kontejner:

   ```
   docker run -p 8000:8000 --name app-2 uloha-2
   ```

   Kontejner nyní běží v popředí - vidíme, co aplikace vypisuje na standardní výstup.

4. V jiném terminálovém okně spustíme `docker ps` a podíváme se na jeho výstup. Vidíme, že kontejner s aplikací běží.

5. Stiskem `Ctrl+C` v prvním terminálovém okně aplikaci zastavíme a zkontrolujeme, že není ve výstupu `docker ps`. Také ověříme, že po otevření stránky `http://localhost:8000` se aplikace už nenačte.

6. Vypíšeme si pomocí `docker ps -a` i zastavené kontejnery, kde jej už uvidíme.

7. Existující kontejner znovu nastartujeme (na pozadí): `docker start app-2`.

8. Spustíme požadované příkazy dle původního postutpu (v běžícím kontejneru):

   ```
   docker exec app-2 python manage.py migrate
   docker exec -it app-2 python manage.py createsuperuser
   ```

9. Otevřeme stránku `http://localhost:8000/nasi-veterinari/` a zkontrolujeme, že obsahuje seznam veterinářů načítaný z databáze a že nezobrazuje chybu.

10. Otevřeme administraci aplikace na `http://localhost:8000/admin/` a přihlásíme se uživatelem, kterého jsme dříve vytvořili příkazem `createsuperuser`.

11. Zastavíme kontejner s aplikací, který běží na pozadí a následně ho odstraníme:

    ```
    docker stop app-2
    docker rm app-2
    ```

    Kontejner již není ani ve výstupu `docker ps -a`, protože je smazaný.

12. Znovu kontejner vytvoříme a spustíme, ale tentokrát rovnou na pozadí volbou `-d` (`--detached`):

    ```
    docker run -d -p 8000:8000 --name app-2 uloha-2
    ```

13. Po otřevření aplikace vidíme, že jsme přišli o data, která existovala jen v již smazaném kontejneru: `http://localhost:8000/nasi-veterinari/`

    Uchováním dat se zabývá úloha 4.

14. Kontejner opět zastavíme, abychom předešli konfliktu s další úlohou, a smažeme:
    ```
    docker stop app-2
    docker rm app-2
    ```
