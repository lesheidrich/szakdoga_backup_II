# Example usage
from log.logger import Logger

if __name__ == "__main__":
    logger = Logger(name='MyApp', log_file="application_log.log")

    logger.log('info', "asdfasdfasdfasdfs")
