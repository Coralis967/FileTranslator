from functions import *

def main():
    language_file = request_language_file()
    translated_list = translate_file_to_list(language_file)
    output_new_file(translated_list)


if __name__ == '__main__':
    main()