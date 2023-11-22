
import rsa
import os
from base64 import b64encode

def generate_keys(private_key_path, public_key_path):
    """Generate RSA private and public keys and save them to files.

    Args:
        private_key_path (str): The path to save  the private key.
        public_key_path (str): The path to save the public key.
    """
    # Generate a new RSA key pair
    (pubkey, privkey) = rsa.newkeys(2048)  # Adjust the key size as needed (2048 is used here)

    # Save the private key to a file
    with open(private_key_path, 'wb') as priv_file:
        priv_file.write(privkey.save_pkcs1())

    # Save the public key to a file
    with open(public_key_path, 'wb') as pub_file:
        pub_file.write(pubkey.save_pkcs1())


# def generate_license_from_private_key(private_key_path):
#     """Generate a license key using only the private RSA key.

#     Args:
#         private_key_path (str): The path to the private RSA key file.

#     Returns:
#         str: The generated license key.
#     """
#     with open(private_key_path, 'rb') as file:
#         private_key = rsa.PrivateKey.load_pkcs1(file.read())

#     # Generate a random string to be signed
#     random_data = os.urandom(20)  # Change the length as needed for your use case
#     string_to_sign = "This is a license key" + str(random_data)  # Incorporate the random content
#     generated_license = b64encode(rsa.sign(string_to_sign.encode(), private_key, 'SHA-256')).decode()
#     print(generated_license)
#     return generated_license


# # Paths to save the keys
# private_key_path = 'keys/private.pem'
# public_key_path = 'keys/public.pem'

# # # Generate and save the keys
# # generate_keys(private_key_path, public_key_path)
# # print("Keys generated and saved.")

# path = 'keys/private.pem'
# generate_license_from_private_key(path)

# import uuid

# def get_mac_address():
#     mac = uuid.getnode()
#     mac_address = ':'.join(['{:02x}'.format((mac >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
#     return mac_address

# mac_address = get_mac_address()
# print(mac_address)


from datetime import datetime

def get_current_time_date():
    current_date = datetime.now().date()
    return current_date

time_date = get_current_time_date()
print(time_date)
print(len(str(time_date)))

# print(f"{time_date}{mac_address}")






def date_difference(start_date, end_date):
    # Convert date strings to datetime objects
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

    # Calculate the difference
    difference = end_datetime - start_datetime
    return difference

start_date = '2023-04-15'
end_date = str(get_current_time_date())
date_diff = date_difference(start_date, end_date)
print("Difference in days:", int(date_diff.days))




