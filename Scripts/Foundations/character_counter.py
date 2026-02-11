def count_characters(text=""):
    # Providing a default "" prevents a crash if no argument is passed
    character_dict = {}
    
    for character in text:
        character_dict[character] = character_dict.get(character, 0) + 1

    return character_dict
