import hashlib

def generate_fingerprinting(data):
    if not isinstance(data, bytes):
        data = data.encode('utf-8')
    hash_obj = hashlib.sha256()
    hash_obj.update(data)
    fingerprinting = hash_obj.hexdigest()
    return fingerprinting

def verifiy_fingerprinting(data, hashedData):
    actual_fingerprint = generate_fingerprinting(data)
    return actual_fingerprint == hashedData

sample_text = 'Hello!'
fingerprint = generate_fingerprinting(sample_text)
print(f'Plain text: {sample_text}\nHashed text: {fingerprint}')

verify_fingerprint = verifiy_fingerprinting(sample_text, fingerprint)
print(f'Compair result: {verify_fingerprint}')

verify_fingerprint = verifiy_fingerprinting("Hello", fingerprint)
print(f'Compair result: {verify_fingerprint}')
