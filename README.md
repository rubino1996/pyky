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
  (https://github.com/rubino1996/pyky.git)

