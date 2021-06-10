# Úloha 4

## Cíl

Zajistit trvalé uchování dat Dockerizované databáze pomocí Docker Volume.

## Zadání

Databáze PostgreSQL, která běží ve vlastním kontejneru si ukládá data do adresáře `/var/lib/postgres/data`.

Když je kontejner odstraněn, data jsou ztracena.

Úpravou `docker-compose.yml` přidejte Docker Volume pro výše uvedený adresář, aby po smazání kontejneru s databází a jeho opětovném vytvoření byla data stále k dispozici.

Soubor `Dockerfile` je již přiložen a nepotřebuje další úpravy.

Máte rovněž připravený `docker-compose.yml`, který odpovídá dokončené předchozí úloze.
