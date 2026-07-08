from src.auth import authenticate


def test_valid_login():
    token = authenticate("admin", "password123")

    assert token is not None


def test_invalid_username():
    token = authenticate("wrong", "password123")

    assert token is None


def test_invalid_password():
    token = authenticate("admin", "wrongpassword")

    assert token is None
