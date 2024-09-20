def load_mapping(file_path):
    mapping = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if '=' in line: 
                key, value = line.strip().split('=')
                mapping[key] = value 
    return mapping


def remove_punctuation(languages):
    punctuation_mark = [':', ';', '::', '/', '*', '()', 
                        '?', '።', '፣', '፥', '፦', '፧', '፨', '፤', '፠', '፦']
    for mark in punctuation_mark:
        languages = languages.replace(mark, '')
    return languages


def convert_text(input_text, mapping):
    converted_text = []
    for char in input_text:
        converted_text.append(mapping.get(char, char))
    return ''.join(converted_text) 


def calculate_word_overlap(text1: str, text2: str) -> float:
    words1 = set(text1.split())
    words2 = set(text2.split())
    
    shared_words = words1.intersection(words2)
    total_unique_words = len(words1.union(words2))
    
    return (len(shared_words) / total_unique_words) * 100 if total_unique_words > 0 else 0


# Main program
if __name__ == "__main__":
    mapping_dict = load_mapping('words.txt')

    with open('Amharic text.txt', 'r', encoding='utf-8') as file:
        amharic_text = file.read()

    with open('Tigrigna text.txt', 'r', encoding='utf-8') as file:
        tigrigna_text = file.read()

    converted_amharic_text = convert_text(amharic_text, mapping_dict)
    converted_tigrigna_text = convert_text(tigrigna_text, mapping_dict)

    amharic_characters = remove_punctuation(converted_amharic_text)
    tigrigna_characters = remove_punctuation(converted_tigrigna_text)
    amharic_characters = set(amharic_characters)
    tigrigna_characters = set(tigrigna_characters)

    # Find shared and unique characters
    shared_characters = amharic_characters.intersection(tigrigna_characters)
    unique_amharic = amharic_characters - tigrigna_characters
    unique_tigrigna = tigrigna_characters - amharic_characters

    # Calculate similarity percentage
    total_unique = len(amharic_characters.union(tigrigna_characters))
    phoneme_overlap = (len(shared_characters) / total_unique) * 100 if total_unique > 0 else 0

    # Calculate word overlap
    word_overlap = calculate_word_overlap(converted_amharic_text, converted_tigrigna_text)

    # Output results
    
    print("\nShared Characters:", shared_characters)
    print("Unique Amharic Characters:", unique_amharic)
    print("Unique Tigrigna Characters:", unique_tigrigna)
    print(f"Word Overlap : {word_overlap:.2f}%")
    print(f"phoneme_overlap: {phoneme_overlap:.2f}%")
    
    