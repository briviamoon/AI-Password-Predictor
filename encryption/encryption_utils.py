import os
from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a new encryption key.

    Returns:
        bytes: Encryption key.
    """
    return Fernet.generate_key()

def encrypt_data(data, key):
    """
    Encrypts the input data using the provided key.

    Args:
        data (str): Input data to be encrypted.
        key (bytes): Encryption key.

    Returns:
        bytes: Encrypted data.
    """
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    """
    Decrypts the encrypted data using the provided key.

    Args:
        encrypted_data (bytes): Encrypted data.
        key (bytes): Encryption key.

    Returns:
        str: Decrypted data.
    """
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data
