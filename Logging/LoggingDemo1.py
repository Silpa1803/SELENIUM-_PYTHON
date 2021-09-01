import logging
logging.basicConfig(filename="test2.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG
                    )

logging.debug("This is a DEBUG message")
logging.info("This is a INFO message")
logging.warning("This is a WARNING message")
logging.error("This is a ERROR message")
logging.critical("This is a CRITICAL message")