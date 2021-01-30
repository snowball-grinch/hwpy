# Sixth question

import re

new_file4 = open("out_sentences_count.txt", "w")
sentences = re.finditer(r"[\".!,?]\s\"*[A-Z]", poem_content)  # Return an iterator of match objects
num_sentences = len([*sentences]) + 2  # 2 -> 1 + 1 -> for python indexing + for considering the last sentence
new_file4.write(str(num_sentences))