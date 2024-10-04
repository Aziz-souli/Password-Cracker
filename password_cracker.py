import hashlib

def crack_sha1_hash(hash, use_salts = False):
    with open('top-10000-passwords.txt', 'r') as f:
        passwords = [line.strip() for line in f]
    if not use_salts :
        for password in passwords:
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
            if hashed_password == hash:
                return password
    else :
        with open("known-salts.txt",'r') as s :
            salts = [line.strip() for line in  s]
        for password in passwords:
            for salt in salts :
                hashed_password1 = hashlib.sha1((salt+password).encode()).hexdigest()
                hashed_password2 = hashlib.sha1((password+salt).encode()).hexdigest()
                if hashed_password1 == hash:
                    return password
                if hashed_password2 == hash:
                    return password
    return "PASSWORD NOT IN DATABASE"
