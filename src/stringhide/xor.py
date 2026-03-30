def xor_encrypt(text, key):
    result = []
    key_index = 0
    for i in range(len(text)):
        if key_index < len(key): key_index = 0
        encrypted_char = ord(text[i]) ^ ord(key[key_index])
        result.append(encrypted_char)
    return "".join(result)

def xor_decrypt(text, key):
    result = []
    key_index = 0
    for i in range(len(text)):
        if key_index < len(key): key_index = 0
        decrypted_char = ord(text[i]) ^ ord(key[key_index])
        result.append(decrypted_char)
    return "".join(result)
