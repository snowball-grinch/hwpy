# First question

import re

with open("poem.txt", "r") as poem:
    poem_content = poem.read()

words = re.findall(r"\w+", poem_content)
num_words = len(words)
unique_words = set(words)
num_unique_words = len(unique_words)
print(__name__)

with open("out_words_count.txt", "w+") as new_file:
    new_file.write(f"{num_words}\n{num_unique_words}")