#!/usr/bin/python3

import logging  # installed by default

import colorlog  # run python -m pip install colorlog

# Setup

# We use __name__ to give our logger a unique name for this file.
# If you're using, say, Matplotlib alongside this code snippet,
# logging.getLogger() will actually cause *both* Matplotlib's debug
# messages *and* your own ones to write to stdout!
logger = logging.getLogger(__name__)
logger.setLevel(colorlog.colorlog.logging.DEBUG)

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())
logger.addHandler(handler)

if __name__ == "__main__":
    logger.debug("This is what DEBUG looks like.")
    logger.info("This is what INFO looks like.")
    logger.warning("This is what WARNING looks like.")
    logger.error("This is what ERROR looks like.")
    logger.critical("This is what CRITICAL looks like.")

    logger.debug("  You change which level you want to see by changing")
    logger.debug("       logger.setLevel(colorlog.colorlog.logging.DEBUG)")
    logger.debug("  at the top.")

    logger.debug("For example, I change it to WARNING, and now...")

    logger.setLevel(colorlog.colorlog.logging.WARNING)

    logger.debug("This is what DEBUG looks like.")
    logger.info("This is what INFO looks like.")
    logger.warning("This is what WARNING looks like.")
    logger.error("This is what ERROR looks like.")
    logger.critical("This is what CRITICAL looks like.")
