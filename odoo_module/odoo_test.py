from entities.entities import OdooEntity
from utils.logger import get_logger

logger = get_logger(__name__)


class OdooTest:
    @classmethod
    def setup_class(cls):
        if not cls.model:
            raise ValueError("Model is not set")
        cls.entity = OdooEntity(cls.model)
        cls.to_delete = []

    def setup_method(self, method):
        logger.info("Running test %s", method.__name__)

    def teardown_method(self, method):
        logger.info("Finished test %s", method.__name__)

    @classmethod
    def teardown_class(cls):
        if cls.to_delete:
            logger.info("Cleaning test records with ids %s", cls.to_delete)
            cls.entity.delete(cls.to_delete)
            cls.to_delete = []
