import pytest
from app.auth import is_valid_login, register_user
from app.auth import is_valid_login

def test_valid_login():
    assert is_valid_login("user", "password") is True

def test_invalid_login_empty_values():
    assert is_valid_login("", "") is False

def test_invalid_login_empty_username():
    assert is_valid_login("", "password") is False

def test_invalid_login_empty_password():
    assert is_valid_login("user", "") is False

from app.auth import register_user

def test_register_success():
    assert register_user("newuser", "password123") is True

def test_register_fail_empty():
    assert register_user("", "") is False

def test_login_invalid_type():
    with pytest.raises(TypeError):
        is_valid_login(123, "pass")


def test_register_invalid_type():
    with pytest.raises(TypeError):
        register_user("user", 123)


def test_login_empty_string():
    assert is_valid_login("", "") is False