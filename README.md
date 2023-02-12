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