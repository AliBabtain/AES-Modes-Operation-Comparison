# AES Modes of Operation Comparison
---
This project aims to compare the performance of three modes of operation used in the Advanced Encryption Standard (AES) algorithm: Galois/Counter Mode (GCM), Cipher-Block Chaining (CBC), and Counter (CTR).

The implementation uses the cryptography library in Python to perform the encryption and decryption operations. The encryption and decryption time of the data is measured for each mode, and the results are compared and plotted. The data is padded using the PKCS7 padding method, and the key size used in the encryption is 128 bits.

The modes of operation are compared by encrypting and decrypting a sample data, and measuring the time taken for each operation. The encryption and decryption times are plotted to compare the performance of each mode.

**The code is written in Python and requires the following libraries:**

* os
* matplotlib
* cryptography
* binascii
* termcolor
* timeit

---

## Running the code:
**The code can be run using the following command:**
```bash
python3 aes_modes_comparison.py
```

This will generate the encryption and decryption results, and plot the comparison of the modes of operation.

---

## Output:

**Encryption Modes Performance:**

<img width="639" alt="Encryption Modes Performance" src="https://user-images.githubusercontent.com/42214099/218317070-8b54e755-128a-4eec-a518-677a5b19e37c.png">

**Decryption Modes Performance:**

<img width="639" alt="Decryption Modes Performance" src="https://user-images.githubusercontent.com/42214099/218317091-ac93878f-7c41-41a3-a28e-177b9ae903f0.png">

**Terminal output:**

<img width="737" alt="Terminal output" src="https://user-images.githubusercontent.com/42214099/218317098-b1c7e20c-ff11-41d1-99d7-2f6d8cee4c1f.png">
