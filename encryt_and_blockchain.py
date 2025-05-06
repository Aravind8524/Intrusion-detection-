import shutil

from cryptography.fernet import Fernet
import os
def generate_key(key_file="encryption_key.key"):
    key = Fernet.generate_key()
    with open(key_file, "wb") as key_out:
        key_out.write(key)
    print(f"Encryption key saved to {key_file}")
    return key
def load_key(key_file="encryption_key.key"):
    if os.path.exists(key_file):
        with open(key_file, "rb") as key_in:
            return key_in.read()
    else:
        print("Key file not found! Generating a new one.")
        return generate_key(key_file)
key = load_key()
class ecc_encryption:
    def encrypt_file(self,input_file, output_file):
        cipher = Fernet(key)
        with open(input_file, "rb") as file:
            file_data = file.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(output_file, "wb") as enc_file:
            enc_file.write(encrypted_data)
    def decrypt_file(self,encrypted_file, output_file):
        cipher = Fernet(key)
        with open(encrypted_file, "rb") as enc_file:
            encrypted_data = enc_file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(output_file, "wb") as dec_file:
            dec_file.write(decrypted_data)
    def store_block(self,filename,id):
        dir1 = '1'
        dir2 = '2'
        dir3 = '3'
        dir4 = '4'
        dir5 = '5'
        if not os.path.exists(dir1):
            os.makedirs(dir1)
        if not os.path.exists(dir2):
            os.makedirs(dir2)
        if not os.path.exists(dir3):
            os.makedirs(dir3)
        if not os.path.exists(dir4):
            os.makedirs(dir4)
        if not os.path.exists(dir5):
            os.makedirs(dir5)
        extension = os.path.splitext(filename)[1]
        for xx in range(1,6):
            dst=os.path.join(str(xx),str(id)+""+extension)
            shutil.copy(filename,dst)

    def match_file(self,id, file):
        try:
            extension = os.path.splitext(file)[1]

            dir1 = '1'
            dir2 = '2'
            dir3 = '3'
            dir4 = '4'
            dir5 = '5'
            file1 = os.path.join(dir1, (str(id) + "" + extension))
            file2 = os.path.join(dir2, (str(id) + "" + extension))
            file3 = os.path.join(dir3, (str(id) + "" + extension))
            file4 = os.path.join(dir4, (str(id) + "" + extension))
            file5 = os.path.join(dir5, (str(id) + "" + extension))

            f1 = open(file1, "r")
            d1 = f1.read()

            f2 = open(file2, "r")
            d2 = f2.read()

            f3 = open(file3, "r")
            d3 = f3.read()

            f4 = open(file4, "r")
            d4 = f4.read()

            f5 = open(file5, "r")
            d5 = f5.read()
            if d1 == d2 == d3 == d4 == d5:
                return "ok"
            return "Modified"
        except:
            return "Modified"







