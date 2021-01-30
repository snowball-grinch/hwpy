# Second question

import re
import collections


def word_frequency(text: str) -> dict:
    words_list = re.findall(r"\w+", text)
    output = collections.Counter(words_list)
    return output
