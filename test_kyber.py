"""
test_kyber.py

This script demonstrates how to use the Kyber encryption scheme to encrypt and decrypt a text file
in chunks. It generates a Kyber key pair, encrypts a text file in chunks, writes the encrypted message
to a binary file, decrypts it, and then writes the decrypted message to a text file. The script also
validates that the decrypted message matches the original.

Functions:
    - read_from_file(filename): Reads a file in binary mode.
    - write_to_file(data, filename): Writes binary or text data to a file.
    - encrypt_message_in_chunks(pubkey, message, chunk_size, params_k): Encrypts a message in chunks.
    - decrypt_message_chunks(private_key, encrypted_chunks, params_k): Decrypts encrypted chunks.
    - test_kyber_message_encryption_decryption(message): Executes the full encryption and decryption
      process and validates the integrity of the decrypted message.

Usage:
    Place the plaintext file to be encrypted at the specified path in the script or modify the path
    accordingly. Run this script to generate encrypted and decrypted files as part of the test.
"""

from cpake import generate_kyber_keys, encrypt, decrypt
from Crypto.Random import get_random_bytes
from params import KYBER_SYM_BYTES


def read_from_file(filename):
    """
    Reads the contents of a file in binary mode.

    :param filename: The path to the file to be read.
    :return: The binary content of the file as bytes.
    """
    with open(filename, 'rb') as file:
        return file.read()


def write_to_file(data, filename):
    """
    Writes data to a file in binary mode. Each chunk in `data` is converted to a byte array before writing.

    :param data: List of byte arrays or bytes to write to the file.
    :param filename: The path to the file where data will be written.
    """
    with open(filename, 'wb') as file:
        for part in data:
            byte_array = bytes(
                [byte if byte >= 0 else 256 + byte for byte in part])
            file.write(byte_array)


def encrypt_message_in_chunks(pubkey, message, chunk_size, params_k):
    """
    Encrypts a message in chunks using Kyber encryption.

    :param pubkey: The public key used for encryption.
    :param message: The message to be encrypted, in bytes.
    :param chunk_size: The size of each chunk, in bytes.
    :param params_k: Kyber parameter set (security level).
    :return: A list of encrypted chunks.
    """
    encrypted_chunks = []
    for start in range(0, len(message), chunk_size):
        end = start + chunk_size
        chunk = message[start:end]
        coins = get_random_bytes(KYBER_SYM_BYTES)
        encrypted_chunk = encrypt(chunk, pubkey, coins, params_k=params_k)
        encrypted_chunks.append(encrypted_chunk)
    return encrypted_chunks


def decrypt_message_chunks(private_key, encrypted_chunks, params_k):
    """
    Decrypts a list of encrypted chunks using Kyber decryption.

    :param private_key: The private key used for decryption.
    :param encrypted_chunks: A list of encrypted message chunks.
    :param params_k: Kyber parameter set (security level).
    :return: The decrypted message, as bytes.
    """
    decrypted_message = b""
    for chunk in encrypted_chunks:
        decrypted_chunk = decrypt(chunk, private_key, params_k=params_k)
        decrypted_chunk = decrypted_chunk.rstrip(b'\x00')
        decrypted_message += decrypted_chunk
    return decrypted_message


def test_kyber_message_encryption_decryption(message):
    """
    Tests the Kyber encryption and decryption of a message, writing results to files and verifying
    integrity.

    - Generates Kyber keys.
    - Encrypts the message in chunks.
    - Writes the encrypted message to a binary file.
    - Decrypts the message and writes the result to a text file.
    - Validates that the decrypted message matches the original.

    :param message: The original message to be encrypted and decrypted.
    """
    private_key, public_key = generate_kyber_keys(params_k=2)
    KYBER_MAX_CHUNK_SIZE = 32  # size in Bytes for Kyber

    encrypted_message_chunks = encrypt_message_in_chunks(
        public_key, message, KYBER_MAX_CHUNK_SIZE, params_k=2)

    # Write encrypted chunks to file
    write_to_file(encrypted_message_chunks, "encrypted_message.bin")

    decrypted_message = decrypt_message_chunks(
        private_key, encrypted_message_chunks, params_k=2)

    # Write decrypted message to file
    write_to_file([decrypted_message], "decrypted_message.txt")

    assert message == decrypted_message, "Decrypted message does not match the original"
    print("Test Passed: The decrypted message matches the original.")


if __name__ == "__main__":
    # Specify the path to the plaintext file to encrypt
    message = read_from_file("C:Data/input_file.txt")
    test_kyber_message_encryption_decryption(message)

