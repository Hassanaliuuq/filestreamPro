# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()
bot_name = "Fɪʟᴇ2Lɪɴᴋ Bᴏᴛ"
bisal_channel = "https://telegram.me/hdlinks4uu"
bisal_grp = "https://t.me/movie_request_group_69"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '21845036'))
    API_HASH = str(getenv('API_HASH', 'b9787357754c57417854ba8ca0d35129'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '6594741905:AAGz5pptFU_ipZA4B-6WyFNh65D6JNInMWQ'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    name = str(getenv('name', 'Chatgpt_adv_bot'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002754811952'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1002754811952'))
    PORT = int(getenv('PORT', '80'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5510849897").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Snow_0_ball'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://BIGBOSS:BIGBOSS@cluster0.ii3gmvr.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Public_Review'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002031180571")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "-1001734958816")).split()))   
    
