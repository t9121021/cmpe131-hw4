def reverse_sort_dictionary(d):
    if not isinstance(d, dict):
        raise TypeError
    result = []
    for k, v in sorted(d.items(), key=lambda x: x[0], reverse=True):
        result.append((k, v[0]))
    return result
