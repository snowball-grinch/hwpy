import one

set_parents = set()

for file in one.list_of_files_obj:
    set_parents.update(file.parents)
    one.File.list_of_parents.clear()

if __name__ == "__main__":
    for file in one.list_of_files_obj[0: 2]:
        print(file.file_name)
        if file in set_parents:
            print(file.file_name)
            #with open("no_children.txt", "a+") as no_children:
            #    no_children.write(f"{file}")