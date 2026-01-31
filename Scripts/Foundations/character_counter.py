def count_characters(text):
    character_dict = {}
    for character in text:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1

    return character_dict


count_characters("banana")
