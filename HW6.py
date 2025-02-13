example = [1, 2, 3, 4, 5, 6]

def split_list(lst):
    mid = (len(lst) + 1) // 2
    return [lst[:mid], lst[mid:]]

print(f"{example} => {split_list(example)}")
