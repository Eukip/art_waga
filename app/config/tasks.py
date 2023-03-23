from .celery import celery_app
from celery.utils.log import get_task_logger
from datetime import datetime


logger = get_task_logger(__name__)


@celery_app.task
def sample_task():
    logger.info("The sample task just ran.")
