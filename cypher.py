import sys
import unicodedata
import random
import copy


def strip_accents(text):
  try:
    text = unicode(text, 'utf-8')
  except NameError: # unicode is a default on python 3 
    pass

  text = unicodedata.normalize('NFD', text)\
    .encode('ascii', 'ignore')\
    .decode("utf-8")

  return str(text)


def save_file(label_name, text_list):
  output_file = open(label_name, "w")
  output_file.writelines(text_list)
  output_file.close()


def get_charset(text_list):
  omited_char = [" ", "\n", ".", ",", ";", ":", "!", "?", "¿", "«", "»", '"', "'", "-"]
  charset = set()
  for line in text_list:
    for char in line:
      if char not in omited_char:
        charset.add(char)
  return charset


def get_chardict(charset):
  chardict = {}
  original_charlist = list(charset)
  
  shuffle_charlist = copy.copy(original_charlist)
  random.shuffle(shuffle_charlist)
  
  print("Acharlist = ", "".join(original_charlist))
  print("Bcharlist = ", "".join(shuffle_charlist))
  #for i in range(0, len(charlist)):
  #  elem = 
  #  print(elem)

def normalize_text(text_list):
  text_list_normalized = []
  for line in text_list:
    new_line = copy.copy(line)
    new_line = strip_accents(new_line)
    new_line = new_line.upper()
    text_list_normalized.append(new_line)
  return text_list_normalized


def main():
  filename = sys.argv[1]
  input_file = open(filename, 'r')
  input_text_list = input_file.readlines()
  normalized_text_list = normalize_text(input_text_list)

  save_file("normalized_input_text.txt", normalized_text_list)
  charset = get_charset(normalized_text_list)
  chardict =  get_chardict(charset)
  

if __name__ == "__main__":
  main()


