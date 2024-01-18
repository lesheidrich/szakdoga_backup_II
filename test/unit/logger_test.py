import os
import time
import unittest
import secrets
from log.logger import Logger


class TestLogger(unittest.TestCase):
    def setUp(self) -> None:
        self.log = Logger(log_file="app_test_log.log",
                          name="UNIT_TEST_LOG",
                          log_level="DEBUG")

    def tearDown(self) -> None:
        self.log.clear_log()
        self.log.close_log()

    def test_log_file_created(self):
        """
        Ensures existence of test log file.
        :return: None
        """
        self.assertTrue(os.path.exists(self.log.log_file_path))

    def test_extensionless_file_name_arg(self):
        """
        Ensures .log extension added in case of extensionless log_file param.
        :return: None
        """
        test = Logger(log_file="extensionless")
        self.assertTrue(test.log_file_path.endswith(".log"))
        test.close_log()
        test.delete_log()

    def test_instantiation_from_different_dir(self):
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

    def test_init_arg_error(self):
        """
        Ensures AttributeError is thrown for instantiation attempt with wrong arg.
        :return: None
        """
        with self.assertRaises(AttributeError):
            Logger(log_file="wrong_param.log", name="UNIT_TEST_LOG", log_level="wrong")

    def test_build_path(self):
        """
        Ensures log file build path functionality.
        :return: None
        """
        mock_path = self.log._build_path("test.log")
        log_dir = os.path.join(secrets.get_project_folder(), 'log')
        log_path = os.path.join(log_dir, "test.log")
        self.assertTrue(mock_path == log_path)
        os.remove(mock_path)

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
        comment = " - UNIT_TEST_LOG - INFO - True"
        result = self.log.check_comment_for_timestamp(comment)
        content = self.log.get_content()
        self.assertIn("True", content)
        self.assertIn("INFO", content)
        self.assertTrue(result)

    def test_warning_str_logging(self):
        """
        Test str input for log. Ensure warning function logs properly through time check of INFO log.
        :return: None
        """
        self.log.warning("This is a warning check string")
        comment = " - UNIT_TEST_LOG - WARNING - This is a warning check string"
        result = self.log.check_comment_for_timestamp(comment)
        content = self.log.get_content()
        self.assertIn(comment, content)
        self.assertIn("WARNING", content)
        self.assertTrue(result)

    def test_int_error_logging(self):
        """
        Test int input for log. Ensure error function logs properly through time check of INFO log.
        :return: None
        """
        self.log.error(5)
        comment = " - UNIT_TEST_LOG - ERROR - 5"
        result = self.log.check_comment_for_timestamp(comment)
        content = self.log.get_content()
        self.assertIn("5", content)
        self.assertIn("ERROR", content)
        self.assertTrue(result)

    def test_check_comment_for_timestamp_true(self):
        """
        Ensures check_comment_for_timestamp returns True if comment gets logged at the right time.
        :return: None
        """
        self.log.info("test_check_comment_for_timestamp_true")
        comment = " - UNIT_TEST_LOG - INFO - test_check_comment_for_timestamp_true"
        result = self.log.check_comment_for_timestamp(comment)
        self.assertTrue(result)

    def test_check_comment_for_timestamp_false(self):
        """
        Ensures check_comment_for_timestamp returns False if comment not in log.
        :return: None
        """
        comment = "This comment is not in the log file."
        result = self.log.check_comment_for_timestamp(comment)
        self.assertFalse(result)

    def test_check_comment_for_timestamp_false_wrong_timestamp(self):
        """
        Ensures check_comment_for_timestamp returns False if comment in log but timestamp is off.
        :return: None
        """
        self.log.info("test_check_comment_for_timestamp_true")
        time.sleep(1.2)
        comment = " - UNIT_TEST_LOG - INFO - test_check_comment_for_timestamp_true"
        result = self.log.check_comment_for_timestamp(comment)
        self.assertFalse(result)

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
