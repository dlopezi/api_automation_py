from helpers.client import XMLRPCClientSingleton
from utils.logger import get_logger


logger = get_logger(__name__)


class OdooEntity:
    def __init__(self, model):
        self.model = model
        self.client = XMLRPCClientSingleton.get_instance()

    def create(self, data):
        logger.debug("Creating '%s' record with data %s", self.model, data)
        record_id = self.client.execute_kw(self.model, 'create', data)
        logger.debug("Created record with id %s", record_id)
        return record_id[0] if type(record_id) is list else record_id

    def read(self, ids=None):
        if ids is None:
            filtering = []
        elif type(ids) is not list:
            filtering = [['id', 'in', [ids]]]
        else:
            filtering = [['id', 'in', ids]]

        logger.debug("Getting '%s' records with ids %s", self.model, ids)
        result = self.client.execute_kw(self.model, 'search_read', filtering)
        logger.debug("Read records with ids %s", ids)
        return result

    def write(self, record_id, data):
        logger.debug("Updating '%s' record with id %s", self.model, record_id)
        result = self.client.execute_kw(self.model, 'write', [record_id], data)
        logger.debug("Updated record with id %s", record_id)
        return result

    def delete(self, record_ids):
        if type(record_ids) is not list:
            record_ids = [record_ids]
        logger.debug("Deleting '%s' records with ids %s", self.model, record_ids)
        result = self.client.execute_kw(self.model, 'unlink', record_ids)
        logger.debug("Deleted '%' record with id %s", record_ids)
        return result
