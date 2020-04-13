import logging
from pathlib import Path


# create logger with 'main'
logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)


def init_logging():
    """This is a docstring

    """
    if not Path(logPath := "logs/main.log").exists():
        with open(logPath, "w") as f:
            pass
    # create file handler which logs with level DEBUG
    fh = logging.FileHandler(logPath)
    fh.setLevel(logging.DEBUG)
    # create console handler which also logs with level DEBUG
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)


def main():
    logger.warning("TEST")
    print("hello world")


if __name__ == "__main__":
    init_logging()
    main()
