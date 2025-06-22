---
title: "Encryption Notes"
date: "2025-03-21"
# last_modified_at: "2025-03-21"
description: "Encryption Notes"
categories: [
  coding
]
tags: [
  dev, python, encryption, cryptography, decryption fernet, aes, aes-128, aes-256, pbkdf2, key derivation, password based key derivation, encode, decode, bytes, bytestring
]
---

# Symmetric Data Encryption
In symmetric encryption, the same key is used to encrypt and decrypt data

## Fernet Encryption
Uses `AES-128` encryption, with a 128-bit key

### Fernet Encryption with Random Key
- A random Fernet key is generated via `Fernet.generate_key()`
- Should be sufficient in comparison to `AES-256` as both should take more time and resources to crack than is feasible

The key is used to encrypt data, usually that data is a string, here we use `plain_string: str`
- Create a `Fernet` object from `key_bytes: bytes` via `fernet: Fernet = Fernet(key_bytes)`
- The encryption is from bytes to bytes, so you will need to convert your data to bytes first via `plain_bytes: bytes = plain_string.encode()`
- You can then encrypt via `encrypted_bytes: bytes = fernet.encrypt(plain_bytes)`
- It is common to save encrypted data in string, so converting it back is common via `encrypted_string: str = encrypted_bytes.decode()`

The key is used to decrypt data, usually that data is a string, here we use `encrypted_string: str`
- Create a `Fernet` object from `key_bytes: bytes` via `fernet: Fernet = Fernet(key_bytes)`
- The decryption is from bytes to bytes, so you will need to convert your data to bytes first via `encrypted_bytes: bytes = encrypted_string.encode()`
- You can then decrypt via `decrypted_bytes: bytes = fernet.decrypt(encrypted_bytes)`
- It is common to read decrpyted data as a string, so converting it back is common via `decrypted_string: str = decrypted_bytes.decode()`

```python

# < ========================================================
# < Imports
# < ========================================================

from cryptography.fernet import Fernet

# < ========================================================
# < Functionality
# < ========================================================

def encrypt_string(plain_string: str, key_bytes: bytes) -> str:
    """Encrypts a string using Fernet using key in bytes"""
    fernet: Fernet = Fernet(key_bytes)
    plain_bytes: bytes = plain_string.encode()
    encrypted_bytes: bytes = fernet.encrypt(plain_bytes)
    encrypted_string: str = encrypted_bytes.decode()
    return encrypted_string

def decrypt_string(encrypted_string: str, key_bytes: bytes,) -> str:
    """Decrypts a string using Fernet using key in bytes"""
    fernet: Fernet = Fernet(key_bytes)
    encrypted_bytes: bytes = encrypted_string.encode()
    decrypted_bytes: bytes = fernet.decrypt(encrypted_bytes)
    decrypted_string: str = decrypted_bytes.decode()
    return decrypted_string

# < ========================================================
# < Entry Point
# < ========================================================

def main() -> None:
    """Entry point function for the application"""
    text_string: str = input("Provide text to be encrypted: ")
    random_key_bytes: bytes = Fernet.generate_key()
    print(f"{random_key_bytes = }")
    encrypted_string: str = encrypt_string(text_string, random_key_bytes)
    print(f"{encrypted_string = }")
    decrypted_string: str = decrypt_string(encrypted_string, random_key_bytes)
    print(f"{decrypted_string = }")

# < ========================================================
# < Execution
# < ========================================================

if __name__ == "__main__":
    main()
```

### Fernet Encryption with Password 
---
You can use `Fernet` encryption with a password by combining normal `Fernet` functionality with `PBKDF2` (password-based key derivation function 2), generating a key from a password and salt. Using the same password and salt in the `PBKDF2` hasing process will always produce the same result for `Fernet` to use. `PBKDF2` is normally used for producing password hashes, which are one-way encryptions of plain text passwords to a hash. In that process you'd be checking a password against a stored hash to see if they match. In our case we aren't looking to match, we are simply generating the hash each time, and inserting that hash as a key for `Fernet` to use, meaning that you do not need to store a random key from `Fernet.generate_key()`, as you can generate the same key dynamically every time, provided you remember the salt and password you used for the `PBKDF2` hashing process used the first time.

