# PetVet

Výuková aplikace pro DevOps workshop.

# Zadání - Úloha 4

Doposud jsme image a kontejner vytvářeli příkazem `docker`.

V této úloze si vyzkoušíme práci s nástrojem `docker-compose`.

Připravte soubor `docker-compose.yml` tak, aby bylo možné aplikaci nastartovat přes `docker-compose up`, podobně jako dříve příkazem `docker run`.

# Databáze

Defaultně aplikace používá SQLite databázi. Jinou DB je možné využít nastavením proměnných prostředí:

- `DB_ENGINE` (Např. `django.db.backends.sqlite3`)
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
