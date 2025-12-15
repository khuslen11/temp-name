import logging

logging.basicConfig(level=logging.INFO)


def is_valid_login(username, password):
    """
    Validate login input data.
    """
    if username is None or password is None:
        logging.error("Login input is None")
        raise ValueError("Username and password must not be None")

    if not isinstance(username, str) or not isinstance(password, str):
        logging.error("Login input has invalid type")
        raise TypeError("Username and password must be strings")

    if not username or not password:
        logging.warning("Empty login input")
        return False

    logging.info("Login input validated successfully")
    return True


def register_user(username, password):
    """
    Validate registration input data.
    """
    if username is None or password is None:
        logging.error("Registration input is None")
        raise ValueError("Username and password must not be None")

    if not isinstance(username, str) or not isinstance(password, str):
        logging.error("Registration input has invalid type")
        raise TypeError("Username and password must be strings")

    if not username or not password:
        logging.warning("Empty registration input")
        return False

    logging.info("Registration input validated successfully")
    return True