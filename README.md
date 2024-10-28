# Crystals-Kyber in Python - Enhanced for Text File Encryption and Decryption

## Overview

This repository is a modified version of the [original Crystals-Kyber Python implementation](https://github.com/asdfjkl/pyky), intended to support encryption and decryption of text files using the Kyber algorithm. These modifications include updates to existing files and a new script, `test_kyber.py`, specifically designed for text file processing.

### Original Repository

The original repository was a toy implementation of Crystals-Kyber in Python, ported from the [official reference](https://github.com/asdfjkl/pyky) . It was intended for educational purposes and is not hardened against timing or other side-channel attacks.

### Modifications in This Repository

- **Changes to `cpake.py`**: changed the return to "Bytes" from the decrypt function
- **Changes to `poly.py`**: Adjusted polynomial handling for compatibility with the `test_kyber.py` script.
- **New File - `test_kyber.py`**: This script allows users to encrypt and decrypt text files using Kyber keys, specifically developed to handle chunked file encryption.


## Installation and Setup

1. **Clone this repository**:
  (https://github.com/rubino1996/pyky.git)

## Usage
1. The test_kyber.py script allows you to encrypt and decrypt a text file.

2. Encrypt and Decrypt a Text File

**This script will:**

- Generate Kyber key pairs.
- Encrypt a text file (test.txt) in chunks.
- Save the encrypted message to encrypted_message.bin.
- Decrypt the encrypted message back to a new file, decrypted_message.txt.

  
**Steps to Run**

- Place the plaintext file (test.txt) in the root of the repository, or specify the file path as needed.
- Run the encryption and decryption process: python test_kyber.py


**Script Breakdown**

- read_from_file(filename): Reads the plaintext file.
- write_to_file(data, filename): Writes data to a binary or text file.
- encrypt_message_in_chunks(pubkey, message, chunk_size, params_k): Encrypts the file in chunks.
- decrypt_message_chunks(private_key, encrypted_chunks, params_k): Decrypts the chunks and restores the original message.
- test_kyber_message_encryption_decryption(message): Executes the end-to-end encryption and decryption.
