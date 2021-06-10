# Úloha 1

## Cíl

Vyzkoušet si ruční instalaci závislostí a typické spuštění aplikace bez Dockeru.

## Zadání

Zprovozněte aplikaci dle níže uvedeného postupu a ověřte její základní funkčnost.

_Pozor, nezapoměňte se v terminálu přepnout do podadresáře úlohy (`cd uloha-1`)._

1. Zajistit, aby na cílovém počítači byl alespoň Python3 >= 3.6
   - _Tip: aktuální verzi Python3 zjistíte pomocí `python3 -V`_
2. Vytvořit virtuální prostředí Pythonu: `python3 -m venv venv`
3. Aktivovat virtuální prostředí: `source venv/bin/activate`
4. Nainstalovat závislosti: `pip install -r requirements.txt`
5. Přejít do projektového podadresáře: `cd czechitas`
6. Spustit DB migraci: `python manage.py migrate`
7. Vytvořit superuživatele: `python manage.py createsuperuser`
8. Spustit server: `gunicorn czechitas.wsgi`

### Ověřte funkčnost aplikace

1. Po spuštění serveru otevřete aplikaci na adrese `localhost:8000`.
   - Zobrazí se vám stránka aplikace?
2. V aplikaci otevřete záložku `Naši veterináři`.
   - Zobrazí se seznam veterinářů nebo databázová chyba?
   - Pokud vidíte DB chybu, zkontrolujte, zda jste provedli všechny kroky návodu.
3. V aplikaci otevřete záložku **Sjednat schůzku**, vyplňte a odešlete formulář.
4. Otevřete stránku `localhost:8000/admin`, přihlaste se jako superuživatel a zkontrolujte, že existuje Schůzka vytvořená v předchozím kroku.
   - Nemůžete se přihlásit? Zkontrolujte, zda jste provedli všechny kroky dle návodu.

## Už máte hotovo?

1. Zkuste napsat Bash skript, který provede automaticky uvedené příkazy (nebo alespoň jejich část).

2. Příkaz `createsuperuser` je záludnější na automatizaci, protože potřebuje vstup od uživatele. Je ale možné jej spustit i bez nutnosti interaktivního ovládání?

   Spoiler: Je to možné :) Viz https://docs.djangoproject.com/en/3.0/ref/django-admin/#createsuperuser
