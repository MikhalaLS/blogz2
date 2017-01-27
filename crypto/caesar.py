from sys import argv, exit
from helpers import alphabet_position, rotate_character

def user_input_is_valid(cl_args):
    if len(cl_args) < 2:
        return False

    if cl_args[1].isdigit() == False:
        return False

    return True


def encrypt(text, rot):
    something = ""
    for i in text:
        if i.isalpha() == True:
            something = something + rotate_character(rot, i)
        else:
            something = something + i

    return something


def main():
    if user_input_is_valid(argv) == True:
        input_text = input("Write a sentence to be encrypted ")
        rotation = int(argv[1])
        print(encrypt(input_text, rotation))

    else:
        print("usage: python3 caesar.py n")
        exit()



if __name__ == '__main__':
    main()
