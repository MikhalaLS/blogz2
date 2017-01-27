sentence = input("Write a sentence ")

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
character_count = {}
for character in sentence:
    if character in alphabet:
        if character in character_count:
            character_count[character] = character_count[character] + 1
        else:
            character_count[character] = 1
keys = character_count.keys()
keys = sorted(keys)
for character in keys:
    print(character, character_count[character])
