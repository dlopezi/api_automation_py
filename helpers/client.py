from xmlrpc.client import ServerProxy

from config.config import API_URL, API_USER, API_PASS, API_DB
from utils.logger import get_logger

logger = get_logger(__name__)

MODELS_URI_FORMAT = '{}/xmlrpc/2/object'


class XMLRPCClientSingleton:
    __instance = None

    @staticmethod
    def get_instance():
        if XMLRPCClientSingleton.__instance is None:
            logger.debug("Creating XMLRPCClientSingleton instance")
            XMLRPCClientSingleton()
        return XMLRPCClientSingleton.__instance

    def __init__(self):
        if XMLRPCClientSingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            try:
                self.__authenticate()
                self.__models_server = ServerProxy(MODELS_URI_FORMAT.format(self.__url))
                XMLRPCClientSingleton.__instance = self
            except ConnectionRefusedError as e:
                logger.error("Connection refused: %s", e)
            except Exception as e:
                logger.error("Error: %s", e)

    def __authenticate(self):
        logger.debug("Authenticating...")
        common = ServerProxy('{}/xmlrpc/2/common'.format(API_URL))
        self.__uid = common.authenticate(API_DB, API_USER, API_PASS, {})
        if not self.__uid:
            logger.error("Failed to authenticate")
        self.__url = API_URL
        self.__pass = API_PASS
        self.__db = API_DB
        logger.debug("Authenticated successfully")

    def execute_kw(self, model, method, *args):
        return self.__models_server.execute_kw(self.__db, self.__uid, self.__pass, model, method, args)
