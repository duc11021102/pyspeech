import logging
import colorlog

#logger config
def setup_logger(level=logging.INFO):
    logger = logging.getLogger("tts-audio")
    logger.setLevel(level)

    # format logger output
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )

    # cli handler
    cli_handler = logging.StreamHandler()
    cli_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(cli_handler)
    return logger