# Crystals-Kyber in Python - Enhanced for Text File Encryption and Decryption

## Overview

This repository is a modified version of the [original Crystals-Kyber Python implementation](https://github.com/asdfjkl/pyky), intended to support encryption and decryption of text files using the Kyber algorithm. These modifications include updates to existing files and a new script, `test_kyber.py`, specifically designed for text file processing.

### Original Repository

The original repository was a toy implementation of Crystals-Kyber in Python, ported from the [official reference](https://github.com/asdfjkl/pyky) . It was intended for educational purposes and is not hardened against timing or other side-channel attacks.

### Modifications in This Repository

- **Changes to `cpake.py`**: Enhanced to integrate with the new text file encryption functionalities.
- **Changes to `poly.py`**: Adjusted polynomial handling for compatibility with the `test_kyber.py` script.
- **New File - `test_kyber.py`**: This script allows users to encrypt and decrypt text files using Kyber keys, specifically developed to handle chunked file encryption.

## Security Note

This repository is not intended for production use, as it is not hardened against side-channel attacks. It is provided for learning and experimental purposes.

## Installation and Setup

1. **Clone this repository**:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Install dependencies**:
    Ensure you have Python installed along with any necessary dependencies. You can use `pip` to install the `Crypto` package if it’s not already installed:
    ```bash
    pip install pycryptodome
    ```

## Usage

The main script, `test_kyber.py`, includes functions for reading a text file, encrypting it in chunks using the Kyber public key, and decrypting it with the private key. Here’s an example usage:

1. **Generate Keys**:
    ```python
    from cpake import generate_kyber_keys
    private_key, public_key = generate_kyber_keys(params_k=2)
    ```

2. **Encrypt a Text File**:
    Use the `encrypt_message_in_chunks` function to encrypt a text message or file.

3. **Decrypt the Encrypted File**:
    Use the `decrypt_message_chunks` function to decrypt the previously encrypted file.
