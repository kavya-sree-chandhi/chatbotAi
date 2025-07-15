import logging
import os
import sys
from functools import lru_cache

import arrow


@lru_cache(maxsize=1)
def configure_logging(log_name='root_logger', log_dir: str = None, log_level=logging.INFO):

    formatter = logging.Formatter('[%(asctime)s] [%(threadName)s] [%(levelname)s] %(message)s')
    h_screen = logging.StreamHandler(sys.stdout)

    root_logger = logging.getLogger()
    root_logger.addHandler(h_screen)
    root_logger.setLevel(log_level)
    h_screen.setFormatter(formatter)

    if log_dir:
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, 'log_{}.log'.format(arrow.now().format("YYYY-MM-DDTHH_mm")))
        h_file = logging.FileHandler(log_file, mode='w', encoding='utf-8')
        h_file.setFormatter(formatter)
        root_logger.addHandler(h_file)

    logging.getLogger(log_name).debug('"{}" loggers configured'.format(log_name))
