import base64
import codecs
import re
import string


def calculate_hamming_distance(string1, string2):
    """Calculate the Hamming distance between two strings or byte sequences."""
    if type(string1) != type(string2):
        raise TypeError("Inputs mismatch!")
    if isinstance(string1, str) and isinstance(string2, str):
        str1_bin = str2binary(string1)
        str2_bin = str2binary(string2)
    elif isinstance(string1, bytes) and isinstance(string2, bytes):
        str1_bin = raw_bytes_to_binary(string1)
        str2_bin = raw_bytes_to_binary(string2)
    else:
        raise TypeError(
            "Ensure you are calculating hamming distance for supported types only"
        )
    # Here we truncated the first string to be the length of second string
    edit_distance = sum(
        char1 != char2
        for char1, char2 in zip(str1_bin[: len(str2_bin)], str2_bin, strict=True)
    )
    return edit_distance


def str2binary(s):
    return "".join(format(ord(i), "08b") for i in s)


def raw_bytes_to_binary(s):
    return "".join(format(byte, "08b") for byte in s)


def get_raw_bytes_from_file(file_name):
    with open(file_name, "r") as file:
        b64_encoded = file.read()
        xor_encrypted_string_bytes = base64.b64decode(b64_encoded)
        try:
            xor_encrypted_string = xor_encrypted_string_bytes.decode("utf-8")
        except UnicodeDecodeError:
            print("Not valid UTF-8")

        # Print byte values to differentiate control chars from regular characters
        # Print control chars as "."
        # for byte in raw_bytes:
        #     print(f"Byte: {byte:02X} - Char: {chr(byte) if 32 <= byte <= 126 else '.'}")
    return xor_encrypted_string_bytes


def find_key_size(raw_bytes):
    d_min = 1000000
    probable_key_size = 0.00
    # print(raw_bytes)
    for key_size in range(3, 45):
        values = []
        for i in range(0, len(raw_bytes), key_size):
            str1 = raw_bytes[i : i + key_size]
            str2 = raw_bytes[i + key_size : i + 2 * key_size]
            d = calculate_hamming_distance(str1, str2)
            normalized_d = float(d / key_size)
            values.append(normalized_d)
        avg = sum(values) / len(values)
        if avg < d_min:
            d_min = avg
            probable_key_size = key_size
    return probable_key_size


def find_key(raw_bytes, keysize):
    """Find the most probable repeating-key XOR key."""
    blocks = []
    for i in range(0, len(raw_bytes), keysize):
        blocks.append(raw_bytes[i : i + keysize])
    blocks.pop(len(blocks) - 1)  # Just a try for now, verify later
    transposed_blocks = []
    collected_bytes = []
    for byte in range(keysize):
        # print(f"Processing byte {byte}")
        for block in blocks:
            collected_bytes.append(chr(block[byte]))
        merged_block = "".join(collected_bytes)
        transposed_blocks.append(merged_block)
        collected_bytes = []

    key = ""
    for t in transposed_blocks:
        required_key, required_plaintext, highest_score = find_decryption_key(t)
        key += required_key
    return key


def find_decryption_key(input_str):
    """Find the single-byte XOR key that produces the most readable plaintext."""
    highest_score: float = 0
    required_key: str = ""
    required_plaintext: str = ""
    if input_str is not None:
        for character in range(256):
            result = xor_string(input_str, character)
            # Check if the result is printable or not
            if not all(c in string.printable for c in result):
                continue
            score = score_english_text(result)
            if score > highest_score:
                highest_score = score
                required_key = chr(character)
                required_plaintext = result

    return required_key, required_plaintext, highest_score


def repeating_key_xor(line, key):
    final_output: str = ""
    for i in range(len(line)):
        final_output += chr(ord(line[i]) ^ ord(key[i % len(key)]))
    return final_output


def xor_string(s, c):
    """given an ascii string s, xor each one by char c"""
    result = ""
    for char in s:
        result += chr(ord(char) ^ c)
    return result


def score_english_text(s):
    """score a text based on English letter frequency: a very basic implementation"""

    # Frequency table for English letters (based on relative frequencies)
    english_frequencies = {
        "E": 12.70,
        "T": 9.06,
        "A": 8.17,
        "O": 7.51,
        "I": 6.97,
        "N": 6.75,
        "S": 6.33,
        "H": 6.09,
        "R": 5.99,
        "D": 4.25,
        "L": 4.03,
        "C": 2.78,
        "U": 2.76,
        "M": 2.41,
        "W": 2.36,
        "F": 2.23,
        "G": 2.02,
        "Y": 1.97,
        "P": 1.93,
        "B": 1.49,
        "V": 0.98,
        "K": 0.77,
        "J": 0.15,
        "X": 0.15,
        "Q": 0.10,
        "Z": 0.07,
    }

    score = 0
    for char in s.upper():
        if char in english_frequencies:
            score += english_frequencies[char]

    # Penalize gibberish: count non-alphabetic characters
    non_alpha = len(re.findall(r"[^A-Za-z\s]", s))
    gibberish_penalty = non_alpha * 5

    # Reward word-like structure
    common_words = ["the", "a", "and", "of", "it", "that", "it", "was"]
    word_score = (
        sum(len(re.findall(rf"\b{word}\b", s.lower())) for word in common_words) * 10
    )

    return score - gibberish_penalty + word_score


def main():
    file_name = "6.txt"
    raw_bytes = get_raw_bytes_from_file(file_name)
    KEYSIZE = find_key_size(raw_bytes)
    KEY = find_key(raw_bytes, KEYSIZE)
    print(f"The repeating XOR key is: \"{KEY}\"\n")
    final_text = repeating_key_xor(raw_bytes.decode("utf-8"), KEY)
    print(f"Decrypted text is: \n {final_text}")


if __name__ == "__main__":
    main()
