import os

from dotenv import load_dotenv

load_dotenv()

# check if .env exists in root
if not os.path.exists(".env"):
    if not os.path.exists(".env.example"):
        raise FileNotFoundError("File `.env` does not exist in the root directory.")
    else:
        raise FileNotFoundError(
            "The `.env` file is missing. Please copy `.env.example` to `.env` and fill in the required values."
        )

# check if all required environment variables are set
for env_var in ["API_URL", "MINIMUM_SERVER_ID_CHARACTER_COUNT", "REQUEST_COOLDOWN"]:
    if not os.getenv(env_var):
        raise ValueError(f"Environment variable {env_var} is not set in the .env file.")

API_URL = os.getenv("API_URL")
HELP = "A space-separated list of Discord server IDs, e.g. 123456789012345678 123456789012345678"
ARG_NAME = "servers"
METAVAR = "ID1 ID2 ... IDn"
MINIMUM_SERVER_ID_CHARACTER_COUNT = os.getenv("MINIMUM_SERVER_ID_CHARACTER_COUNT")
REQUEST_COOLDOWN = os.getenv("REQUEST_COOLDOWN")
