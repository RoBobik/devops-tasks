# Výuková aplikace pro Docker Compose

Vytvořte konfigurační soubor `docker-compose.yml`, pomocí kterého bude sestavena a spuštěna přiložená aplikace vč. databáze.

Soubor `Dockerfile` už máte připravený a nemusíte do něj zasahovat.

Začněte s konfigurací Docker Compose služby pro aplikaci. Až vám bude fungovat build i spuštění aplikace přes příkaz `docker-compose up`, přidejte do `docker-compose.yml` další službu s databází **PostgreSQL**. Použijte [oficiální postgres image z DockerHubu](https://hub.docker.com/_/postgres).

Následně nastavte proměnné prostředí pro službu aplikace (viz dále - `DB_ENGINE`, `DB_NAME` atd.)

To samé proveďte pro službu databáze. Zde nastavte proměnné prostředí podle [popisu na DockerHubu](https://hub.docker.com/_/postgres), tedy tyto:

- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`

Přehled příkazů pro `docker-compose` najdete na [stránkách workshopu](https://czechitas.orchi.page/linux/docker/).

## Jak nastavit aplikaci, aby používala jinou databázi

Defaultně aplikace používá souborovou SQLite databázi.
Vývojář už však aplikaci připravil tak, aby si přebírala konfiguraci z proměnných prostředí.
Jinou DB je proto možné využít nastavením těchto proměnných prostředí:

- `DB_ENGINE` -- DB Engine, např. `django.db.backends.sqlite3`
- `DB_NAME` -- Název databáze
- `DB_USER` -- Uživatel databáze
- `DB_PASSWORD` -- Heslo uživatele databáze
- `DB_HOST` -- Hostname či IP adresa, na které je databáze přístupná
- `DB_PORT` -- Port, na kterém databáze naslouchá

Nastavením těchto proměnných prostředí řeknete aplikaci, aby používala danou databázi místo defaultní SQLite.

Framework Django podporuje následující DB enginy (jejich název zde odpovídá proměnné `DB_ENGINE`):

- `django.db.backends.postgresql`
- `django.db.backends.mysql`
- `django.db.backends.sqlite3`
- `django.db.backends.oracle`

## Zachování databázových dat

Databáze PostgreSQL, která běží ve vlastním kontejneru si ukládá data do adresáře `/var/lib/postgresql/data`.

Když je kontejner odstraněn, data jsou ztracena.

Úpravou `docker-compose.yml` přidejte Docker Volume pro výše uvedený adresář, aby po smazání kontejneru s databází a jeho opětovném vytvoření byla data stále k dispozici.

## Nápověda

1. Při úpravě `docker-compose.yml` dbejte na správné odsazení.

2. Databázi nesestavujeme lokálně, ale bereme si hotový image z Docker Hubu. V `docker-compose.yml` tedy nepoužíváme položku `build`, ale položku `image`.

3. Při použití `docker-compose` dojde k vytvoření defaultní sítě. Služby (tedy aplikace a databáze) se navzájem vidí pod hostnamem, který je defaultně stejný jako jejich název v souboru `docker-compose.yml`. Máme-li pod `services` definovanou aplikaci jako `app` a databázi jako `db`, tak aplikace může k databázi přistoupit přes hostname `db`.

4. U databáze není potřeba mapovat porty, aby k ní mohla přistupovat aplikace na stejné síti (pamatujte, že byla vytvořena defaultní síť). Porty mapujeme jen když potřebujeme propojit kontejner s hostitelským systémem.

5. Nezapomeňte, že hodnoty v proměnných prostředí aplikace a databáze musí souhlasit. Například pokud ve službě databáze nastavíte název `POSTGRES_DB=mojedb`, tak musíte odpovídajícím způsobem nastavit proměnnou aplikace `DB_NAME=mojedb`.

## Řešení

Řešením úlohy je soubor `docker-compose.yml`, kterým lze nastartovat aplikaci vč. její databáze.

Výsledné řešení najdete v souboru `reseni.b64`. Je zakódované pomocí `base64`, aby nebylo na první pohled čitelné.

Než nahlédnete do řešení, zkuste úlohu vyřešit s pomocí nápověd uvedených výše.

Pokud opravdu chcete zobrazit řešení, zavolejte `base64 -d reseni.b64`.
