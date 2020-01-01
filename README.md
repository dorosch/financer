## Financer

Telegram bot for cost accounting.


### Usage

1. Create `.env` file:
```bash
$ echo "TELEGRAM_API_KEY=YOUR_API_TOKEN" > .env
```

2. Build docker-container:
```bash
$ docker build --tag financer:latest .
```

3. And run container:
```bash
$ docker run --env-file .env -it --rm financer:latest
```
