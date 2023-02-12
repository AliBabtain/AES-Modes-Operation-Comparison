import os
import matplotlib.pyplot as plt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import binascii
from termcolor import colored
import timeit

# ########################################## GENERATE KEY FUNC ##########################################
def generate_key(key_size):
    return os.urandom(key_size // 4)
# ########################################## ENC FUNC ##########################################
def encrypt_data(mode, key, data, iv):
    if mode == "gcm":
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        encryptor = cipher.encryptor()
        return (encryptor.update(padded_data) + encryptor.finalize(), encryptor.tag)
    else:
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv) if mode == "cbc" else modes.CTR(iv), backend=default_backend())
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    encryptor = cipher.encryptor()
    return  encryptor.update(padded_data) + encryptor.finalize()
# ########################################## DEC FUNC ##########################################
def decrypt_data(mode, key, encrypted_data, iv , tag):
    if mode == "gcm":
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv,tag),backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()

        return  unpadder.update(padded_data) + unpadder.finalize()
    if mode == "cbc":
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv),backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(padded_data) + unpadder.finalize()
    if mode == "ctr":
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv),backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(padded_data) + unpadder.finalize()
    return
# ########################################## PRINTING FUNC ##########################################
def print_enc_data(mode, enc_time, data):
    print(colored('Encrypted data: ', 'light_cyan', attrs=["bold"]) + colored(str(binascii.hexlify(data)), 'light_yellow'))
    print(colored('Encrytpion Time: ', 'light_cyan', attrs=["bold"]) + colored(str(enc_time) + " ms", 'light_grey') + "\n")

def print_dec_data(mode, dec_time, data):
    print(colored('Decrypted data: ', 'light_cyan', attrs=["bold"]) + colored(str(data), 'light_green'))
    print(colored('Decrytpion Time: ', 'light_cyan', attrs=["bold"]) + colored(str(dec_time) + " ms", 'light_grey'))
# ########################################## PLOT FUNC ##########################################
def plot_Modes(gcm_enc_time, cbc_enc_time, ctr_enc_time, gcm_dec_time, cbc_dec_time, ctr_dec_time, num_repeated_test):
    # Plot results
    fig1, ax1 = plt.subplots()
    ax1.bar(["GCM", "CBC","CTR"], [gcm_enc_time , cbc_enc_time, ctr_enc_time], color=["Maroon", "blue", "Teal"])
    ax1.set_xlabel("Encryption Modes(Number of test:"+str(num_repeated_test)+ ")")
    ax1.set_ylabel("Time (milliseconds)")
    ax1.set_title("Encryption Modes Comparison")
    ax1.set_ylim(0.000, 5)
    for i, v in enumerate([gcm_enc_time, cbc_enc_time, ctr_enc_time]):
        ax1.annotate(format(v, '.3f'), xy=(i, v), xycoords='data',
                xytext=(0, 20), textcoords='offset points',
                ha='center', va='bottom',
                fontweight='bold')

    fig2, ax2 = plt.subplots()
    ax2.bar(["GCM", "CBC","CTR"], [gcm_dec_time , cbc_dec_time, ctr_dec_time], color=["Maroon", "blue", "Teal"])
    ax2.set_xlabel("Decryption Modes(Number of test:"+str(num_repeated_test)+ ")")
    ax2.set_ylabel("Time (milliseconds)")
    ax2.set_title("Decryption Modes Comparison")
    ax2.set_ylim(0.000, 5)
    for i, v in enumerate([gcm_dec_time, cbc_dec_time, ctr_dec_time]):
        ax2.annotate(format(v, '.3f'), xy=(i, v), xycoords='data',
                xytext=(0, 20), textcoords='offset points',
                ha='center', va='bottom',
                fontweight='bold')
    plt.show()
