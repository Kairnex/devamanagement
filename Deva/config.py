class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 20536459
    API_HASH = "c1c01c363ed3dcd6017d89d5938afb6f"

    CASH_API_KEY = "8SOSKTRI0KPL"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://u42ofs7t07ivi:paaaa8cdb6040a555e3a65e5b8945038e1e8b7c54c1bc33bc06c660642feb9535@c1vo05l6n8k8mv.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d304b47asno1o9"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002404751523)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://eagleupdate019:1TNeLNefuf2Fn5Du@cluster0.3zhea.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://files.catbox.moe/6gn6nf.jpg"

    SUPPORT_CHAT = "https://t.me/TFW_UPDATES"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "8098975400:AAFvNVpkYmTTD7AKLNO7t6ErrXSUl7JuTrI"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "https://timezonedb.com/api"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7538572906 # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = [7538572906]  # List of groups that you want blacklisted.
    DRAGONS = [7538572906]  # User id of sudo users
    DEV_USERS = [7538572906]  # User id of dev users
    DEMONS = [7538572906]  # User id of support users
    TIGERS = [7538572906]  # User id of tiger users
    WOLVES = [7538572906]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
