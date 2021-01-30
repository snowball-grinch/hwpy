
# Fifth question

new_file_3 = open("out_capital_words.txt", "w")
for word in unique_words:
    if word.istitle() or word.isupper():
        new_file_3.write(f"{word} ({dic_word_frequency[word]})\n")