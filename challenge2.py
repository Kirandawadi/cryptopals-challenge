import codecs
string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"


def xor_two_hex_strings(string1, string2):

    xored = int(string1, 16) ^ int(string2, 16)
    xored = hex(xored).replace("0x", "")
    return xored


print(xor_two_hex_strings(string1, string2))

