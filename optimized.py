def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def wagner_fischer_optimized(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    
    # Ensure s1 is the shorter string
    if len_s1 > len_s2:
        s1, s2 = s2, s1
        len_s1, len_s2 = len_s2, len_s1

    current_row = list(range(len_s1 + 1))
    
    for i in range(1, len_s2 + 1):
        previous_value = current_row[0]
        current_row[0] = i
        for j in range(1, len_s1 + 1):
            old_value = current_row[j]
            if s2[i - 1] == s1[j - 1]:
                current_row[j] = previous_value
            else:
                current_row[j] = min(previous_value + 1, current_row[j] + 1, current_row[j - 1] + 1)
            previous_value = old_value

    return current_row[len_s1]

def spell_check(word, dictionary):
    suggestions = []

    for correct_word in dictionary:
        distance = wagner_fischer_optimized(word, correct_word)
        suggestions.append((correct_word, distance))

    suggestions.sort(key=lambda x: x[1])
    return suggestions[:5]  # Return top 10 suggestions

# Example usage
if __name__ == "__main__":
    dictionary = load_dictionary("words.txt")
    misspelled_word = "algoritm"
    suggestions = spell_check(misspelled_word, dictionary)
    
    print(f"Top 5 suggestions for '{misspelled_word}':")
    for word, distance in suggestions:
        print(f"{word} (Distance: {distance})")
