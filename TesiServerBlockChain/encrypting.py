from cryptography.fernet import Fernet
from generate_key import load_key

def encrypt(filename):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    print("")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("*                                           *")
    print("*                Cripto i file              *")
    print("*                                           *")
    print("+++++++++++++++++++++++++++++++++++++++++++++\n")
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        # write the encrypted file
    with open(filename+"_crypted", "wb") as file:
        file.write(encrypted_data)


def decrypt(filename):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
        
