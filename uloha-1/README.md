# PetVet

Výuková aplikace pro DevOps workshop.

# Zadání - Úloha 1

Zprovozněte aplikaci dle níže uvedeného postupu a ověřte její základní funkčnost.

# Jak aplikaci zprovoznit

- Nainstalovat Python >= 3.6
- Vytvořit virtuální prostředí Pythonu: `python3 -m venv venv`
- Aktivovat virtuální prostředí:
  - Linux/Mac: `source venv/bin/activate`
  - Windows Cmd: `venv\Scripts\activate.bat`
  - Windows Powershell: `.\venv\Scripts\activate`
- Nainstalovat závislosti: `pip install -r requirements.txt`
- Přejít do projektového podadresáře: `cd czechitas`
- Spustit DB migraci: `python manage.py migrate`
- Vytvořit superuživatele: `python manage.py createsuperuser`
- Spustit server: `python manage.py runserver`

# Databáze

Defaultně aplikace používá SQLite databázi. Jinou DB je možné využít nastavením proměnných prostředí:

- `DB_ENGINE` (Např. `django.db.backends.sqlite3`)
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`