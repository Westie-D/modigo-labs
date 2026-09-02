def remove_duplicates(items):
    New_list = []
    
    for item in items:
        if item not in New_list:
            New_list.append(item)# TODO: use a loop to build a new list with duplicates removed, keeping first occurrences
    return New_list