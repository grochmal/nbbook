#!/usr/bin/env python


import logging
from collections import defaultdict


LOG = logging.getLogger(__name__)
HANDLER = logging.StreamHandler()
FMT = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
HANDLER.setFormatter(FMT)
LOG.addHandler(HANDLER)
LOG_LEVELS = defaultdict(
    lambda x: logigng.DEBUG,
    {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG})
# import this logger and overwrite the level for controlled logging
LOG.setLevel(LOG_LEVELS[1])

