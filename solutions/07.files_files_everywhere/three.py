import one

dicti = {"biggest length": 0}

for file in one.list_of_files_obj:
    file.parents
    if len(file.list_of_parents) > dicti["biggest length"]:
        dicti["biggest length"] = len(file.list_of_parents)

print(dicti["biggest length"])



