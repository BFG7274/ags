
import logging
from pkg.notify import default_send_request


class logger:
    def __init__(self, level=logging.INFO, path="ags.log"):
        self.level = level
        logging.basicConfig(format='[%(asctime)s][%(process)d] %(name)s:%(levelname)s: %(message)s',
                            level=self.level,
                            filemode='a',
                            filename=path,
                            )

    def INFO(self, msg, tag=[]):
        logging.info(msg)
        tags = ['info']+tag
        if logging.INFO >= self.level:
            default_send_request(tags, "", msg)

    def WARNING(self, msg, tag=[]):
        logging.warning(msg)
        tags = ['warning']+tag
        if logging.WARNING >= self.level:
            default_send_request(tags, "", msg)

    def DEBUG(self, msg, tag=[]):
        logging.debug(msg)
        tags = ['debug']+tag
        if logging.DEBUG >= self.level:
            default_send_request(tags, "", msg)

    def ERROR(self, msg, tag=[]):
        logging.error(msg)
        tags = ['error']+tag
        if logging.ERROR >= self.level:
            default_send_request(tags, "", msg)


log = logger()
