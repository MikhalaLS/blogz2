x = input("Type out a sentence")

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_count = {}
for character in x:
    if character in alphabet:
        if character in letter_count:
            letter_count[character] = letter_count[character] + 1
        else:
            letter_count[character] = 1
keys = letter_count.keys()
#keys.sort()
for character in keys:
    print(character, letter_count[character])
