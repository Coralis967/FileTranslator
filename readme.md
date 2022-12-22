FileTranslator

This project is designed to grab a file (originally a .lua file) and read the file line by line in to memory, where any line has a non-english character it will translate that entire line through Google Translate, and once the file has been completely translated will output a new file in the translated english.

Requires install of pre-release version of googletrans library:
    pip install googletrans==4.0.0rc1