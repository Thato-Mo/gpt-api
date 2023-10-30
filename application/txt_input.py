import sys

def open_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    print(text)
    return text

def main(arg):
    open_text_file(arg)

if __name__ == "__main__":
    main(sys.argv[1])