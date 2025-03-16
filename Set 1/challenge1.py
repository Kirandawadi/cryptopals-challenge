import codecs
import base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


def hex2str(s):
    """
    Given an ASCII string of single-byte hex literals, interpret it as ASCII.
    "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d" -> "I'm killing your brain like a poisonous mushroom"

    Args:
        s (str): A string containing hexadecimal-encoded data (hex literals).

    Returns:
        str: The ASCII string representation of the decoded hex input.
        If the input is not valid UTF-8, returns None.
    """
    bytearray = codecs.decode(s, "hex") # Gives b"I'm killing your brain like a poisonous mushroom"
    try:
        return str(bytearray, "UTF-8") #This converts bytearray to printable string
    except UnicodeDecodeError:
        return


def str2b64(s):
    """
    Converts a string to its Base64-encoded equivalent.
    "I'm killing your brain like a poisonous mushroom" -> "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    Args:
        s (str): The string to be encoded.

    Returns:
        str: The Base64-encoded version of the input string.
    """
    b64_bytes = base64.b64encode(s.encode("utf-8")) # Base64 encoding works on byte data, not directly on strings.
    b64_str = b64_bytes.decode("utf-8")
    return b64_str


def method_2(hex_string):
    """
    Converts a hex-encoded string to a Base64-encoded string using bytearray.
    "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d" -> "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    Args:
        s (str): A string containing hexadecimal-encoded data (hex literals).

    Returns:
        str: The Base64-encoded string obtained from the hex input.
    """
    raw_bytes = bytearray.fromhex(hex_string)
    b = base64.b64encode(raw_bytes) # Base64 encoding works on byte data, not directly on strings.
    b64_str = b.decode("utf-8")
    return b64_str


def main():
    ascii_text = hex2str(hex_string)
    b64_encoded = str2b64(ascii_text)
    print(b64_encoded)
    print(method_2(hex_string))


if __name__ == "__main__":
    main()
