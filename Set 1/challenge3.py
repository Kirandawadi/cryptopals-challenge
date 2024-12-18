import string
import codecs
input_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
bytearray = codecs.decode(input_string, 'hex')
# print(bytearray)
print(str(bytearray, 'UTF-8'))

def xor_strings(string1, string2):
    bytes1 = string1.encode('utf-8')
    bytes2 = string2.encode('utf-8')

    result_bytes = bytes([a ^ b for a, b in zip(bytes1, bytes2)])
    return result_bytes.hex()


for character in string.ascii_letters:
    xored_against = character * 34
    # print(xored_against)
    xored = xor_strings(input_string, xored_against)
    # print(xored)
    
    # xored = int(input_string, 16) ^ int(xored_against, 16)
    # xored = hex(xored).replace("0x", "")
    # print(codecs.decode(xored, 'hex'))
# def plaintext_scoring(text):
#     score = 0
#     return score

