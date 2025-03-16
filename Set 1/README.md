## Crypto Challenge Set 1
This is the qualifying set. We picked the exercises in it to ramp developers up gradually into coding cryptography, but also to verify that we were working with people who were ready to write code.

This set is relatively easy. With one exception, most of these exercises should take only a couple minutes. But don't beat yourself up if it takes longer than that. It took Alex two weeks to get through the set!

If you've written any crypto code in the past, you're going to feel like skipping a lot of this. Don't skip them. At least two of them (we won't say which) are important stepping stones to later attacks.

### 1. Convert hex to base64
> Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
1. Decode the hex string into raw bytes.
2. Then, encode those raw bytes into a Base64 string.
---
### 2. Fixed XOR
1. Convert both hex strings to raw bytes using `bytes.fromhex()`.
2. Use `zip` to pair the corresponding bytes from both strings.
3. XOR each byte pair and store the result.
4. Convert the XOR-ed bytes back to a hex string and return the result.
---
### 3. Single-byte XOR cipher
1. Convert the given hex string to ASCII text using `hex2str()`.
2. Iterate through all possible single-character keys (from `string.ascii_letters`), and XOR the input string with each character using the `xor_string()` function.
3. Ensure the result of each XOR operation consists only of printable characters.
4. For each printable result, score it based on English letter frequencies using the `score_english_text()` function.
5. Keep track of the highest score, the corresponding key, and the decrypted message.
6. Print the key that yields the highest score and the decrypted plaintext message.

---
### 4. Detect single-character XOR
1. Open and read the file `4.txt` line by line.
2. For each line (hex-encoded ciphertext), attempt to find the decryption key and plaintext by calling the `find_decryption_key()` function.
3. In `find_decryption_key()`, convert the hex string to an ASCII string using `hex2str()`, then XOR each character in the string with all possible byte values (0-255) using the `xor_string()` function.
4. Check if the result after XOR is printable. If it is, score the result using the `score_english_text()` function, which rates the English text based on letter frequencies, penalizes gibberish, and rewards word-like structure.
5. Keep track of the key, plaintext, and score that yield the highest score for each ciphertext.
6. After processing all lines, print the key, plaintext, and ciphertext associated with the highest score found across all lines in the file.

---
### 5. Implement repeating-key XOR
- Initialize an empty string `final_output` to store the XOR results.
- Loop through each character in the input `line`.
    - XOR each character with the corresponding character from the repeating `key` (using modulo to repeat the key).
    - Convert the XOR result to a hexadecimal string and append it to `final_output`.
- Print the final XOR result in hexadecimal format.


---
### 6. Break repeating-key XOR
---
### 7. AES in ECB mode
---
### 8. Detect AES in ECB mode
---