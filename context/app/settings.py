import os


DEBUG = bool(int(os.environ.get('DEBUG', '0')))
if DEBUG:
    from dotenv import load_dotenv
    load_dotenv('../../.env')
    load_dotenv('../../local.env', override=True)

# App settings.
APP_HOST = os.environ['APP_HOST']
APP_PORT = int(os.environ['APP_PORT'])

# Log settings.
LOG_LVL = os.environ['LOG_LVL']

# Service settings
SERVICE = os.environ['SERVICE']