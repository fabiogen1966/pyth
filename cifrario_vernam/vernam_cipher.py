def vernam_cipher(message, key):
    """
    Codifica un messaggio usando il cifrario di Vernam (XOR).
    
    Args:
        message (str): Il messaggio da codificare
        key (str): La chiave per la codifica
    
    Returns:
        str: Il messaggio codificato
    """
    result = ""
    key_length = len(key)
    
    for i, char in enumerate(message):
        key_char = key[i % key_length]
        encoded_char = chr(ord(char) ^ ord(key_char))
        result += encoded_char
    
    return result

def vernam_decipher(encrypted_message, key):
    """
    Decifra un messaggio codificato con il cifrario di Vernam.
    
    Args:
        encrypted_message (str): Il messaggio codificato
        key (str): La chiave per la decodifica
    
    Returns:
        str: Il messaggio decodificato
    """
    return vernam_cipher(encrypted_message, key)