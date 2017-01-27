from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    output = ""
    keynum = []
    a = 0
    for j in key:
        keynum += [alphabet_position(j)]
    for i in text:
        if i.isalpha() == True:
            output = output + rotate_character(keynum[a % len(keynum)], i)
            a = a + 1
        else:
            output = output + i

    return output

def main():
    text = input("Type a message:")
    key = input("Encryption key:")
    print(encrypt(text, key))

if __name__ == '__main__':
    main()
