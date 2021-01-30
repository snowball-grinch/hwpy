# Seventh question

import re
from one import poem_content

quotes = re.findall(r"\".+", poem_content)

with open("out_quote.txt", "w") as new_file_5:
    for quote in enumerate(quotes):
        new_file_5.write(f"{quote[1]}\n")