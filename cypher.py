import sys
import unidecode
import random
import copy


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ü", "u")
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def normalize_text(text):
    normalized_text = []
    for line in text:
        new_line = copy.copy(line)
        new_line = normalize(new_line)
        new_line = new_line.upper()
        normalized_text.append(new_line)
    return normalized_text


def get_charset(text):
    charset = set()
    for line in text:
        for char in line:
            if char.isalnum(): # If a string contains alphanumeric characters, without symbols
                charset.add(char)
    return charset


def all_elements_are_different(list_a, list_b):
    different = True
    for i in range(0, len(list_a)):
        if list_a[i] == list_b[i]:
            different =  False
            break
    return different


def get_random_key(charset):
    original_charlist = list(charset)

    shuffle_charlist = copy.copy(original_charlist)
    while True:
        random.shuffle(shuffle_charlist)
        different = all_elements_are_different(original_charlist, shuffle_charlist)
        if different:
            break
    random_key = [original_charlist, shuffle_charlist]
    return random_key


def get_encryptor(random_key):
    original_charlist = random_key[0]
    shuffle_charlist = random_key[1]
    encryptor = {}
    for i in range(len(original_charlist)):
        att = original_charlist[i]
        val = shuffle_charlist[i]
        encryptor[att] = val
    return encryptor


def encrypt_line(encryptor, line):
    encrypted_chars = []
    for char in line:
        if char in encryptor:
            encrypted_chars.append(encryptor[char])
        else:
            encrypted_chars.append(char)
    encrypted_line = "".join(encrypted_chars)
    return encrypted_line


def encrypt_text(encryptor, normalized_text):
    encrypted_text = []
    for line in normalized_text:
        encrypted_line = encrypt_line(encryptor, line)
        encrypted_text.append(encrypted_line)
    return encrypted_text


def split_string_randomly(text):
    temp_text = copy.copy(text)

    text = []
    while True:
        if len(temp_text) == 0:
            break
        index = random.randint(2, 8)
        text_a = temp_text[:index]
        text.append(text_a)
        temp_text = temp_text[index:]

    new_text = " ".join(text)
    return new_text


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

    input_text = input_file.readlines()
    normalized_text = normalize_text(input_text)
    
    charset = get_charset(normalized_text)
    random_key =  get_random_key(charset)
    encryptor = get_encryptor(random_key)
    
    header = "".join(random_key[0]) + "\n"
    footer = "".join(random_key[1]) + "\n"

    header = split_string_randomly(header)
    footer = split_string_randomly(footer)

    encrypted_text = encrypt_text(encryptor, normalized_text)

    encrypted_text.insert(0, header)
    encrypted_text.append(footer)

    # Debug
    print_text(input_text)
    print_text(normalized_text)
    print_text(encrypted_text)

    # Output
    save_file("normalized_text.txt", normalized_text)
    save_file("encrypted_text.txt", encrypted_text)
  

if __name__ == "__main__":
  main()
