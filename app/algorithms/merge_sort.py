def merge_sort(results):
    # Base case
    if len(results) <= 1:
        return results

    # Divide
    mid = len(results) // 2

    left = merge_sort(results[:mid])
    right = merge_sort(results[mid:])

    # Merge
    return merge(left, right)


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        # Highest compatibility score first
        if left[i].score >= right[j].score:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Remaining left elements
    while i < len(left):
        result.append(left[i])
        i += 1

    # Remaining right elements
    while j < len(right):
        result.append(right[j])
        j += 1

    return result