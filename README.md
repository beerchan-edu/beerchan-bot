# Beerchan Bot

Beerchan Bot is a Telegram bot designed to help you track and manage your workout durations. You can save your workout times, see your progress, and compete with others in your chat group.

## Features

- Track and save your workout durations
- View the top sportsmen in your chat group for the last 30 days
- Simple commands to interact with the bot

## Commands

- `/start` - Start the bot and get a welcome message
- `/help` - Get information about available commands
- `/save <message>` - Save your workout message (duration in minutes)
- `/top` - Show the top sportsmen for the last 30 days in the current chat

## Setup and Installation

### Prerequisites

- Docker
- Docker Compose
- Python 3.8 or higher
- Telegram Bot Token (you can get this from BotFather on Telegram)

### Clone the Repository

```
git clone https://github.com/yourusername/beerchan-bot.git
cd beerchan-bot
```

### Environment Variables
Create a .env file in the root directory of the project and add the following environment variables:

```
POSTGRES_PASSWORD=<your password>
POSTGRES_USER=<your username>
POSTGRES_DB=sports_db
TELEGRAM_KEY=<your telegram bot token>
```

### Docker Setup
This project uses Docker to run the bot and PostgreSQL database. The database is initialized within Docker for training purposes. The db service in the docker-compose.yml file sets up the database with the necessary environment variables.

#### Building and Running the Containers
1. Build the Docker Containers:
```
docker-compose build
```
2. Start the Docker Containers:
```
docker-compose up -d
```
3. Check Logs to Ensure Everything is Running:
```
docker-compose logs -f bot
```

## Application Structure

* app/command_handler.py: Contains the command handling logic for the bot.

* app/models.py: Defines the database models.

* app/db.py: Sets up the database connection.

* app/main.py: Entry point for the bot, initializes the bot application and adds command handlers.

* consts.py: Contains constant values such as the Telegram bot token.

* Dockerfile: Defines the Docker image for the bot.

* docker-compose.yml: Defines the Docker services for the bot and PostgreSQL database.

## Example Usage

1. ### Save a Workout Duration:
```
/save I did a workout for 30 minutes
```
Response:
```
I saved your result, User
```

2. ### View Top Sportsmen:
```
/top
```
Response:
```
TOP best sportsmen for the last 30 days:
1. User1 1h 30m
2. User2 1h 0m
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License
This project is licensed under the GNU License.

## Acknowledgments
Special thanks to all contributors and third-party resources used in this project.
