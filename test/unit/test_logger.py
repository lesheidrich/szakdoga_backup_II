import os
import unittest
from datetime import datetime
from log.logger import Logger


class TestLogger(unittest.TestCase):
    def setUp(self) -> None:
        self.log = Logger(log_file="app_test_log.log",
                          name="UNIT_TEST_LOG",
                          log_level="DEBUG")

    def tearDown(self) -> None:
        self.log.clear_log()
        self.log.close_log()

    def test_file_creation(self):
        """
        Ensures existence of test log file.
        :return: None
        """
        self.assertTrue(os.path.exists(self.log.log_file_path))

    def test_creation_from_elsewhere(self):
        """
        Checks successful creation of log file from different dir.
        :return: None
        """
        cwd = os.getcwd()
        os.chdir("../")
        test = Logger(log_file="app_test_log_elsewhere.log")
        test.info("Test log message from elsewhere")
        self.assertTrue(os.path.exists(test.log_file_path))
        test.delete_log()
        os.chdir(cwd)

    def test_build_path(self):
        """
        Ensures log file build path functionality.
        :return: None
        """
        mock_path = self.log._build_path("test.file")
        project_dir = os.getcwd().rsplit("test", 1)[0]
        log_dir = os.path.join(project_dir, 'log')
        log_path = os.path.join(log_dir, "test.file")
        self.assertTrue(mock_path == log_path)
        os.remove(mock_path)

    def test_init_arg_error(self):
        """
        Ensures AttributeError is thrown for instantiation attempt with wrong arg.
        :return: None
        """
        with self.assertRaises(AttributeError):
            Logger(log_file="wrong_param.log", name="UNIT_TEST_LOG", log_level="wrong")

    def test_get_content(self):
        """
        Ensures Logger.get_content() functionality.
        :return: None
        """
        comment = "Running TestLogger.test_get_content() unit test."
        self.log.info(comment)
        content = self.log.get_content()
        self.assertIn(comment, content)

    def test_info_bool_logging(self):
        """
        Test boolean input for log. Ensure info function logs properly through time check of INFO log.
        :return: None
        """
        self.log.info(True)
        content = self.log.get_content()
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.assertIn("True", content)
        self.assertIn("INFO", content)
        self.assertIn(current_datetime, content)

    def test_warning_str_logging(self):
        """
        Test str input for log. Ensure warning function logs properly through time check of INFO log.
        :return: None
        """
        comment = "This is a warning check string"
        self.log.warning(comment)
        content = self.log.get_content()
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.assertIn(comment, content)
        self.assertIn("WARNING", content)
        self.assertIn(current_datetime, content)

    def test_int_error_logging(self):
        """
        Test int input for log. Ensure error function logs properly through time check of INFO log.
        :return: None
        """
        self.log.error(5)
        content = self.log.get_content()
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.assertIn("5", content)
        self.assertIn("ERROR", content)
        self.assertIn(current_datetime, content)

    def test_clear_log(self):
        """
        Ensures Logger.clear_log() functionality.
        :return: None
        """
        comment = "Comment for clearing function."
        self.log.info(comment)
        self.log.clear_log()
        content = self.log.get_content()
        self.assertNotIn(comment, content)

    def test_close_log(self):
        """
        Ensures Logger.close_log() functionality.
        :return: None
        """
        self.log.close_log()
        self.assertFalse(self.log.has_open_handlers())
        self.setUp()

    def test_has_open_handlers(self):
        """
        Ensures Logger.has_open_handlers() functionality.
        :return: None
        """
        self.assertTrue(self.log.has_open_handlers())

    def test_delete_log(self):
        """
        Ensures Logger.delete_lot() functionality.
        :return: None
        """
        path = self.log.log_file_path
        self.log.close_log()
        self.log.delete_log()
        self.assertFalse(os.path.exists(path))
        self.setUp()
