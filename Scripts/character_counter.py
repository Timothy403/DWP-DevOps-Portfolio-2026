def count_characters(text):
    character_dict = {}
    for character in text:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    print(character_dict)
    return character_dict


count_characters("banana")
