"""
Module: secrets.py

This module is designed to store sensitive information, such as passwords.

Important:
    - Keep this module secure and do not expose it to the public.
    - Ensure that only authorized personnel have access to this file.

Example:
    import secrets
    db_password = secrets.get_db_password()

Functions:
    - get_api_key(): Retrieves the API key securely.
    - get_database_password(): Retrieves the database password securely.

Note:
    Make sure to add this file to your '.gitignore' or equivalent configuration
    to prevent accidental exposure of sensitive information in version control systems.
"""

PROJECT_FOLDER = 'C:\\users\\dblin\\PycharmProjects\\WebScraping_and_MonteCarloSim_gwjz4t'


def get_project_folder() -> str:
    """
    Retrieves str of project's absolute path securely
    used in:
        - logger.py
        - proxy_handler.py
        - logger_test.py
        - proxy_handler_test.py
    :return: str absolute path of project folder
    """
    return PROJECT_FOLDER
