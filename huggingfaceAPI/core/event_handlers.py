from typing import Callable

from fastapi import FastAPI
from loguru import logger

from core.config import MODEL_NAME_OR_PATH, TASK, FP16
from models.nlp import TextGenerationModel
from core.commons import Tasks


def _startup_model(app: FastAPI) -> None:
    model_name_or_path = MODEL_NAME_OR_PATH
    task = TASK
    fp16 = FP16
    if task == Tasks.TEXT_GENERATION.value:
        model_instance = TextGenerationModel(model_name_or_path, fp16)
    else:
        pass
    # model_instance = QAModel(model_path)
    app.state.model = model_instance


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")
        _startup_model(app)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        _shutdown_model(app)

    return shutdown
