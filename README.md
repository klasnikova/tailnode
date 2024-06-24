# Tail Node Site - Docs

![Main](/static/favicon.ico)

## Deployment Project With Docker Locally (Linux)

### Getting Started
- Node.JS & NPM [Docs](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)
- Docker Compose [Docs](https://docs.docker.com/compose/install/)

### Development Usage
Go to tailnode_site project e.g.
```console
./tailnode-site/tailnode_site
```

Create .env file
```console
$ touch .env
```

Add the following environment variables by edit .env file
```console
$ vi .env
```
```console
SECRET_KEY=(Your key)
DEBUG=True
PRODUCTION=False
ALLOWED_HOSTS=localhost
```

You can add your own key or generate a new key by following the command as well
```console
$ docker-compose run web python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

We strongly recomend to set DEBUG **False** when running on prduction environment, You can check database to ensure database is perfectly set on production.

If you want to tracking your analytics add this
```console
...
GOOGLE_ANALYTICS_ID=(Your Measurement ID)
...
```

Save .env file by press `esc` and type "wq" and press `enter`
```console
...


wq
```

Go to project root e.g.
```console
./tailnode-site
```

Install package via npm:
```console
$ npm install
```

Run docker compose
```console
$ docker-compose up
```

Service running on [http://localhost:8080](http://localhost:8080) by default
<br>

If you want to start developing, you can open another window to start the Tailwind CLI build process and webpack builder side by side.

Start the Tailwind CLI build process
```console
$ npx tailwindcss -i ./src/tailnode-entrypoint.css -o ./src/styles/tailnode-site.css --watch
```

Start webpack builder
```console
$ npm run dev
```

<br>
<br>
<br>
Write on July 24, 2024.
<br>

[faturrachmanmochammad.id](https://www.faturrachmanmochammad.id)