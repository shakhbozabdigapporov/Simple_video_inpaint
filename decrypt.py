from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import cv2
import numpy as np



def generate_key(password, salt, key_length=32):
    key = PBKDF2(password, salt, dkLen=key_length)
    return key

def load_image_with_decryption(path, pw):
    with open(path, 'rb') as file:
        data = file.read()
    salt = data[:16]
    iv = data[16:16 + 16]
    encrypted_data = data[16 + 16:]
    key = generate_key(pw.encode(), salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    nparr = np.frombuffer(decrypted_data, np.uint8)
    decrypted_image_data = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    return decrypted_image_data

for i in range(1,20):
    folder = "fire"
    path = f'{folder}/fire ({i}).enc'
    image = load_image_with_decryption(path, "1234")
    cv2.imwrite(f'decrypted_masks/fire({i}).png', image)
print(image.shape)
