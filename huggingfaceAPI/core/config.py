from starlette.config import Config

APP_VERSION = "0.1.0-dev"
APP_NAME = "Huggingface API"
API_PREFIX = "/api"
TASK = "TEXT_GENERATION"

config = Config(".env")

MODEL_NAME_OR_PATH: str = config("MODEL_NAME_OR_PATH")
FP16: bool = config("FP16", cast=bool, default=False)
