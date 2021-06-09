# Zadání - Úloha 1

Zprovozněte aplikaci dle níže uvedeného postupu a ověřte její základní funkčnost.

## Zprovozněte aplikaci dle návodu

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
- Spustit server: `gunicorn czechitas.wsgi`

## Ověřte funkčnost aplikace

1. Po spuštění serveru otevřete aplikaci na adrese `localhost:8000`.
   - Zobrazí se vám stránka aplikace?
2. V aplikaci otevřete záložku `Naši veterináři`
   - Zobrazí se seznam veterinářů nebo databázová chyba?
   - Pokud vidíte DB chybu, zkontrolujte, zda jste provedli všechny kroky návodu.
3. V aplikaci otevřete záložku **Sjednat schůzku**, vyplňte a odešlete formulář
4. Otevřete stránku `localhost:8000/admin`, přihlaste se jako superuživatel a zkontrolujte, že existuje Schůzka vytvořená v předchozím kroku.
   - Nemůžete se přihlásit? Zkontrolujte, zda jste provedli všehcny kroky dle návodu.

# Už máte hotovo?

1. Zkuste napsat Bash skript, který provede automaticky uvedené příkazy (nebo alespoň jejich část).

2. Příkaz `createsuperuser` je záludnější na automatizaci, protože potřebuje vstup od uživatele. Je ale možné jej spustit i bez nutnosti interaktivního ovládání?

   Spoiler: Je to možné :) Viz https://docs.djangoproject.com/en/3.0/ref/django-admin/#createsuperuser
