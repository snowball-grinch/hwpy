# Seventh question

import re

new_file_5 = open("out_quote.txt", "w")
quotes = re.findall(r"\".+", poem_content)
for quote in enumerate(quotes):
    new_file_5.write(f"{quote[1]}\n")