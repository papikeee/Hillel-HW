example = [1, 2, 3, 4, 5]

def shift_last_to_first(lst):
    if len(lst) > 1:
        return [lst[-1]] + lst[:-1]
    return lst

print(f"{example} => {shift_last_to_first(example)}")

