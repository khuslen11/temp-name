def is_valid_login(username, password):
    """
    Check whether both username and password are provided.

    Returns:
        bool: True if both values are non-empty, otherwise False.
    """
    return bool(username and password)


def register_user(username, password):
    """
    Validate user registration input.

    Returns:
        bool: True if registration data is valid, otherwise False.
    """
    return bool(username and password)
