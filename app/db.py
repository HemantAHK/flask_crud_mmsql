from app import db
from logzero import logger
db.create_all()

logger.info("Table Created Successfully.")