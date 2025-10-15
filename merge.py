def merge_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError
    combined = list1 + list2
    for item in combined:
        if not isinstance(item, int):
            raise TypeError
    n = len(combined)
    for i in range(n):
        for j in range(0, n - i - 1):
            if combined[j] > combined[j + 1]:
                combined[j], combined[j + 1] = combined[j + 1], combined[j]
    return combined
