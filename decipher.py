import sys


def get_random_key(header, footer):
    header = header.replace(" ", "").replace("\n", "")
    footer = footer.replace(" ", "").replace("\n", "")
    random_key = [header, footer]
    return random_key


def get_decryptor(random_key):
    original_charlist = random_key[0]
    shuffle_charlist = random_key[1]
    decryptor = {}
    for i in range(len(original_charlist)):
        att = shuffle_charlist[i]
        val = original_charlist[i]
        decryptor[att] = val
    return decryptor


def decrypt_line(decryptor, line):
    decrypted_chars = []
    for char in line:
        if char in decryptor:
            decrypted_chars.append(decryptor[char])
        else:
            decrypted_chars.append(char)
    decrypted_line = "".join(decrypted_chars)
    return decrypted_line


def decrypt_text(decryptor, encrypted_text):
    decrypted_text = []
    for line in encrypted_text:
        decrypted_line = decrypt_line(decryptor, line)
        decrypted_text.append(decrypted_line)
    return decrypted_text


def print_text(text):
    max_len = 0
    for line in text:
        print(line, end="")
        if (len(line) > max_len):
            max_len = len(line)  
    last_line = "*" * max_len
    print(last_line)


def save_file(filename, text):
    output_file = open(filename, "w")
    output_file.writelines(text)
    output_file.close()


def main():
    filename = sys.argv[1]
    input_file = open(filename, 'r')

    encrypted_text = input_file.readlines()
    header = encrypted_text.pop(0)
    footer = encrypted_text.pop(-1)

    random_key = get_random_key(header, footer)
    decryptor = get_decryptor(random_key)
    decrypted_text = decrypt_text(decryptor, encrypted_text)

    # Debug
    print_text(decrypted_text)

    # Output
    save_file("decrypted text.txt", decrypted_text)
  

if __name__ == "__main__":
  main()
