from cryptography.fernet import Fernet
import os

KEY_FILE = "data/key.key"


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key


def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()

    with open(KEY_FILE, "rb") as f:
        return f.read()


key = load_key()
fernet = Fernet(key)


def encrypt(text: str) -> str:
    return fernet.encrypt(text.encode()).decode()


def decrypt(text: str) -> str:
    return fernet.decrypt(text.encode()).decode()

import hashlib

MASTER_FILE = "data/master.key"


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def set_master_password(password: str):
    hashed = hash_password(password)
    with open(MASTER_FILE, "w") as f:
        f.write(hashed)


def check_master_password(password: str) -> bool:
    if not os.path.exists(MASTER_FILE):
        set_master_password(password)
        return True

    with open(MASTER_FILE, "r") as f:
        stored = f.read().strip()

    return stored == hash_password(password)