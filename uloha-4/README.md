# PetVet

Výuková aplikace pro DevOps workshop.

# Zadání - Úloha 5

V této úloze definujeme v `docker-compose.yml` novou slubu s databází a tu následně propojíme s aplikací.

Zároveň pomocí Docker

# Databáze

Defaultně aplikace používá SQLite databázi. Jinou DB je možné využít nastavením proměnných prostředí:

- `DB_ENGINE` (Např. `django.db.backends.sqlite3`)
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