# ########################################## MAIN FUNC ##########################################
if __name__ == "__main__":
    key = generate_key(128)
    iv = os.urandom(16)

    num_repeated_test = 20

    gcm_enc_time = None
    cbc_enc_time = None
    ctr_enc_time = None

    gcm_dec_time = None
    cbc_dec_time = None
    ctr_dec_time = None

    data = b"This is some secret data"
    print(colored('\n*********************** (', 'light_grey', attrs=["bold"]) + colored('PLAIN-TEXT', 'light_green', attrs=["bold"]) + colored(') **********************', 'light_grey', attrs=["bold"]))
    print(colored('Data: ', 'light_cyan', attrs=["bold"]) + colored(str(data), 'light_green'))
    # ########################################## GCM MODE ##########################################
    # -> ENCRYPTION:
    mode = "gcm"
    print(colored('\n\n*********************** (', 'light_grey', attrs=["bold"]) + colored('GALOIS/COUNTER MODE', 'light_red', attrs=["bold"]) + colored(') **********************', 'light_grey', attrs=["bold"]))
    encrypted_data, tag = encrypt_data(mode, key, data , iv)
    gcm_enc_time = timeit.timeit(stmt='encrypt_data(mode, key, data , iv)', globals=globals(), number=num_repeated_test)
    gcm_enc_time = gcm_enc_time * 1000
    print_enc_data(mode, gcm_enc_time, encrypted_data)
    # -> DECRYPTION:
    decrypted_data = decrypt_data(mode, key, encrypted_data , iv, tag)
    gcm_dec_time = timeit.timeit(stmt='decrypt_data(mode, key, encrypted_data , iv, tag)', globals=globals(), number=num_repeated_test)
    gcm_dec_time = gcm_dec_time * 1000
    print_dec_data(mode, gcm_dec_time, decrypted_data)
    # ########################################## CBC MODE ##########################################
    # -> ENCRYPTION:
    mode = "cbc"
    print(colored('\n\n*********************** (', 'light_grey', attrs=["bold"]) + colored('CIPHER-BLOCK CHAINING', 'light_red', attrs=["bold"]) + colored(') **********************', 'light_grey', attrs=["bold"]))
    encrypted_data = encrypt_data(mode, key, data , iv)
    cbc_enc_time = timeit.timeit(stmt='encrypt_data(mode, key, data , iv)', globals=globals(), number=num_repeated_test)
    cbc_enc_time = cbc_enc_time * 1000
    print_enc_data(mode, cbc_enc_time, encrypted_data)
    # -> DECRYPTION:
    decrypted_data = decrypt_data(mode, key, encrypted_data , iv , tag)
    cbc_dec_time = timeit.timeit(stmt='decrypt_data(mode, key, encrypted_data , iv, tag)', globals=globals(), number=num_repeated_test)
    cbc_dec_time = cbc_dec_time * 1000
    print_dec_data(mode, cbc_dec_time, decrypted_data)
    # ########################################## CTR MODE ##########################################
    # -> ENCRYPTION:
    mode = "ctr"
    print(colored('\n\n*********************** (', 'light_grey', attrs=["bold"]) + colored('COUNTER', 'light_red', attrs=["bold"]) + colored(') **********************', 'light_grey', attrs=["bold"]))
    encrypted_data = encrypt_data(mode, key, data , iv)
    ctr_enc_time = timeit.timeit(stmt='encrypt_data(mode, key, data , iv)', globals=globals(), number=num_repeated_test)
    ctr_enc_time = ctr_enc_time * 1000
    print_enc_data(mode, ctr_enc_time, encrypted_data)
    # -> DECRYPTION:
    decrypted_data = decrypt_data(mode, key, encrypted_data , iv, tag)
    ctr_dec_time = timeit.timeit(stmt='decrypt_data(mode, key, encrypted_data , iv, tag)', globals=globals(), number=num_repeated_test)
    ctr_dec_time = ctr_dec_time * 1000
    print_dec_data(mode, ctr_dec_time, decrypted_data)
    # ########################################## PLOT ##########################################
    plot_Modes(gcm_enc_time, cbc_enc_time, ctr_enc_time, gcm_dec_time, cbc_dec_time, ctr_dec_time, num_repeated_test) 

   
