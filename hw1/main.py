import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

#encrypt/decrypt with AES-GCM mode
def encrypt_decrypt_aes_gcm(plaintext):
    key = os.urandom(32)
    iv = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    start = time.time()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    end = time.time()
    elapsed_time= end - start
    print(f"encrypt speed of AES-GCM: {len(plaintext)/elapsed_time:.2f} B/sec")
    tag = encryptor.tag
    
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()

    with open("encrypted_AES_GCM.bin", "wb") as enc_file:
        enc_file.write(ciphertext)
    with open("Decrypted_AES_GCM.txt", "wb") as dec_file:
        dec_file.write(decrypted)   
    
    return decrypted, ciphertext

#encrypt/decrypt with AES-CTR mode
def encrypt_decrypt_aes_ctr(plaintext):
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    start = time.time()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    end = time.time()
    elapsed_time= end - start
    print(f"encrypt speed of AES-CTR: {len(plaintext)/elapsed_time:.2f} B/sec")
    
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()
    
    with open("encrypted_AES_CTR.bin", "wb") as enc_file:
        enc_file.write(ciphertext)
    with open("Decrypted_AES_CTR.txt", "wb") as dec_file:
        dec_file.write(decrypted)   
    
    return decrypted, ciphertext

#encrypt/decrypt with ChaCha20
def encrypt_decrypt_chacha20(plaintext):
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.ChaCha20(key, iv), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    
    start = time.time()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    end = time.time()
    elapsed_time= end - start
    print(f"encrypt speed of ChaCha20: {len(plaintext)/elapsed_time:.2f} B/sec")

    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()
    
    with open("encrypted_chacha20.bin", "wb") as enc_file:
        enc_file.write(ciphertext)
    with open("Decrypted_chacha20.txt", "wb") as dec_file:
        dec_file.write(decrypted)   
    
    return decrypted, ciphertext

def verify_text(plaintext, decrypted, mode):
    assert plaintext == decrypted, f"{mode} Encrypt failed."
    print(f"{mode} Encrypt success.")

filename = 'data.txt'
with open(filename, 'rb') as file:
    plaintext = file.read()

print("\nAES-GCM")
decrypted, ciphertext = encrypt_decrypt_aes_gcm(plaintext)
verify_text(plaintext, decrypted,'AES-GCM')
print("\nAES-CTR")
decrypted, ciphertext = encrypt_decrypt_aes_ctr(plaintext)
verify_text(plaintext, decrypted,'AES-CTR')
print("\nChaCha20")
decrypted, ciphertext = encrypt_decrypt_chacha20(plaintext)
verify_text(plaintext, decrypted,'ChaCha20')
