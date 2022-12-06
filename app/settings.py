import os
from Crypto.Protocol.KDF import PBKDF2

__all__ = ["DB_PATH", "GLOBAL_SALT", "ROOT_KEY", "ROOT_STANDART_PASSWORD", "MESSAGES_STYLE"]


def generate_root_key(salt, root_password):
    key = PBKDF2(root_password, salt, dkLen=32)
    return key



ROOT_STANDART_PASSWORD = "root"

DB_PATH = r"data\database\db.db"
GLOBAL_SALT =  b'W\xb5\x03\x98\\\x08}\x15H\xc1n\xd1\xefW2\xe6\xee\xfa\x08\xbdD:\xc3\xfaV\x17\xa8\xc7\xeeg\xcd}'
ROOT_KEY = generate_root_key(GLOBAL_SALT, ROOT_STANDART_PASSWORD)
MESSAGES_STYLE = """background-color: #242424;
            font-family: Inter;
            color: #fafafa;
            font-size: 16px;"""

if __name__ == '__main__':
    print(DB_PATH)