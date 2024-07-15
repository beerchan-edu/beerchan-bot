# beerchan-bot
Playground repository

# How to locally run the project.
to connect postgres database, you need:
1) launch docker-compose.yaml (docker-compose up --d)
2) connect to the database using psql in terminal
(psql -h localhost -U admin) password = root

## python configuration
1. install python
2. `pipenv shell` & select in VS code via cmd+shift+P -> 'python select interpretor' the interpreter in this folder
3. update .env file. it should look like:
```
TELEGRAM_KEY=YOUR_BOT_TELEGRAM_KEY
```
4. run bot via terminal `python app/bot.py`

### TODO:
1. Make a beautiful readme file
2. Create tests on github
3. Create a dockerfile
4. Run bot on some host
