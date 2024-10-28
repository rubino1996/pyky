from cpake import generate_kyber_keys, encrypt, decrypt
from Crypto.Random import get_random_bytes
from params import KYBER_SYM_BYTES


def read_from_file(filename):
    with open(filename, 'rb') as file:
        return file.read()


def write_to_file(data, filename):
    with open(filename, 'wb') as file:
        for part in data:
            byte_array = bytes(
                [byte if byte >= 0 else 256 + byte for byte in part])
            file.write(byte_array)


def encrypt_message_in_chunks(pubkey, message, chunk_size, params_k):
    encrypted_chunks = []
    for start in range(0, len(message), chunk_size):
        end = start + chunk_size
        chunk = message[start:end]
        coins = get_random_bytes(KYBER_SYM_BYTES)
        encrypted_chunk = encrypt(chunk, pubkey, coins, params_k=params_k)
        encrypted_chunks.append(encrypted_chunk)
    return encrypted_chunks


def decrypt_message_chunks(private_key, encrypted_chunks, params_k):
    decrypted_message = b""
    for chunk in encrypted_chunks:
        decrypted_chunk = decrypt(chunk, private_key, params_k=params_k)
        decrypted_chunk = decrypted_chunk.rstrip(b'\x00')
        decrypted_message += decrypted_chunk
    return decrypted_message


def test_kyber_message_encryption_decryption(message):
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
    message = read_from_file(
        r"C:\Users\ruben\Documents\NAU\PhD\Spring2024\Kyber\pyky\test.txt")
    test_kyber_message_encryption_decryption(message)
