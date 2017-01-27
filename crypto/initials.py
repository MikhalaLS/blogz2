import sys
def get_initials(fullname):
    splitname = fullname
    splitname = splitname.split()
    initial = ""

    for name in splitname:
        first_letter = name[0]
        first_letter = first_letter.upper()
        initial = initial + first_letter
    return initial

def main():
    get_initials(input("What is the name? "))

if __name__ == '__main__':
    main()
