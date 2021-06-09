# Zadání - Úloha 2

Vytvořte `Dockerfile`, pomocí kterého automatizujete úvodní kroky a krok spuštění serveru, tedy:

- Nainstalovat Python >= 3.6
- Nainstalovat závislosti: `pip install -r requirements.txt`
- Spustit server tak, aby naslouchal na všech rozhraních: `gunicorn -b 0.0.0.0:8000`

Následně v běžícím kontejneru proveďte manuálně zbývající příkazy:

- Přejít do projektového podadresáře: `cd czechitas`
- Spustit DB migraci: `python manage.py migrate`
- Vytvořit superuživatele: `python manage.py createsuperuser`

Užitečné instrukce pro `Dockerfile` najdete na [stránkách workshopu](https://czechitas.orchi.page/linux/uzitecne/docker/).

# Nápověda

- Nemůžete se připojit k aplikaci zvenku i když jste kontejneru namapovali porty pomocí `-p 8000:8000`?
  - Zkontrolujte, zda aplikace naslouchá na všech síťových rozhraních, tedy na `0.0.0.0:8000`. Pokud naslouchá na 127.0.0.1, bude dostupná jen zevnitř kontejneru.

# Už máte hotovo?

1. Pomocí příkazů v `Dockerfile` automatizujte i zbylé manuální kroky (DB migrace a tvorba superuživatele).

2. Zkuste vysvětlit, proč můžeme při použití Dockeru vynechat tyto kroky:
   - Vytvořit virtuální prostředí Pythonu: `python3 -m venv venv`
   - Aktivovat virtuální prostředí: `source venv/bin/activate`
