# Sixth question

import re
from one import poem_content

sentences = re.finditer(r"[\".!,?]\s\"*[A-Z]", poem_content)  # Return an iterator of match objects
num_sentences = len([*sentences]) + 1  # 1 -> 1 -> for considering the last sentence

with open("out_sentences_count.txt", "w") as new_file4:
    new_file4.write(str(num_sentences))
