import random

def generate_key(text):
    """Genera una chiave random della stessa lunghezza del testo."""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789àáèéìíòóùú"
    return ''.join(random.choice(chars) for _ in range(len(text)))

def vernam_cipher(text, key):
    """
    Cifrario di Vernam con caratteri alfanumerici e accentati.
    Perfettamente simmetrico: cifra e decifra con la stessa funzione.
    """
    if len(text) != len(key):
        raise ValueError("Testo e chiave devono avere la stessa lunghezza")
    
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789àáèéìíòóùú"
    result = ""
    
    for i in range(len(text)):
        if text[i] == ' ':
            result += ' '
        else:
            text_pos = chars.index(text[i])
            key_pos = chars.index(key[i])
            cipher_pos = (text_pos + key_pos) % len(chars)
            result += chars[cipher_pos]
    
    return result

def vernam_decipher(text, key):
    """
    Funzione di decifratura per il cifrario di Vernam.
    """
    if len(text) != len(key):
        raise ValueError("Testo e chiave devono avere la stessa lunghezza")
    
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789àáèéìíòóùú"
    result = ""
    
    for i in range(len(text)):
        if text[i] == ' ':
            result += ' '
        else:
            text_pos = chars.index(text[i])
            key_pos = chars.index(key[i])
            cipher_pos = (text_pos - key_pos) % len(chars)
            result += chars[cipher_pos]
    
    return result