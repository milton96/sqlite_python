from hashlib import sha256

def to_sha256(string: str) -> str:
    hash_string = sha256(string.encode()).hexdigest()
    return hash_string