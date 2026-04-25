from typing import List

def contains_duplicate(words: List[str]) -> bool:
    unique_strings = set()

    for word in words:
        if word in unique_strings:
            return True
        unique_strings.add(word)
    
    return False


# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
