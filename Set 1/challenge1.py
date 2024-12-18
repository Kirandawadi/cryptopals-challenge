import codecs
import base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


# Method 1
def hex_encoded_to_base64(hex_string):
    b64_str = codecs.encode(codecs.decode(hex_string, "hex"), "base64")
    b64_str = str(b64_str, "UTF-8")
    return b64_str


# Method 2
def hex_encoded_to_base64_method_2(hex_string):
    raw_bytes = bytearray.fromhex(hex_string)
    b = base64.b64encode(raw_bytes)
    b64_str = b.decode("utf-8")
    return b64_str


print(hex_encoded_to_base64(hex_string=hex_string))
print(hex_encoded_to_base64_method_2(hex_string=hex_string))