```python

# < ========================================================
# < Imports
# < ========================================================

import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pwinput import pwinput

# < ========================================================
# < Functionality
# < ========================================================

def get_hashed_password(password: str, salt: str) -> bytes:
    """Hash a given password using salt, via an asymmetric / one-way hashing function"""
    password_bytes: bytes = password.encode()
    salt_bytes: bytes = salt.encode()
    kdf: PBKDF2HMAC = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt_bytes,
        iterations = 100000
    )
    return kdf.derive(password_bytes)

def get_fernet_key(password: str, salt: str) -> bytes:
    """Generate a Fernet key as base64-encoded bytes from a given password and salt"""
    hash: bytes = get_hashed_password(password, salt)
    key: bytes = base64.urlsafe_b64encode(hash)
    return key

def encrypt_string(plain_string: str, key_bytes: bytes) -> str:
    """Encrypts a string using Fernet using key in bytes"""
    fernet: Fernet = Fernet(key_bytes)
    plain_bytes: bytes = plain_string.encode()
    encrypted_bytes: bytes = fernet.encrypt(plain_bytes)
    encrypted_string: str = encrypted_bytes.decode()
    return encrypted_string

def decrypt_string(encrypted_string: str, key_bytes: bytes,) -> str:
    """Decrypts a string using Fernet using key in bytes"""
    fernet: Fernet = Fernet(key_bytes)
    encrypted_bytes: bytes = encrypted_string.encode()
    decrypted_bytes: bytes = fernet.decrypt(encrypted_bytes)
    decrypted_string: str = decrypted_bytes.decode()
    return decrypted_string

# < ========================================================
# < Entry Point
# < ========================================================

def main() -> None:
    """Entry point function for the application"""
    text_string: str = input("Provide text to be encrypted: ")
    generated_key_bytes: bytes = get_fernet_key("one", "two")
    print(f"{generated_key_bytes = }")
    encrypted_string: str = encrypt_string(text_string, generated_key_bytes)
    print(f"{encrypted_string = }")
    decrypted_string: str = decrypt_string(encrypted_string, generated_key_bytes)
    print(f"{decrypted_string = }")

# < ========================================================
# < Execution
# < ========================================================

if __name__ == "__main__":
    main()
```

#### A Note on PBKDF2
`PBKDF2` was designed for key derivation but is commonly used for password hashing / storage. When working with a user database with passwords, you might want to store the passwords as hashes, in this use case you would apply a cryptographic hash function many times (usually thousands / millions of iterations). `PBKDF2` is an asymmetric system, or a one-way function, and not an encryption method, you cannot reverse the hashing process. This means that you can store all of the data on how you created the hash, such as salt, iterations and algorithm etc. because you cannot mathematically derive the original password from the hash regardless. 

| user_id | username | salt (Base64) | iterations | hash_algorithm | key_length | password_hash (Base64) |
|---------|----------|---------------|------------|----------------|------------|------------------------|
| 1 | alice92 | rQ7LPz8Kx9UdBeKw | 210000 | sha256 | 32 | Xvs8pte2sMZpBzLq6vKHNkH4DEsZ9qPUWb5LjmMnHYQ= |

One common attack is a `rainbow table attack`, which uses a pre-computed table of hashes, usually generated from common passwords, and checks the `rainbow table` against a database to check for matches. If unique salting is not used then this attack is very effective as hashes are **deterministic**, whereas when salting is used you would need a table for each unique salt as using a random salt in the hashing process means that two passwords do not produce the same hash. Here `PBKDF2` is used to defend against `brute force` and `rainbow table` attacks, as the hashing process is computationally expensive, and generating a table for each unique salt would be completely unfeasible.

In theory, storing the salts, or hashing process information separately to the hashed passwords would create more "defence in depth" as you'd need multiple security breaches for a hacker to even attempt to crack passwords. But in practical terms you can store them together in most cases, a salt does not need to be secret in order to be effective, it simply needs to be random.

In simple terms, if you only store the password hash, and never the plain text password, and the hasing process used then a user can input a password and it will be checked against the hashed password using the same process to check if it matches, thereby authenticating the user. If a bad actor were to steal a `PBKDF2` hashed password it would be useless until cracked as the site doesn't accept the hashed password, it only takes plain text passwords and hashes them so you'd need to crack the password. If the hashing process used say 200,000 iterations for hashing they'd need to apply the hashing function 200,000 times for each possible password combination, and check the resulting hash against the stolen password hash.

#### A Note on PBKDF2 Alternatives
The `bcrypt` password hashing function requires more computational power and is considered significantly stronger against many modern attacks

Snippet about `PBKDF2` from Wikipedia:
> PBKDF2 applies a pseudorandom function, such as hash-based message authentication code (HMAC), to the input password or passphrase along with a salt value and repeats the process many times to produce a derived key, which can then be used as a cryptographic key in subsequent operations.