import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def setup_logging(verbose=False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt="%H:%M:%S",
    )


def validate_input(filepath):
    if not Path(filepath).is_file():
        logger.error(f"Input file not found: {filepath}")
        return False
    logger.info(f"Input file validated: {filepath}")

    return True