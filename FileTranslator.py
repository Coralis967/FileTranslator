import io
from googletrans import Translator

def list_append(line):
    for letter in line:
        if ord(letter) > 255:
            translator.translate(line)
            voyeur_list.append(line)
        else:
            voyeur_list.append(line)
    return 


def main():
    voyeur_list = []
    with io.open('Voyeur copy.lua', 'r', encoding = 'utf-8') as voyeur_lua:
        line = voyeur_lua.readline()
        count = 1
        while line:
            try:
                voyeur_list.append(line)
                line = voyeur_lua.readline()
                count += 1
            except UnicodeDecodeError:
                print("we done fucked up and got a UnicodeDecodeError, check the input text encoding.")
    translator = Translator()
    for row in voyeur_list:
        for letter in row:
            if ord(letter) > 255:
                print(translator.translate(row))
                break







if __name__ == '__main__':
    main()
