# Third question
import collections
from one import words

with open("out_most_frequent.txt", "w") as new_file_2:
    new_file_2 = open("out_most_frequent.txt", "w")
    cn = collections.Counter(words)
    most_common_list = cn.most_common(10)
    for i, j in enumerate(most_common_list):
        new_file_2.write(f"{i+1}. {j[0]}           {j[1]}\n")
