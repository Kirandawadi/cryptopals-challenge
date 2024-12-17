import string
import re
import codecs

in_hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


def main():
    # print(hex2str(in_hex))
    # return
    for letter in string.ascii_letters:
        result = xor_string(hex2str(in_hex), letter)
        # print(result)
        # remove ascii control chars
        pretty_result = re.sub(r"[\x00-\x1F]+", "", result)
        # print the result and the corresponding letter used to decode
        print(f"{letter}: {pretty_result}")


def hex2str(s):
    """given an ascii string of single-byte hex literals, interpret as ascii"""
    # return bytes.fromhex(s).decode('ascii')
    bytearray = codecs.decode(s, "hex")
    return str(bytearray, "UTF-8")


def string_xor(s, c):
    """given an ascii string s of hexadecimal values, xor each one by char c"""
    c = ord(c)  # dirty dynamic typing
    return "".join(map(lambda h: chr(ord(h) ^ c), s))


def xor_string(s, c):
    result = ""
    for h in s:
        result += chr(ord(h) ^ ord(c))
    return result


if __name__ == "__main__":
    main()
