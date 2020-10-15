#!/usr/bin/python3

import logging  # installed by default

import colorlog  # run python -m pip install colorlog

# Setup

logger = logging.getLogger()
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
