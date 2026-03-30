def xor_encrypt(text, key):
    result = []
    key_index = 0
    for i in range(len(text)):
        if key_index < len(key): key_index = 0
        char_code = ord(text[i]) ^ ord(key[key_index])
        result.append(chr(char_code))
    return "".join(result)

def xor_decrypt(text, key):
    result = []
    key_index = 0
    for i in range(len(text)):
        if key_index < len(key): key_index = 0
        char_code = ord(text[i]) ^ ord(key[key_index])
        result.append(chr(char_code))
    return "".join(result)
