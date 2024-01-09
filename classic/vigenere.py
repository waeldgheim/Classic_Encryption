def vigenere(text, key, mode):
    def vigenere_encrypt(plain_text, key):
        result = ""
        key_length = len(key)

        for i in range(len(plain_text)):
            char = plain_text[i]
            if char.isalpha():
                # Calculate the shift based on the current key character
                shift = ord(key[i % key_length].upper()) - ord('A')
                if char.islower():
                    # Encrypt lowercase letters
                    result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                else:
                    # Encrypt uppercase letters
                    result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                # Preserve non-alphabetic characters
                result += char

        return result

    def vigenere_decrypt(cipher_text, key):
        result = ""
        key_length = len(key)

        for i in range(len(cipher_text)):
            char = cipher_text[i]
            if char.isalpha():
                # Calculate the shift based on the current key character
                shift = ord(key[i % key_length].upper()) - ord('A')
                if char.islower():
                    # Decrypt lowercase letters
                    result += chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
                else:
                    # Decrypt uppercase letters
                    result += chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            else:
                # Preserve non-alphabetic characters
                result += char

        return result

    # Check the mode and perform either encryption or decryption
    if mode.lower() == "encrypt":
        return vigenere_encrypt(text, key)
    elif mode.lower() == "decrypt":
        return vigenere_decrypt(text, key)
