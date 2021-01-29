import collections
import re

# First question

poem = open("poem.txt", "r")
poem_content = poem.read()
words = re.findall(r"\w+", poem_content)
num_words = len(words)
new_file = open("out_words_count.txt", "w+")
unique_words = set(words)
num_unique_words = len(unique_words)
new_file.write(f"{num_words}\n{num_unique_words}")

# ........................................................
# Second question


def word_frequency(text: str) -> dict:
    words_list = re.findall(r"\w+", text)
    output = collections.Counter(words_list)
    return output


# .........................................................
# Third question

new_file_2 = open("out_most_frequent.txt", "w")
cn = collections.Counter(words)
most_common_list = cn.most_common(10)
for i, j in enumerate(most_common_list):
    new_file_2.write(f"{i+1}. {j[0]}           {j[1]}\n")

# ...........................................................
# Fourth question

ord_dict = collections.OrderedDict()
dic_word_frequency = word_frequency(poem_content)
longest_words = sorted(dic_word_frequency, key=lambda x: len(x), reverse=True)

for word in longest_words[0: 5]:
    ord_dict[word] = dic_word_frequency[word]

# .............................................................
# Fifth question

new_file_3 = open("out_capital_words.txt", "w")
for word in unique_words:
    if word.istitle() or word.isupper():
        new_file_3.write(f"{word} ({dic_word_frequency[word]})\n")

# ..............................................................
# Sixth question

new_file4 = open("out_sentences_count.txt", "w")
sentences = re.finditer(r"[\".!,?]\s\"*[A-Z]", poem_content)  # Return an iterator of match objects
num_sentences = len([*sentences]) + 2  # 2 -> 1 + 1 -> for python indexing + for considering the last sentence
new_file4.write(str(num_sentences))

# ...............................................................
# Seventh question

new_file_5 = open("out_quote.txt", "w")
quotes = re.findall(r"\".+", poem_content)
for quote in enumerate(quotes):
    new_file_5.write(f"{quote[1]}\n")

# ................................................................
# Eighth question

