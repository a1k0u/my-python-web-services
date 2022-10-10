"""
Configurate logger for project.
"""

import logging
import sys

log_format = "[%(asctime)s] [%(levelname)s] - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=log_format)
logging.StreamHandler(sys.stdout)

logger = logging.getLogger("gRPC")

if __name__ == "__main__":
    logger.debug("Test debug info.")
