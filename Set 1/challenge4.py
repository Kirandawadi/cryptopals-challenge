import string
import codecs
import re

def main():

    highest_score_overall : float = 0
    required_key_overall : str = ""
    required_plaintext_overall : str = ""
    required_ciphertext : str = ""
    with open('4.txt', 'r') as file:
        for line in file:
            hex_str = line.strip()
            key, plaintext, score = find_decryption_key(hex_str)
            if (score > highest_score_overall):
                highest_score_overall = score
                required_key_overall = key
                required_plaintext_overall = plaintext
                required_ciphertext = hex_str

        print((f"Overall:\n"
              f"The required key is: {required_key_overall}\n"
              f"The required plaintext is: {required_plaintext_overall}"
              f"The required 60-character string is {required_ciphertext}"))


def find_decryption_key(input_string):
    highest_score : float = 0
    required_key : str = ""
    required_plaintext : str = ""
    input_str = hex2str(input_string)
    if input_str is not None:
        for character in range(256):
            result = xor_string(input_str, character)
            #Check if the result is printable or not
            if not all(c in string.printable for c in result):
                continue
            score = score_english_text(result)
            if score > highest_score:
                highest_score = score
                required_key = chr(character)
                required_plaintext = result

    return required_key, required_plaintext, highest_score

def hex2str(s):
    """ given an ascii string of single-byte hex literals, interpret as ascii"""
    bytearray = codecs.decode(s, "hex")
    try:
        return str(bytearray, 'UTF-8')
    except UnicodeDecodeError:
        return

def xor_string(s, c):
    """ given an ascii string s, xor each one by char c"""
    result = ""
    for char in s:
        result += chr(ord(char) ^ c)
    return result

def score_english_text(s):
    """score a text based on English letter frequency: a very basic implementation"""

    # Frequency table for English letters (based on relative frequencies)
    english_frequencies = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
    'P': 1.93, 'B': 1.49, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
    'Q': 0.10, 'Z': 0.07
    }

    score = 0
    for char in s.upper():
        if char in english_frequencies:
            score += english_frequencies[char]

    # Penalize gibberish: count non-alphabetic characters
    non_alpha = len(re.findall(r'[^A-Za-z\s]', s))
    gibberish_penalty = non_alpha * 5

    # Reward word-like structure
    common_words = ['the', 'a', 'and', 'of', 'it', 'that', 'it', 'was']
    word_score = sum(len(re.findall(rf'\b{word}\b', s.lower())) for word in common_words) * 10

    return score - gibberish_penalty + word_score

if __name__ == "__main__":
    main()
