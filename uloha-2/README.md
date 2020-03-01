# Zadání - Úloha 2

Vytvořte `Dockerfile`, pomocí kterého automatizujete úvodní kroky a krok spuštění serveru, tedy:

- Nainstalovat Python >= 3.6
- Nainstalovat závislosti: `pip install -r requirements.txt`
- Spustit server: `python manage.py runserver`

Následně v běžícím kontejneru proveďte manuálně zbývající příkazy:

- Přejít do projektového podadresáře: `cd czechitas`
- Spustit DB migraci: `python manage.py migrate`
- Vytvořit superuživatele: `python manage.py createsuperuser`

Abyste správně viděli výstupy aplikace v terminálu, přidejte si do `Dockerfile` instrukci `ENV PYTHONUNBUFFERED=1`. Např. hned za instrukci `FROM`.

Užitečné instrukce pro `Dockerfile` najdete na [stránkách workshopu](https://czechitas.orchi.page/linux/docker/).

# Nápověda

- Nemůžete se připojit k aplikaci zvenku i když jste kontejneru namapovali porty pomocí `-p 8000:8000`?
  - Zkontrolujte, zda aplikace naslouchá na všech síťových rozhraních, tedy na `0.0.0.0:8000`. Pokud naslouchá na 127.0.0.1, bude dostupná jen zevnitř kontejneru.
  - Nevíte si rady, jak na to? Nahlédněte do [dokumentace Djanga](https://docs.djangoproject.com/en/3.0/ref/django-admin/#runserver).

# Už máte hotovo?

1. Pomocí příkazů v `Dockerfile` automatizujte i zbylé manuální kroky (DB migrace a tvorba superuživatele).

2. Zkuste vysvětlit, proč bez přidání instrukce `ENV PYTHONUNBUFFERED=1` nevidíme ve svém terminálu všechny zprávy, které aplikace posílá na výstup.

3. Zkuste vysvětlit, proč můžeme při použití Dockeru vynechat tyto kroky:
   - Vytvořit virtuální prostředí Pythonu: `python3 -m venv venv`
   - Aktivovat virtuální prostředí: `source venv/bin/activate`
