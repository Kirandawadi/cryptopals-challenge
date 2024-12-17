def xor_strings(string1, string2):
    bytes1 = string1.encode('utf-8')
    bytes2 = string2.encode('utf-8')

    result_bytes = bytes([a ^ b for a, b in zip(bytes1, bytes2)])
    return result_bytes.hex()

string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"
result = xor_strings(string1, string2)
print(result)