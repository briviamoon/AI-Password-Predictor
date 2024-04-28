import hashlib
import secrets

def generate_salt(length=16):
    """
    Generates a random salt for hashing.

    Args:
        length (int): Length of the salt in bytes. Default is 16.

    Returns:
        bytes: Random salt.
    """
    return secrets.token_bytes(length)

def hash_password(password, salt=None):
    """
    Hashes the input password using a salt.

    Args:
        password (str): Input password to be hashed.
        salt (bytes): Salt for hashing. If None, a new salt will be generated.

    Returns:
        bytes: Hashed password.
    """
    if salt is None:
        salt = generate_salt()
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hashed_password, salt

def verify_password(password, hashed_password, salt):
    """
    Verifies if the input password matches the hashed password using the provided salt.

    Args:
        password (str): Input password to be verified.
        hashed_password (bytes): Hashed password.
        salt (bytes): Salt used for hashing.

    Returns:
        bool: True if the password is verified, False otherwise.
    """
    new_hashed_password, _ = hash_password(password, salt)
    return secrets.compare_digest(new_hashed_password, hashed_password)
