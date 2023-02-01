from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "28360704"))
API_HASH = getenv("API_HASH", "60f9309f95081eed3da7c42148e602d6")
BOT_TOKEN = getenv("BOT_TOKEN", "6102973133:AAFuY3QWYue-JcPRzBI5t2NRKhxWRRImnnQ)
SESSION_NAME = getenv("SESSION_NAME", "AQGwwAAAFOeoU7EP4fvHtEmb3sZ4dYLSrD3S1OQugmMea9xefo27U-HLpviLH52NySlu9go9ZU9T7Aojk_yXozSYGMnD1hVjGyrrUuZnk-fPda6TW3uiG_FJuNtSLCb5zYmwTmByzzenG5Ih8E0HjHzqISg8-3IUyWuD9FUazRmAPg0K2f5j4vIYC5TFq1kdJ0-NLnTKpLzkyMba6ihdIOCVyPUoqsm57SNoCncqNzsiH7vxN9FllsvrctRVmnBnVdnSK-FGOB-uWIBOtAErxAkRw5yT_eX5zECTX_3vJly9KGzP1fk821zRFecVZabnwZieqdceYC-5xnKolRSAjikpVOhgrAAAAAFvjWGwAA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "Prooooo1v1")
ALIVE_NAME = getenv("ALIVE_NAME", "abdo")
BOT_USERNAME = getenv("BOT_USERNAME", "Abdopllaewbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ujikmhioo")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ujikmhioo")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://abdoragab3190:<password>@cluster0.hn3lkvl.mongodb.net/?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "6166503856").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6166503856").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
