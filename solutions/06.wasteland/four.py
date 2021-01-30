# Fourth question

from tow import collections, word_frequency
from one import poem_content

ord_dict = collections.OrderedDict()
dic_word_frequency = word_frequency(poem_content)
longest_words = sorted(dic_word_frequency, key=lambda x: len(x), reverse=True)

for word in longest_words[0: 5]:
    ord_dict[word] = dic_word_frequency[word]
