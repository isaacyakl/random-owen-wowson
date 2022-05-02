# random-owen-wowson

A discord bot to send random Owen Wilson "wow" clips. Powered by The Owen Wilson Wow API: https://owen-wilson-wow-api.herokuapp.com/

## Setup the bot

### 1. Get a Bot token

Follow this link to create a Discord app, create a Bot, and generate a Bot token:
https://discord.com/developers/docs/getting-started#creating-an-app

### 2. Install dependencies

`pip install -r requirements.txt`

### 3. Supply your Bot token

Create an `.env` file in the root directory and place your Discord Bot token in this file like so:

```
TOKEN=<discord_token>
```

## Run the bot

```
python bot.py
```

## Monitor the bot's status (Health Check)

A Flask app is included to indicate the status of the bot.

### Setup the bot status app

Add the following to the `.env` file, on a newline:

```
FLASK_APP=status
```

### Run the bot status app

(Linux only)

```
gunicorn bot:app
```
