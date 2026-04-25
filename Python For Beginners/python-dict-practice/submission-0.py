from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    occurrencesOfWords = {}

    for character in word:
        if character in occurrencesOfWords:
            occurrencesOfWords[character] += 1
        else:
            occurrencesOfWords[character] = 1
    
    return occurrencesOfWords




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
