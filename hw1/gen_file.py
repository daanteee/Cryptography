import os 
import random
import string

def generate_file(filename ,size):
    chars = string.ascii_letters + string.digits
    with open(filename, 'w') as file:
        while os.path.getsize(filename) < size:
            file.write(''.join(random.choice(chars) for _ in range(1024)))

filename = 'data.txt'
size = 100 * 1024 * 1024  # 100 MB

generate_file(filename, size)