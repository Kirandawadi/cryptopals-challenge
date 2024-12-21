import string
import codecs

def main():

    line = f"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    repeating_key_xor(line, key)
    return

def repeating_key_xor(line, key):
    final_output : str = ""
    for i in range(len(line)):
        final_output += chr(ord(line[i]) ^ ord(key[i % 3])).encode('utf-8').hex()
        # print(f"{i} --> {line[i]} --> {key[i % 3]} --> { chr(ord(line[i]) ^ ord(key[i % 3])).encode('utf-8').hex()}")
    print(final_output)

if __name__ == "__main__":
    main()
