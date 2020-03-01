# PetVet

Výuková aplikace pro DevOps workshop.

# Zadání - Úloha 2

Vytvořte `Dockerfile`, pomocí kterého automatizujete úvodní kroky a krok spuštění serveru:

- Nainstalovat Python >= 3.6
- Nainstalovat závislosti: `pip install -r requirements.txt`
- Spustit server: `python manage.py runserver`

Následně v běžícím kontejneru proveďte manuálně zbývající příkazy:

- Přejít do projektového podadresáře: `cd czechitas`
- Spustit DB migraci: `python manage.py migrate`
- Vytvořit superuživatele: `python manage.py createsuperuser`

## K zamyšlení

Proč můžeme vynechat tyto následující kroky?

- Vytvořit virtuální prostředí Pythonu: `python3 -m venv venv`
- Aktivovat virtuální prostředí:
  - Linux/Mac: `source venv/bin/activate`
  - Windows Cmd: `venv\Scripts\activate.bat`
  - Windows Powershell: `.\venv\Scripts\activate`

# Databáze

Defaultně aplikace používá SQLite databázi. Jinou DB je možné využít nastavením proměnných prostředí:

- `DB_ENGINE` (Např. `django.db.backends.sqlite3`)
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
