import logging

logger = logging.getLogger("databricks.labs.mcp")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(handler)
