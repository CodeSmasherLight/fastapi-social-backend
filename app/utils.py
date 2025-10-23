from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended() # to create password hash

def hash_password(password: str):
    return pwd_context.hash(password)