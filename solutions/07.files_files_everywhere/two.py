import one

set_parents = set()

for file in one.list_of_files_obj:
    set_parents.update(file.parents)
    one.File.list_of_parents.clear()

with open("no_children.txt", "w+") as no_children:
    for file in one.list_of_files_obj:
        #print(file.file_name)
        if file in set_parents:
            print(file.file_name)
            #no_children.writelines(f"{file.file_name}")
