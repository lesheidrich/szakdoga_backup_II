import logging
import os
from typing import Literal


class Logger:
    """
        LOGGER:
        A custom logger for handling application logs.

        Attributes:
            log_file (str): The path to the log file.
            log_formatter (logging.Formatter): The formatter for log messages.
            log_handler (logging.Handler): The log handler for writing logs to a file.
            console_handler (logging.Handler): The log handler for writing logs to the console.

        Methods:
            __init__(self, log_file: str)
                Initialize the logger.

            info(self, message: str)
                Log informational messages.

            exception(self, message: str)
                Log an exception message.

            configure_console_logging(self)
                Configure the logger to log messages to the console.

            add_context(self, key: str, value: str)
                Add contextual information to logs.

        Usage:
            logger = MyLogger("app.log")
            logger.info("This is an informational message.")
            logger.exception("An error occurred.")
            logger.configure_console_logging()
    """
    def __init__(self,
                 log_level: Literal["INFO", "DEBUG"] = "INFO",
                 name=__name__,
                 log_file='application_log.log'):
        level = getattr(logging, log_level)
        self.log_file_path = self._build_path(log_file)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_file_handler(self.log_file_path, level)
        self._setup_console_handler(level)

    def _setup_file_handler(self, log_file: str, log_level) -> None:
        """
        Sets up the logging formatter.
        :param log_file: str of absolute file path
        :param log_level: sets log level [INFO | DEBUG]
        :return: None
        """
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def _setup_console_handler(self, log_level) -> None:
        """
        Sets up logging formatter for printing to console.
        :param log_level: sets log level [INFO | DEBUG]
        :return: None
        """
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(name)s')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def _build_path(self, file: str) -> str:
        """
        Ensures log file is created in log dir. Builds absolute path for arg filename.
        :param file: str application filename (can add subdirectories in log dir)
        :return: str of absolute log file path
        """
        project_folder = "WebScraping_and_MonteCarloSim_gwjz4t"
        project_dir = os.getcwd().rsplit(project_folder, 1)[0] + project_folder
        log_dir = os.path.join(project_dir, 'log')
        path = os.path.join(log_dir, file)

        if not os.path.exists(path):
            with open(path, 'w'):
                pass
        return path

    # def log(self, message, log_type: Literal["INFO", "WARNING", "ERROR"] = "INFO") -> None:
    #     """
    #
    #     :param message: message to log (auto-converts to str)
    #     :param log_type: The type of log ("INFO", "WARNING", "ERROR")
    #     :return:
    #     """
    #     log_function = getattr(self.logger, message, log_type.lower())
    #     try:
    #         log_function(message)
    #     except Exception as e:
    #         print(f"Error logging message: {message}\n{e}")

    def info(self, message) -> None:
        """
        Logs arg message as INFO.
        :param message: Logs arg (auto-converts to str).
        :return: None
        """
        self.logger.info(message)

    def warning(self, message) -> None:
        """
        Logs arg message as WARNING.
        :param message: Logs arg (auto-converts to str).
        :return: None
        """
        self.logger.warning(message)

    def error(self, message) -> None:
        """
        Logs arg message as ERROR.
        :param message: Logs arg (auto-converts to str).
        :return: None
        """
        self.logger.error(message)

    def get_content(self) -> str:
        """
        Gets contents of log file as str.
        :return: log file content as str
        """
        with open(self.log_file_path, "r") as f:
            content = f.read()
        return content

    def clear_log(self) -> None:
        """
        Clears the contents of the log file.
        :return: None
        """
        try:
            with open(self.log_file_path, 'w'):
                pass
            print(f"Log file '{self.log_file_path}' truncated.")
        except Exception as e:
            print(f"Error clearing log file{self.log_file_path}!\n{e}")

    def has_open_handlers(self) -> bool:
        """
        Boolean check for status of log handlers.
        :return: True for open log, else False
        """
        return len(self.logger.handlers) > 0

    def close_log(self) -> None:
        """
        Closes every connection to the log file by removing handlers.
        :return: None
        """
        try:
            if self.has_open_handlers():
                for handler in self.logger.handlers[:]:
                    self.logger.removeHandler(handler)
                    handler.close()
        except Exception as e:
            print(f"Error closing log: {e}")

    def delete_log(self) -> None:
        """
        Deletes the log file.
        :return: None
        """
        try:
            self.close_log()
            os.remove(self.log_file_path)
            print(f"Successfully deleted log: {self.log_file_path}")
        except Exception as e:
            print(f"Error deleting log: {e}")
