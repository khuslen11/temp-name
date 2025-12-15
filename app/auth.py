def is_valid_login(username, password):
    """
    Returns True if both username and password are not empty.
    Otherwise returns False.
    """
    if not username or not password:
        return False
    return True

def register_user(username, password):
    """
    Returns True if registration data is valid.
    Returns False if username or password is empty.
    """
    if not username or not password:
        return False
    return True