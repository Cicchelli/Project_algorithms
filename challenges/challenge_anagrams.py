def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return (first_string, second_string, False)

    first_string = first_string.lower()
    second_string = second_string.lower()

    sorted_1 = merge_sort(list(first_string))
    sorted_2 = merge_sort(list(second_string))

    return ("".join(sorted_1), "".join(sorted_2), sorted_1 == sorted_2)


def merge_sort(string):
    def _merge_sort(string, start, end):
        if end - start > 1:
            mid = (start + end) // 2
            _merge_sort(string, start, mid)
            _merge_sort(string, mid, end)
            merge(string, start, mid, end)

    _merge_sort(string, 0, len(string))
    return string


def merge(string, start, mid, end):
    left = string[start:mid]
    right = string[mid:end]

    left_index, right_index = 0, 0
    general_index = start

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            string[general_index] = left[left_index]
            left_index += 1
        else:
            string[general_index] = right[right_index]
            right_index += 1
        general_index += 1

    while left_index < len(left):
        string[general_index] = left[left_index]
        left_index += 1
        general_index += 1

    while right_index < len(right):
        string[general_index] = right[right_index]
        right_index += 1
        general_index += 1
