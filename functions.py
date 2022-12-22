import io
from googletrans import Translator

#TODO allow language selection, currently auto detects source and translates to english.
def translate_line(line):
    translator = Translator()
    for letter in line:
        if ord(letter) > 255:
            translator.translate(line)
            return line
    return line

#TODO maybe add a progress counter.
def translate_file_to_list(language_file):
    translated_list = []
    total_lines = count_lines(language_file)
    with io.open(language_file, 'r', encoding = 'utf-8') as old_file:
        line = old_file.readline()
        count = 0
        while line:
            try:
                translated_list.append(translate_line(line))
                line = old_file.readline()
                print(f"Current Line: {count}/{total_lines}")
                count += 1
            except UnicodeDecodeError:
                return "UnicodeDecodeError, check the input text encoding."
    return translated_list

def request_language_file():
    language_file = input("Which file would you like to translate?: ")
    return language_file

#TODO build output function to create a new file with same encoding
#ensure file is same format as original
def output_new_file(translated_list):
    pass

def count_lines(file):
    with io.open(file, 'r', encoding = 'utf-8') as old_file:
        total_lines = len(old_file.readlines())
    return total_lines


