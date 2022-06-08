# Úloha 3

## Cíl

Vyzkoušet si skládání služeb (aplikace + databáze) pomocí `docker compose`.

## Zadání

Vytvořte konfigurační soubor `docker-compose.yml`, pomocí kterého bude sestavena („zbuilděna“) naše aplikace.

Soubor `Dockerfile` už máte připravený a nemusíte do něj zasahovat.

Až vám bude fungovat spuštění aplikace přes příkaz `docker compose up` (aplikace by se měla chovat stejně jako v předchozí úloze), přidejte do `docker-compose.yml` další službu s databází **PostgreSQL 13.7**. Použijte [oficiální postgres image z DockerHubu](https://hub.docker.com/_/postgres).

Následně nastavte proměnné prostředí pro službu aplikace (viz dále - `DB_ENGINE`, `DB_NAME` atd.)

To samé proveďte pro službu databáze. Zde nastavte proměnné prostředí podle [popisu na DockerHubu](https://hub.docker.com/_/postgres), tedy tyto:

- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`

Přehled příkazů pro `docker compose` najdete na [stránkách workshopu](https://czechitas.orchi.page/devops/uzitecne/docker/).

## Jak nastavit aplikaci, aby používala jinou databázi

Defaultně aplikace používá souborovou SQLite databázi.
Váš kolega vývojář už však aplikaci připravil tak, aby si přebírala konfiguraci z proměnných prostředí.
Jinou DB je proto možné využít nastavením těchto proměnných prostředí:

- `DB_ENGINE` -- DB Engine, např. `django.db.backends.sqlite3`
- `DB_NAME` -- Název databáze
- `DB_USER` -- Uživatel databáze
- `DB_PASSWORD` -- Heslo uživatele databáze
- `DB_HOST` -- Hostname či IP adresa, na které je databáze přístupná
- `DB_PORT` -- Port, na kterém databáze naslouchá

Kdybyste chtěli do nastavení nahléhnout (pro vyřešení úlohy to potřeba ale není), najdete ho v `./czechitas/czechitas/settings.py`.

Django podporuje následující DB enginy (jejich název zde odpovídá proměnné `DB_ENGINE`):

- 'django.db.backends.postgresql'
- 'django.db.backends.mysql'
- 'django.db.backends.sqlite3'
- 'django.db.backends.oracle'

Nastavením těchto proměnných prostředí řeknete aplikaci, aby používala danou databázi místo defaultní SQLite.

## Nápověda

1. Při úpravě `docker-compose.yml` dbejte na správné odsazení.

2. Databázi nesestavujeme lokálně, ale bereme si hotový image z DockerHubu. V `docker-compose.yml` tedy nepoužíváme položku `build`, ale položku `image`.

3. Při použití `docker compose` dojde k vytvoření defaultní sítě. Služby (tedy aplikace a databáze) se navzájem vidí pod hostnamem, který je defaultně stejný jako jejich název v souboru `docker-compose.yml`. Máme-li pod `services` definovanou aplikaci jako `app` a databázi jako `db`, tak aplikace může k databázi přistoupit přes hostname `db`.

4. U databáze není potřeba mapovat porty, aby k ní mohla přistupovat aplikace na stejné síti (pamatujte, že byla vytvořena defaultní síť). Porty mapujeme jen když potřebujeme propojit kontejner s hostitelským systémem.

5. Nezapomeňte, že hodnoty v proměnných prostředí aplikace a databáze musí souhlasit. Například pokud ve službě databáze nastavíte název `POSTGRES_DB=mojedb`, tak musíte odpovídajícím způsobem nastavit proměnnou aplikace `DB_NAME=mojedb`.
