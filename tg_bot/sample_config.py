if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1790024478:AAHlU51dRdzjH4vO4H07sT75lU1Rytp6YSM"
    OWNER_ID = 514358671  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "chetanguptaa"
    API_ID=3966119
    API_HASH="bbe93fd2299c195cc6935cabcc3c2a51"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://ixlgkmparpfvie:43b26eba5b3af2cb4b6782a07f6a9f75ac4a80893a7037fec5b0ff6e224b3163@ec2-54-225-182-108.compute-1.amazonaws.com:5432/d1rjq0oj8a8lnd'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    # sed has been disabled after the discovery that certain long-running sed commands maxed out cpu usage
    # and killed the bot. Be careful re-enabling it!
    NO_LOAD = ['translation', 'rss', 'sed']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    DEV_USERS = []
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [1106816358]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /
    MAL_REFRESH_TOKEN = ''
    MAL_ACCESS_TOKEN = ''
    MAL_CLIENT_ID = ''
    MOE_API = ''
    WALL_API = ''
    LASTFM_API_KEY = ''
    AI_API_KEY = ''
    BL_CHATS = []

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
