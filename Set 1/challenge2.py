import codecs
string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"

def xor_two_hex_strings(string1, string2):
    """
    Given two hex-encoded strings, XOR them byte by byte and return the resulting hex string.
    "1c0111001f010100061a024b53535009181c" ^ "686974207468652062756c6c277320657965" -> "746865206b696c6c696e6720796f757320657965"

    Args:
        string1 (str): The first hex-encoded string.
        string2 (str): The second hex-encoded string.

    Returns:
        str: The resulting hex string after XOR operation.
    """
    # Convert both hex strings to raw bytes
    bytes1 = bytes.fromhex(string1) # Gives b'\x1c\x01\x11\x00\x1f\x01\x01\x00\x06\x1a\x02KSSP\t\x18\x1c'
    bytes2 = bytes.fromhex(string2) # Gives b"hit the bull's eye"

    # XOR the raw bytes byte by byte using zip
    xored_bytes = bytes(a ^ b for a, b in zip(bytes1, bytes2)) # Gives b"the kid don't play"

    # Convert the result back to a hex string and return
    return xored_bytes.hex()

print(xor_two_hex_strings(string1, string2))

