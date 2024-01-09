def create_monoalphabetic_cipher(key):
    # Check if the key has exactly 26 characters
    if len(key) != 26:
        raise ValueError("Key must contain all 26 letters of the alphabet")

    # Convert the key to uppercase for consistency
    key = key.upper()

    # Create a dictionary to represent the monoalphabetic cipher
    cipher = {}
    for i in range(26):
        cipher[chr(65 + i)] = key[i]
    return cipher

def monoalphabetic(text, key, mode):
    def monoalphabetic_cipher(plaintext, key):
        # Create the monoalphabetic cipher based on the provided key
        cipher = create_monoalphabetic_cipher(key)
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                # Encrypt alphabetic characters
                if char.islower():
                    ciphertext += cipher[char.upper()].lower()
                else:
                    ciphertext += cipher[char]
            else:
                # Preserve non-alphabetic characters
                ciphertext += char
        return ciphertext

    def monoalphabetic_decipher(ciphertext, key):
        # Create the monoalphabetic cipher based on the provided key
        cipher = create_monoalphabetic_cipher(key)

        # Create the inverse cipher for decryption
        inverse_cipher = {v: k for k, v in cipher.items()}
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                # Decrypt alphabetic characters
                if char.islower():
                    plaintext += inverse_cipher[char.upper()].lower()
                else:
                    plaintext += inverse_cipher[char]
            else:
                # Preserve non-alphabetic characters
                plaintext += char
        return plaintext
    
    # Check the mode and perform either encryption or decryption
    if mode.lower() == "encrypt":
        return monoalphabetic_cipher(text, key)
    elif mode.lower() == "decrypt":
        return monoalphabetic_decipher(text, key)
